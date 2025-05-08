using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using System.Threading;
using System.Windows.Forms;
using System.Drawing;
using System.IO;
using System.Xml.Serialization;
#nullable disable

namespace FocusTime
{
    // Moved BlockMode definition here so it's available before MainForm
    public enum BlockMode
    {
        Gentle, // Just minimize other apps (no refocusing)
        Moderate, // Minimize and refocus to selected app
        Strict // Close other apps (only when they are brought to the foreground)
    }

    // Updated FocusMode enum
    public enum FocusMode
    {
        Ember,   // Formerly Simple: Beginner – Gentle Heat
        Forge,   // Formerly Iron: Intermediate – Structured Pressure
        Obsidian // New: Advanced – Ruthless Clarity
    }

    public class AppSettings
    {
        public bool MinimizeToTray { get; set; }
        public BlockMode BlockMode { get; set; }
        public List<string> WhitelistedApps { get; set; } = new List<string>();
        public int BlockingIntervalMs { get; set; }
        public bool NotificationEnabled { get; set; } = true; // General session notifications
        public FocusMode Mode { get; set; } = FocusMode.Ember; // Default to Ember
        public bool EnableHealthReminders { get; set; } = true; // New setting for health reminders
    }


    public class Program
    {
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }

    public class MainForm : Form
    {
        // Main Panel Controls
        private Panel mainPanel;
        private CheckedListBox focusAppCheckedListBox;
        private Button startButton;
        private NumericUpDown minutesInput;
        private Label timerLabel;
        private Button settingsButton;

        // Settings Panel Controls
        private Panel settingsPanel;
        private CheckBox minimizeToTrayCheckbox;
        private GroupBox blockModeGroupBox;
        private ComboBox blockModeComboBox;
        private GroupBox whitelistGroupBox;
        private ListBox whitelistBox;
        private TextBox addWhitelistTextBox;
        private Button addWhitelistButton;
        private Button removeWhitelistButton;
        private Button settingsApplyButton;
        private Button settingsCancelButton;
        private Button buttonCoffee;
        private PictureBox pictureBoxHealthInfo;
        private ToolTip toolTip1;

        // Optimization Settings Controls
        private GroupBox optimizationGroupBox;
        private Label blockingIntervalLabel;
        private NumericUpDown blockingIntervalInput;
        private CheckBox enableNotificationsCheckbox;

        // Focus Mode Controls
        private GroupBox focusModeGroupBox;
        private Label focusModeLabel;
        private ComboBox focusModeComboBoxControl;
        private Label focusModeTaglineLabel; // New label for tagline

        // Health Reminder Controls
        private GroupBox healthRemindersGroupBox;
        private CheckBox enableHealthRemindersCheckbox;

        // Footer Panel Controls
        private Panel footerPanel;
        private Label footerQuoteLabel;
        private System.Windows.Forms.Timer quoteTimer;
        private List<string> motivationalQuotes = new List<string>
        {
            "The best way to predict the future is to create it.",
            "The only way to do great work is to love what you do.",
            "Believe you can and you're halfway there.",
            "Your time is limited, don't waste it living someone else's life.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Strive not to be a success, but rather to be of value.",
            "The mind is everything. What you think you become.",
            "Either you run the day, or the day runs you.",
            "The only impossible journey is the one you never begin.",
            "The only limit to our realization of tomorrow will be our doubts of today.",
            "Do what you can, with all you have, wherever you are.",
            "The successful warrior is the average man, with laser-like focus.",
            "Your focus determines your reality.",
            "Concentration is the root of all the higher abilities in man.",
            "The key is not to prioritize what's on your schedule, but to schedule your priorities.",
            "The difference between ordinary and extraordinary is that little extra.",
            "Today's actions are tomorrow's results.",
            "The journey of a thousand miles begins with a single step.",
            "Don't watch the clock; do what it does. Keep going.",
            "The harder the conflict, the more glorious the triumph.",
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "The only way to achieve the impossible is to believe it is possible.",
            "The best revenge is massive success.",
            "Opportunities don't happen, you create them.",
            "It's not what you look at that matters, it's what you see.",
            "The mind is not a vessel to be filled, but a fire to be kindled.",
            "The function of leadership is to produce more leaders, not more followers.",
            "Innovation distinguishes between a leader and a follower.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
            "The only person you are destined to become is the person you decide to be.",
            "The greatest glory in living lies not in never falling, but in rising every time we fall.",
            "The way to get started is to quit talking and begin doing.",
            "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work.",
            "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
            "Life is what happens when you're busy making other plans.",
            "Success usually comes to those who are too busy to be looking for it.",
            "The only way to do great work is to love what you do.",
            "The best way to predict the future is to create it.",
            "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it."
        };
        private Random random = new Random();

        // Timers and other state
        private System.Windows.Forms.Timer countdownTimer;
        private List<ProcessInfo> runningApps;
        private FocusSession activeSession;
        private System.Windows.Forms.Timer blockingTimer;
        private NotifyIcon trayIcon;
        private AppSettings settings;
        private string settingsPath = Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData),
            "FocusTime",
            "settings.xml");

        // Health Reminder Timers
        private System.Windows.Forms.Timer eyeStrainTimer;
        private System.Windows.Forms.Timer standUpTimer;
        private System.Windows.Forms.Timer hydrationTimer;

        // P/Invoke declarations
        [DllImport("user32.dll")]
        private static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
        [DllImport("user32.dll")]
        private static extern IntPtr GetForegroundWindow();
        [DllImport("user32.dll")]
        private static extern bool SetForegroundWindow(IntPtr hWnd);
        [DllImport("user32.dll", SetLastError = true)]
        static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint lpdwProcessId);

        private const int SW_MINIMIZE = 6;
        private const int SW_RESTORE = 9;
        private const int SHORT_DELAY_MS = 50;
        private const int NOTIFICATION_DURATION_MS = 7000;

        private Color defaultBackColor = SystemColors.Control;
        private Color defaultPanelColor = SystemColors.ControlLightLight;
        private Color defaultTextColor = SystemColors.ControlText;
        private Color defaultHighlightColor = SystemColors.Highlight;
        private Color defaultErrorColor = SystemColors.ControlDarkDark;

        private decimal previousMinutesValue = 25; // To store minutes value before switching to Obsidian

        public MainForm()
        {
            LoadSettings();
            InitializeComponent();
            PopulateInstalledApps();
            ShowMainPanel();
            UpdateMotivationalQuote();
            quoteTimer.Start();
        }

        private void LoadSettings()
        {
            try
            {
                string directory = Path.GetDirectoryName(settingsPath);
                if (!Directory.Exists(directory))
                {
                    Directory.CreateDirectory(directory);
                }

                if (File.Exists(settingsPath))
                {
                    using (var reader = new StreamReader(settingsPath))
                    {
                        XmlSerializer serializer = new XmlSerializer(typeof(AppSettings));
                        settings = (AppSettings)serializer.Deserialize(reader);
                        if (settings.WhitelistedApps == null)
                        {
                            settings.WhitelistedApps = new List<string>();
                        }
                        if (settings.BlockingIntervalMs == 0) settings.BlockingIntervalMs = 250;
                    }
                }
                else
                {
                    settings = new AppSettings
                    {
                        MinimizeToTray = true,
                        BlockMode = BlockMode.Gentle,
                        WhitelistedApps = new List<string> { "explorer", "devenv", "code", "msedge", "chrome", "firefox" },
                        BlockingIntervalMs = 250,
                        NotificationEnabled = true,
                        Mode = FocusMode.Ember, // Default to Ember
                        EnableHealthReminders = true
                    };
                    SaveSettings();
                }
            }
            catch (Exception)
            {
                settings = new AppSettings
                {
                    MinimizeToTray = true,
                    BlockMode = BlockMode.Gentle,
                    WhitelistedApps = new List<string> { "explorer", "devenv", "code", "msedge", "chrome", "firefox" },
                    BlockingIntervalMs = 250,
                    NotificationEnabled = true,
                    Mode = FocusMode.Ember, // Default to Ember
                    EnableHealthReminders = true
                };
                MessageBox.Show("Failed to load settings. Using default settings.", "Settings Load Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void SaveSettings()
        {
            try
            {
                string directory = Path.GetDirectoryName(settingsPath);
                if (!Directory.Exists(directory))
                {
                    Directory.CreateDirectory(directory);
                }

                using (var writer = new StreamWriter(settingsPath))
                {
                    XmlSerializer serializer = new XmlSerializer(typeof(AppSettings));
                    serializer.Serialize(writer, settings);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Failed to save settings: {ex.Message}", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void InitializeComponent()
        {
            this.Text = "FocusTime";
            this.Size = new Size(540, 700); // Adjusted height for new tagline label
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Icon = Icon.ExtractAssociatedIcon(Application.ExecutablePath);
            this.FormClosing += MainForm_FormClosing;
            this.Padding = new Padding(10);
            this.BackColor = defaultBackColor;

            // --- Main Panel Setup ---
            mainPanel = new Panel
            {
                Dock = DockStyle.Fill,
                Padding = new Padding(10),
                BackColor = defaultPanelColor
            };
            this.Controls.Add(mainPanel);

            Label appSelectLabel = new Label { Text = "Select application(s) to keep focused on:", Location = new Point(10, 10), AutoSize = true, Font = new Font(this.Font.FontFamily, 10, FontStyle.Bold), ForeColor = defaultTextColor };
            mainPanel.Controls.Add(appSelectLabel);
            focusAppCheckedListBox = new CheckedListBox { Location = new Point(10, 35), Width = 480, Height = 150, CheckOnClick = true, BackColor = SystemColors.Window, ForeColor = defaultTextColor, BorderStyle = BorderStyle.FixedSingle };
            mainPanel.Controls.Add(focusAppCheckedListBox);

            Label timeLabelCtrl = new Label { Text = "Focus time (minutes):", Location = new Point(10, 200), AutoSize = true, Font = new Font(this.Font.FontFamily, 10, FontStyle.Bold), ForeColor = defaultTextColor };
            mainPanel.Controls.Add(timeLabelCtrl);
            minutesInput = new NumericUpDown { Location = new Point(10, 225), Width = 100, Minimum = 1, Maximum = 720, Value = 25, BackColor = SystemColors.Window, ForeColor = defaultTextColor }; // Max increased for Obsidian
            mainPanel.Controls.Add(minutesInput);
            timerLabel = new Label { Text = "00:00:00", Location = new Point(150, 225), AutoSize = true, Font = new Font("Arial", 18, FontStyle.Bold), TextAlign = ContentAlignment.MiddleCenter, ForeColor = defaultTextColor };
            mainPanel.Controls.Add(timerLabel);

            startButton = new Button { Text = "Start Focus Session", Location = new Point(10, 280), Width = 200, Height = 50, Font = new Font(this.Font.FontFamily, 12, FontStyle.Bold), FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true };
            startButton.Click += StartButton_Click;
            mainPanel.Controls.Add(startButton);
            settingsButton = new Button { Text = "Settings", Location = new Point(startButton.Right + 10, 280), Width = 100, Height = 50, Font = new Font(this.Font.FontFamily, 10, FontStyle.Regular), FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true };
            settingsButton.Click += SettingsButton_Click;
            mainPanel.Controls.Add(settingsButton);

            Label infoLabel1 = new Label { Text = "Select the applications you want to stay focused on during your session.", Location = new Point(10, 340), Width = 480, AutoSize = false, ForeColor = defaultTextColor, Font = new Font(this.Font.FontFamily, 9, FontStyle.Italic) };
            mainPanel.Controls.Add(infoLabel1);
            Label infoLabel2 = new Label { Text = "Set the duration of your focus session in minutes.", Location = new Point(10, 255), Width = 480, AutoSize = false, ForeColor = defaultTextColor, Font = new Font(this.Font.FontFamily, 9, FontStyle.Italic) };
            mainPanel.Controls.Add(infoLabel2);

            // --- Settings Panel Setup ---
            settingsPanel = new Panel { Dock = DockStyle.Fill, Padding = new Padding(10), BackColor = defaultPanelColor };
            this.Controls.Add(settingsPanel);
            int currentY = 10;

            minimizeToTrayCheckbox = new CheckBox { Text = "Minimize to system tray when closing", Location = new Point(10, currentY), Width = 480, ForeColor = defaultTextColor };
            settingsPanel.Controls.Add(minimizeToTrayCheckbox);
            currentY += minimizeToTrayCheckbox.Height + 10;

            blockModeGroupBox = new GroupBox { Text = "Blocking Mode", Location = new Point(10, currentY), Size = new Size(480, 80), Padding = new Padding(10), ForeColor = defaultTextColor };
            settingsPanel.Controls.Add(blockModeGroupBox);
            Label blockModeLabel = new Label { Text = "Select how non-focus apps are handled:", Location = new Point(10, 20), AutoSize = true, ForeColor = defaultTextColor };
            blockModeGroupBox.Controls.Add(blockModeLabel);
            blockModeComboBox = new ComboBox { Location = new Point(10, 45), Width = 460, DropDownStyle = ComboBoxStyle.DropDownList, BackColor = SystemColors.Window, ForeColor = defaultTextColor };
            blockModeComboBox.Items.AddRange(new object[] { "Gentle - Minimize other apps", "Moderate - Minimize and refocus to selected app", "Strict - Close other apps" });
            blockModeComboBox.SelectedIndex = (int)settings.BlockMode;
            blockModeGroupBox.Controls.Add(blockModeComboBox);
            currentY += blockModeGroupBox.Height + 10;

            whitelistGroupBox = new GroupBox { Text = "Whitelisted Apps (Process Names, e.g., 'explorer')", Location = new Point(10, currentY), Size = new Size(480, 150), Padding = new Padding(10), ForeColor = defaultTextColor };
            settingsPanel.Controls.Add(whitelistGroupBox);
            whitelistBox = new ListBox { Location = new Point(10, 20), Width = 460, Height = 60, BackColor = SystemColors.Window, ForeColor = defaultTextColor, BorderStyle = BorderStyle.FixedSingle };
            whitelistGroupBox.Controls.Add(whitelistBox);
            addWhitelistTextBox = new TextBox { Location = new Point(10, 90), Width = 280, BackColor = SystemColors.Window, ForeColor = defaultTextColor };
            whitelistGroupBox.Controls.Add(addWhitelistTextBox);
            addWhitelistButton = new Button { Text = "Add", Location = new Point(addWhitelistTextBox.Right + 10, 89), Width = 80, FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true };
            addWhitelistButton.Click += AddWhitelistButton_Click;
            whitelistGroupBox.Controls.Add(addWhitelistButton);
            removeWhitelistButton = new Button { Text = "Remove", Location = new Point(addWhitelistButton.Right + 10, 89), Width = 80, FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true };
            removeWhitelistButton.Click += RemoveWhitelistButton_Click;
            whitelistGroupBox.Controls.Add(removeWhitelistButton);
            currentY += whitelistGroupBox.Height + 10;

            optimizationGroupBox = new GroupBox { Text = "Performance & Session Notifications", Location = new Point(10, currentY), Size = new Size(480, 80), Padding = new Padding(10), ForeColor = defaultTextColor };
            settingsPanel.Controls.Add(optimizationGroupBox);
            blockingIntervalLabel = new Label { Text = "Blocking check interval (ms):", Location = new Point(10, 20), AutoSize = true, ForeColor = defaultTextColor };
            optimizationGroupBox.Controls.Add(blockingIntervalLabel);
            blockingIntervalInput = new NumericUpDown { Location = new Point(220, 17), Width = 100, Minimum = 100, Maximum = 5000, Increment = 50, Value = settings.BlockingIntervalMs, BackColor = SystemColors.Window, ForeColor = defaultTextColor };
            optimizationGroupBox.Controls.Add(blockingIntervalInput);
            enableNotificationsCheckbox = new CheckBox { Text = "Enable session start/end notifications", Location = new Point(10, 45), Width = 460, Checked = settings.NotificationEnabled, ForeColor = defaultTextColor };
            optimizationGroupBox.Controls.Add(enableNotificationsCheckbox);
            currentY += optimizationGroupBox.Height + 10;

            healthRemindersGroupBox = new GroupBox { Text = "Health Reminders", Location = new Point(10, currentY), Size = new Size(480, 50), Padding = new Padding(10), ForeColor = defaultTextColor };
            settingsPanel.Controls.Add(healthRemindersGroupBox);
            enableHealthRemindersCheckbox = new CheckBox { Text = "Enable health and posture reminders during session", Location = new Point(10, 20), AutoSize = true, Checked = settings.EnableHealthReminders, ForeColor = defaultTextColor };
            healthRemindersGroupBox.Controls.Add(enableHealthRemindersCheckbox);
            pictureBoxHealthInfo = new PictureBox
            {
                Name = "pictureBoxHealthInfo", Size = new Size(16, 16), SizeMode = PictureBoxSizeMode.StretchImage, Cursor = Cursors.Help, BackColor = Color.Transparent, Image = SystemIcons.Information.ToBitmap(),
                Location = new Point(enableHealthRemindersCheckbox.Right + 5, enableHealthRemindersCheckbox.Top + (enableHealthRemindersCheckbox.Height - 16) / 2)
            };
            healthRemindersGroupBox.Controls.Add(pictureBoxHealthInfo);
            toolTip1 = new ToolTip();
            toolTip1.SetToolTip(pictureBoxHealthInfo, "Health Reminders Intervals:\n- Eye Strain (20-20-20 Rule): Every 20 minutes\n- Movement: Every 30 minutes\n- Hydration: Every 45 minutes");
            currentY += healthRemindersGroupBox.Height + 10;

            // Focus Mode GroupBox - Updated
            focusModeGroupBox = new GroupBox { Text = "Focus Mode", Location = new Point(10, currentY), Size = new Size(480, 100), Padding = new Padding(10), ForeColor = defaultTextColor }; // Increased height for tagline
            settingsPanel.Controls.Add(focusModeGroupBox);
            focusModeLabel = new Label { Text = "Select focus mode:", Location = new Point(10, 20), AutoSize = true, ForeColor = defaultTextColor };
            focusModeGroupBox.Controls.Add(focusModeLabel);
            focusModeComboBoxControl = new ComboBox { Location = new Point(150, 17), Width = 310, DropDownStyle = ComboBoxStyle.DropDownList, BackColor = SystemColors.Window, ForeColor = defaultTextColor };
            focusModeComboBoxControl.Items.AddRange(new object[] {
                "Ember 🔥 (Beginner – Gentle Heat)",
                "Forge ⚒️ (Intermediate – Structured Pressure)",
                "Obsidian 🖤 (Advanced – Ruthless Clarity)"
            });
            focusModeComboBoxControl.SelectedIndexChanged += FocusModeComboBoxControl_SelectedIndexChanged; // Event handler added
            focusModeGroupBox.Controls.Add(focusModeComboBoxControl);

            // New Tagline Label
            focusModeTaglineLabel = new Label
            {
                Text = "", // Initial text will be set by event handler or LoadSettingsPanel
                Location = new Point(10, focusModeComboBoxControl.Bottom + 8), // Position below combobox
                Width = focusModeGroupBox.ClientSize.Width - 20,
                Height = 30, // Allow space for two lines if needed
                AutoSize = false,
                TextAlign = ContentAlignment.TopCenter,
                ForeColor = defaultTextColor, // Or a more subtle color like SystemColors.GrayText
                Font = new Font(this.Font.FontFamily, 8.25F, FontStyle.Italic)
            };
            focusModeGroupBox.Controls.Add(focusModeTaglineLabel);
            currentY += focusModeGroupBox.Height + 20; // Adjusted Y for next controls

            // Apply/Cancel buttons
            int buttonY = currentY;
            settingsApplyButton = new Button { Text = "Apply", Location = new Point(480 - 80 - 80 - 10, buttonY), Width = 80, Height = 25, FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true };
            settingsApplyButton.Click += SettingsApplyButton_Click;
            settingsPanel.Controls.Add(settingsApplyButton);
            settingsCancelButton = new Button { Text = "Cancel", Location = new Point(480 - 80, buttonY), Width = 80, Height = 25, FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true };
            settingsCancelButton.Click += SettingsCancelButton_Click;
            settingsPanel.Controls.Add(settingsCancelButton);

            buttonCoffee = new Button
            {
                Name = "buttonCoffee", Text = "☕ Buy Me a Coffee", Location = new Point(settingsPanel.Padding.Left, buttonY), Width = 150, Height = 25,
                Cursor = Cursors.Hand, FlatStyle = FlatStyle.System, UseVisualStyleBackColor = true, Font = new Font(this.Font.FontFamily, 9, FontStyle.Regular)
            };
            toolTip1.SetToolTip(buttonCoffee, "Support the developer!");
            buttonCoffee.Click += ButtonCoffee_Click;
            settingsPanel.Controls.Add(buttonCoffee);

            int requiredPanelHeight = buttonY + settingsApplyButton.Height + 10;
            int mainPanelRequiredHeight = infoLabel1.Bottom + 10;
            int requiredFormHeight = Math.Max(requiredPanelHeight, mainPanelRequiredHeight) + this.Padding.Top + this.Padding.Bottom + 40; // +40 for footer
            this.ClientSize = new Size(this.ClientSize.Width, requiredFormHeight);

            // --- Footer Panel Setup ---
            footerPanel = new Panel
            {
                Dock = DockStyle.Bottom, Height = 40, Padding = new Padding(10, 5, 10, 5),
                BackColor = Color.PaleGreen, ForeColor = SystemColors.ControlText
            };
            this.Controls.Add(footerPanel);
            footerQuoteLabel = new Label
            {
                Text = "", Location = new Point(10, 5), AutoSize = false, Width = footerPanel.ClientSize.Width - 20,
                TextAlign = ContentAlignment.MiddleCenter, Font = new Font(this.Font.FontFamily, 9, FontStyle.Italic), ForeColor = SystemColors.ControlText
            };
            footerQuoteLabel.Location = new Point((footerPanel.ClientSize.Width - footerQuoteLabel.Width) / 2, 5);
            footerPanel.Controls.Add(footerQuoteLabel);

            // --- Timer Setup ---
            countdownTimer = new System.Windows.Forms.Timer { Interval = 1000 };
            countdownTimer.Tick += CountdownTimer_Tick;
            blockingTimer = new System.Windows.Forms.Timer { Interval = settings.BlockingIntervalMs };
            blockingTimer.Tick += BlockingTimer_Tick;
            quoteTimer = new System.Windows.Forms.Timer { Interval = 30000 };
            quoteTimer.Tick += QuoteTimer_Tick;

            eyeStrainTimer = new System.Windows.Forms.Timer { Interval = 20 * 60 * 1000 };
            eyeStrainTimer.Tick += EyeStrainTimer_Tick;
            standUpTimer = new System.Windows.Forms.Timer { Interval = 30 * 60 * 1000 };
            standUpTimer.Tick += StandUpTimer_Tick;
            hydrationTimer = new System.Windows.Forms.Timer { Interval = 45 * 60 * 1000 };
            hydrationTimer.Tick += HydrationTimer_Tick;

            trayIcon = new NotifyIcon { Icon = Icon.ExtractAssociatedIcon(Application.ExecutablePath), Text = "FocusTime", Visible = false };
            trayIcon.DoubleClick += TrayIcon_DoubleClick;
            ContextMenuStrip trayMenu = new ContextMenuStrip();
            trayMenu.Items.Add("Show", null, TrayShow_Click);
            trayMenu.Items.Add("Stop Session", null, TrayStop_Click);
            trayMenu.Items.Add("Exit", null, TrayExit_Click);
            trayIcon.ContextMenuStrip = trayMenu;

            // Set initial state of focus mode controls after all controls are initialized
            // This ensures focusModeTaglineLabel is not null
            if (focusModeComboBoxControl.Items.Count > 0)
            {
                 UpdateControlsForFocusMode((FocusMode)settings.Mode); // Call this to set initial tagline and minutes
            }
        }

        private string GetTaglineForMode(FocusMode mode)
        {
            switch (mode)
            {
                case FocusMode.Ember: return "Ember 🔥: Start the fire.";
                case FocusMode.Forge: return "Forge ⚒️: Shape yourself through action.";
                case FocusMode.Obsidian: return "Obsidian 🖤: No excuses. Just results.";
                default: return "";
            }
        }

        private void UpdateControlsForFocusMode(FocusMode mode)
        {
            if (focusModeTaglineLabel == null) return; // Guard against early calls during init

            focusModeTaglineLabel.Text = GetTaglineForMode(mode);

            if (mode == FocusMode.Obsidian)
            {
                if (minutesInput.Value != 120) // Only store if not already Obsidian's default
                {
                    // Check if previousMinutesValue is not already 120 to avoid overwriting a legitimate user value with Obsidian's default
                    if (previousMinutesValue != 120 ) previousMinutesValue = minutesInput.Value;
                }
                minutesInput.Value = 120;
            }
            else // Ember or Forge
            {
                // If current value is Obsidian's default (120), revert to stored previous value or a standard default (25).
                if (minutesInput.Value == 120)
                {
                    minutesInput.Value = (previousMinutesValue > 0 && previousMinutesValue <= minutesInput.Maximum && previousMinutesValue != 120) ? previousMinutesValue : 25;
                }
                // Ensure value is within bounds and not zero.
                if (minutesInput.Value > minutesInput.Maximum) minutesInput.Value = minutesInput.Maximum;
                if (minutesInput.Value < minutesInput.Minimum) minutesInput.Value = minutesInput.Minimum;
                if (minutesInput.Value == 0) minutesInput.Value = 25; // Fallback
            }
        }


        private void FocusModeComboBoxControl_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (focusModeComboBoxControl.SelectedIndex == -1) return;
            FocusMode selectedMode = (FocusMode)focusModeComboBoxControl.SelectedIndex;
            UpdateControlsForFocusMode(selectedMode);
        }


        private void UpdateMotivationalQuote()
        {
            if (motivationalQuotes.Count > 0)
            {
                int index = random.Next(motivationalQuotes.Count);
                footerQuoteLabel.Text = motivationalQuotes[index];
            }
        }

        private void QuoteTimer_Tick(object sender, EventArgs e)
        {
            UpdateMotivationalQuote();
        }

        private void ShowMainPanel()
        {
            settingsPanel.Hide();
            mainPanel.Show();
            mainPanel.BringToFront();
            this.Text = "FocusTime";
            buttonCoffee.Enabled = (activeSession == null);
        }

        private void ShowSettingsPanel()
        {
            mainPanel.Hide();
            LoadSettingsPanel(); // This will set the combo box and trigger UpdateControlsForFocusMode
            settingsPanel.Show();
            settingsPanel.BringToFront();
            this.Text = "FocusTime Settings";
            buttonCoffee.Enabled = true;
        }

        private void LoadSettingsPanel()
        {
            minimizeToTrayCheckbox.Checked = settings.MinimizeToTray;
            blockModeComboBox.SelectedIndex = (int)settings.BlockMode;
            whitelistBox.Items.Clear();
            if (settings.WhitelistedApps != null)
            {
                foreach (string app in settings.WhitelistedApps)
                {
                    whitelistBox.Items.Add(app);
                }
            }
            blockingIntervalInput.Value = settings.BlockingIntervalMs;
            enableNotificationsCheckbox.Checked = settings.NotificationEnabled;
            
            // Set selected index for focus mode. This will also trigger SelectedIndexChanged
            // which in turn calls UpdateControlsForFocusMode to set tagline and minutesInput.
            focusModeComboBoxControl.SelectedIndex = (int)settings.Mode;
            
            // If SelectedIndexChanged didn't fire (e.g. index was already set to settings.Mode),
            // explicitly call UpdateControlsForFocusMode to ensure UI is correct.
            // This is also called at the end of InitializeComponent.
            UpdateControlsForFocusMode((FocusMode)settings.Mode);

            enableHealthRemindersCheckbox.Checked = settings.EnableHealthReminders;
        }

        private void SettingsApplyButton_Click(object sender, EventArgs e)
        {
            settings.MinimizeToTray = minimizeToTrayCheckbox.Checked;
            settings.BlockMode = (BlockMode)blockModeComboBox.SelectedIndex;
            settings.WhitelistedApps.Clear();
            foreach (string app in whitelistBox.Items)
            {
                settings.WhitelistedApps.Add(app.ToString());
            }
            settings.BlockingIntervalMs = (int)blockingIntervalInput.Value;
            settings.NotificationEnabled = enableNotificationsCheckbox.Checked;
            settings.Mode = (FocusMode)focusModeComboBoxControl.SelectedIndex;
            settings.EnableHealthReminders = enableHealthRemindersCheckbox.Checked;
            SaveSettings();
            blockingTimer.Interval = settings.BlockingIntervalMs;
            ShowMainPanel();
        }

        private void SettingsCancelButton_Click(object sender, EventArgs e)
        {
            ShowMainPanel();
        }

        private void AddWhitelistButton_Click(object sender, EventArgs e)
        {
            string appName = addWhitelistTextBox.Text.Trim();
            if (!string.IsNullOrEmpty(appName))
            {
                bool alreadyExists = whitelistBox.Items.Cast<string>().Any(item => item.Equals(appName, StringComparison.OrdinalIgnoreCase));
                if (!alreadyExists)
                {
                    whitelistBox.Items.Add(appName);
                    addWhitelistTextBox.Text = "";
                    addWhitelistTextBox.Focus();
                }
                else
                {
                    MessageBox.Show("This application is already in the whitelist.", "Duplicate Entry", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
        }

        private void RemoveWhitelistButton_Click(object sender, EventArgs e)
        {
            if (whitelistBox.SelectedIndex != -1)
            {
                whitelistBox.Items.RemoveAt(whitelistBox.SelectedIndex);
            }
            else
            {
                MessageBox.Show("Please select an application from the list to remove.", "Nothing Selected", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Updated to check for Forge or Obsidian mode
            if (activeSession != null && (settings.Mode == FocusMode.Forge || settings.Mode == FocusMode.Obsidian) && e.CloseReason == CloseReason.UserClosing)
            {
                MessageBox.Show($"Cannot exit FocusTime while in {settings.Mode} mode with an active session. Please wait for the timer to finish.", $"{settings.Mode} Mode Restriction", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                e.Cancel = true;
                return;
            }
            if (settings.MinimizeToTray && (activeSession != null || e.CloseReason == CloseReason.UserClosing))
            {
                e.Cancel = true;
                this.Hide();
                trayIcon.Visible = true;
                if (settings.NotificationEnabled)
                {
                    string message = activeSession != null ? "FocusTime is still running in the background with an active session." : "FocusTime is minimized to the system tray.";
                    trayIcon.ShowBalloonTip(3000, "FocusTime", message, ToolTipIcon.Info);
                }
            }
            else if (activeSession != null && e.CloseReason == CloseReason.UserClosing)
            {
                DialogResult result = MessageBox.Show("A focus session is currently active. Are you sure you want to exit?", "Confirm Exit", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (result == DialogResult.No)
                {
                    e.Cancel = true;
                }
                else
                {
                    StopFocusSession();
                }
            }
        }

        private void TrayShow_Click(object sender, EventArgs e)
        {
            this.Show();
            this.WindowState = FormWindowState.Normal;
            trayIcon.Visible = false;
            ShowMainPanel();
        }

        private void TrayStop_Click(object sender, EventArgs e)
        {
            // Updated to check for Forge or Obsidian mode
            if (activeSession != null && (settings.Mode == FocusMode.Forge || settings.Mode == FocusMode.Obsidian))
            {
                MessageBox.Show($"Cannot stop the focus session while in {settings.Mode} mode. Please wait for the timer to finish.", $"{settings.Mode} Mode Restriction", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            StopFocusSession();
            this.Show();
            this.WindowState = FormWindowState.Normal;
            trayIcon.Visible = false;
            ShowMainPanel();
        }

        private void TrayExit_Click(object sender, EventArgs e)
        {
            // Updated to check for Forge or Obsidian mode
            if (activeSession != null && (settings.Mode == FocusMode.Forge || settings.Mode == FocusMode.Obsidian))
            {
                MessageBox.Show($"Cannot exit FocusTime while in {settings.Mode} mode with an active session. Please wait for the timer to finish.", $"{settings.Mode} Mode Restriction", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            StopFocusSession();
            Application.Exit();
        }

        private void TrayIcon_DoubleClick(object sender, EventArgs e)
        {
            TrayShow_Click(sender, e);
        }

        private void ButtonCoffee_Click(object sender, EventArgs e)
        {
            try
            {
                Process.Start(new ProcessStartInfo
                {
                    FileName = "cmd", Arguments = $"/c start https://buymeacoffee.com/gourabdg",
                    UseShellExecute = false, CreateNoWindow = true
                });
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Could not open the link: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void SettingsButton_Click(object sender, EventArgs e)
        {
            ShowSettingsPanel();
        }

        private void PopulateInstalledApps()
        {
            runningApps = new List<ProcessInfo>();
            focusAppCheckedListBox.Items.Clear();
            var addedProcessNames = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
            var addedDisplayStrings = new HashSet<string>();
            Process[] processes = Process.GetProcesses();
            var userProcesses = processes
                .Where(p => !string.IsNullOrEmpty(p.MainWindowTitle) && p.MainWindowHandle != IntPtr.Zero && p.SessionId == Process.GetCurrentProcess().SessionId)
                .OrderBy(p => p.ProcessName)
                .ToList();

            foreach (var process in userProcesses)
            {
                try
                {
                    string processName = process.ProcessName;
                    string mainWindowTitle = process.MainWindowTitle;
                    IntPtr mainWindowHandle = process.MainWindowHandle;
                    string displayString = $"{processName} - {mainWindowTitle}";
                    if (addedProcessNames.Add(processName))
                    {
                        runningApps.Add(new ProcessInfo { ProcessName = processName, MainWindowTitle = mainWindowTitle, MainWindowHandle = mainWindowHandle });
                    }
                    if (addedDisplayStrings.Add(displayString))
                    {
                        focusAppCheckedListBox.Items.Add(displayString);
                    }
                }
                catch (Exception ex) { Debug.WriteLine($"Error populating app: {process?.ProcessName} - {ex.Message}"); }
            }
            startButton.Enabled = focusAppCheckedListBox.Items.Count > 0;
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            if (activeSession == null)
            {
                StartFocusSession();
            }
            else
            {
                // Updated to check for Forge or Obsidian mode
                if (settings.Mode == FocusMode.Forge || settings.Mode == FocusMode.Obsidian)
                {
                    MessageBox.Show($"Cannot stop the focus session while in {settings.Mode} mode. Please wait for the timer to finish.", $"{settings.Mode} Mode Restriction", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }
                else
                {
                    StopFocusSession();
                }
            }
        }

        private void StartFocusSession()
        {
            List<string> selectedAppNames = new List<string>();
            List<string> selectedAppDisplayNames = new List<string>();
            foreach (object item in focusAppCheckedListBox.CheckedItems)
            {
                string displayString = item.ToString();
                string processName = GetProcessNameFromSelection(displayString);
                if (!string.IsNullOrEmpty(processName))
                {
                    selectedAppNames.Add(processName);
                    selectedAppDisplayNames.Add(displayString);
                }
            }
            if (selectedAppNames.Count == 0)
            {
                MessageBox.Show("Please select at least one application to focus on.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int minutes = (int)minutesInput.Value;
            if (minutes <= 0)
            {
                MessageBox.Show("Focus time must be at least 1 minute.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            DateTime endTime = DateTime.Now.AddMinutes(minutes);
            activeSession = new FocusSession { FocusAppNames = selectedAppNames, EndTime = endTime };
            string appList = string.Join(", ", selectedAppDisplayNames);

            startButton.Text = "Stop Focus Session";
            // Updated to disable stop button for Forge or Obsidian mode
            if (settings.Mode == FocusMode.Forge || settings.Mode == FocusMode.Obsidian)
            {
                startButton.Enabled = false;
                if (trayIcon.ContextMenuStrip != null && trayIcon.ContextMenuStrip.Items.Count > 1) trayIcon.ContextMenuStrip.Items[1].Enabled = false; // Disable "Stop Session" in tray
            }
            else
            {
                 startButton.Enabled = true; // Ensure it's enabled for Ember
                 if (trayIcon.ContextMenuStrip != null && trayIcon.ContextMenuStrip.Items.Count > 1) trayIcon.ContextMenuStrip.Items[1].Enabled = true;
            }

            startButton.UseVisualStyleBackColor = true;
            focusAppCheckedListBox.Enabled = false;
            minutesInput.Enabled = false;
            settingsButton.Enabled = false;
            buttonCoffee.Enabled = false;

            // Minimize focus apps if in Forge or Obsidian mode (similar to old Iron mode behavior)
            if (settings.Mode == FocusMode.Forge || settings.Mode == FocusMode.Obsidian)
            {
                foreach (string focusAppName in activeSession.FocusAppNames)
                {
                    try
                    {
                        Process[] focusProcesses = Process.GetProcessesByName(focusAppName);
                        foreach (Process proc in focusProcesses.Where(p => !p.HasExited && p.MainWindowHandle != IntPtr.Zero && p.SessionId == Process.GetCurrentProcess().SessionId))
                        {
                            MinimizeWindow(proc.MainWindowHandle);
                        }
                    }
                    catch (Exception ex) { Debug.WriteLine($"[StartFocusSession - {settings.Mode}Mode] Error minimizing focus app '{focusAppName}': {ex.Message}"); }
                }
            }

            countdownTimer.Start();
            blockingTimer.Start();

            if (settings.EnableHealthReminders)
            {
                if (minutes >= 20) eyeStrainTimer.Start();
                if (minutes >= 30) standUpTimer.Start();
                if (minutes >= 45) hydrationTimer.Start();
            }

            if (settings.NotificationEnabled)
            {
                if (settings.MinimizeToTray)
                {
                    this.Hide();
                    trayIcon.Visible = true;
                    ShowNotification($"Focus session started on: {appList}. Running in background.", "FocusTime");
                } else {
                    ShowNotification($"Focus session started on: {appList}.", "FocusTime");
                }
            } else if (settings.MinimizeToTray)
            {
               this.Hide();
               trayIcon.Visible = true;
            }
        }

        private string GetProcessNameFromSelection(string selection)
        {
            int separatorIndex = selection.IndexOf(" - ");
            return separatorIndex > 0 ? selection.Substring(0, separatorIndex) : selection;
        }

        private void StopFocusSession()
        {
            if (activeSession == null) return;
            activeSession = null;
            countdownTimer.Stop();
            blockingTimer.Stop();
            eyeStrainTimer.Stop();
            standUpTimer.Stop();
            hydrationTimer.Stop();

            startButton.Text = "Start Focus Session";
            startButton.Enabled = true; // Re-enable start/stop button
            if (trayIcon.ContextMenuStrip != null && trayIcon.ContextMenuStrip.Items.Count > 1) trayIcon.ContextMenuStrip.Items[1].Enabled = true; // Re-enable "Stop Session" in tray
            
            startButton.UseVisualStyleBackColor = true;
            focusAppCheckedListBox.Enabled = true;
            minutesInput.Enabled = true;
            settingsButton.Enabled = true;
            buttonCoffee.Enabled = true;
            timerLabel.Text = "00:00:00";

            if (settings.NotificationEnabled)
            {
                ShowNotification("Focus session completed!", "FocusTime");
            }

            if (trayIcon.Visible && !settings.MinimizeToTray)
            {
                this.Show();
                this.WindowState = FormWindowState.Normal;
                trayIcon.Visible = false;
            }
            else if (trayIcon.Visible && settings.MinimizeToTray)
            {
                trayIcon.Text = "FocusTime - Idle";
            }
            else if (!trayIcon.Visible && this.Visible == false)
            {
                this.Show();
                this.WindowState = FormWindowState.Normal;
            }
        }

        private void CountdownTimer_Tick(object sender, EventArgs e)
        {
            if (activeSession == null)
            {
                countdownTimer.Stop();
                timerLabel.Text = "00:00:00";
                return;
            }
            TimeSpan remaining = activeSession.EndTime - DateTime.Now;
            if (remaining.TotalSeconds <= 0)
            {
                timerLabel.Text = "00:00:00";
                StopFocusSession();
                return;
            }
            timerLabel.Text = string.Format("{0:00}:{1:00}:{2:00}", (int)remaining.TotalHours, remaining.Minutes, remaining.Seconds);
            if (trayIcon.Visible) trayIcon.Text = $"FocusTime - {timerLabel.Text} remaining";
        }

        private void BlockingTimer_Tick(object sender, EventArgs e)
        {
            if (activeSession == null)
            {
                blockingTimer.Stop();
                return;
            }
            BlockNonFocusApps(activeSession.FocusAppNames);
        }

        private void EyeStrainTimer_Tick(object sender, EventArgs e)
        {
            if (settings.EnableHealthReminders)
            {
                ShowNotification("Look at something 20 feet away for 20 seconds.", "Eye Strain Reminder (20-20-20 Rule)");
            }
        }
        private void StandUpTimer_Tick(object sender, EventArgs e)
        {
            if (settings.EnableHealthReminders)
            {
                ShowNotification("Time to stand up and stretch for a bit!", "Movement Reminder");
            }
        }
        private void HydrationTimer_Tick(object sender, EventArgs e)
        {
            if (settings.EnableHealthReminders)
            {
                ShowNotification("Stay hydrated! Drink 200-300 ml of water.", "Hydration Reminder");
            }
        }

        private void ShowNotification(string text, string title, ToolTipIcon icon = ToolTipIcon.Info)
        {
            bool wasTrayIconVisible = trayIcon.Visible;
            if (!wasTrayIconVisible)
            {
                trayIcon.Visible = true;
            }
            trayIcon.ShowBalloonTip(NOTIFICATION_DURATION_MS, title, text, icon);
            if (!wasTrayIconVisible && !settings.MinimizeToTray)
            {
                System.Windows.Forms.Timer hideTrayTimer = new System.Windows.Forms.Timer { Interval = NOTIFICATION_DURATION_MS + 500 };
                hideTrayTimer.Tick += (s, ev) =>
                {
                    trayIcon.Visible = false;
                    ((System.Windows.Forms.Timer)s).Stop();
                    ((System.Windows.Forms.Timer)s).Dispose();
                };
                hideTrayTimer.Start();
            }
        }

        private void BlockNonFocusApps(List<string> focusAppNames)
        {
            IntPtr foregroundWindowHandle = GetForegroundWindow();
            Process foregroundProcess = null;
            string foregroundProcessName = "N/A";
            try
            {
                if (foregroundWindowHandle != IntPtr.Zero)
                {
                    uint processId;
                    GetWindowThreadProcessId(foregroundWindowHandle, out processId);
                    if (processId != 0)
                    {
                        try { foregroundProcess = Process.GetProcessById((int)processId); foregroundProcessName = foregroundProcess?.ProcessName ?? "Unknown"; }
                        catch (ArgumentException) { /* Process might have exited */ }
                    }
                    if (foregroundProcess != null && !foregroundProcess.HasExited && foregroundProcess.Id == Process.GetCurrentProcess().Id)
                    {
                        // FocusTime is in foreground, do nothing
                    }
                    else if (foregroundProcess != null && !foregroundProcess.HasExited)
                    {
                        bool isForegroundFocusApp = focusAppNames.Any(name => foregroundProcessName.Equals(name, StringComparison.OrdinalIgnoreCase));
                        bool isForegroundWhitelisted = settings.WhitelistedApps != null && settings.WhitelistedApps.Any(app => foregroundProcessName.Equals(app, StringComparison.OrdinalIgnoreCase));

                        if (!isForegroundFocusApp && !isForegroundWhitelisted)
                        {
                            switch (settings.BlockMode)
                            {
                                case BlockMode.Gentle:
                                    MinimizeWindow(foregroundWindowHandle);
                                    break;
                                case BlockMode.Moderate:
                                    MinimizeWindow(foregroundWindowHandle);
                                    System.Threading.Thread.Sleep(SHORT_DELAY_MS);
                                    BringAFocusAppToFront(focusAppNames);
                                    break;
                                case BlockMode.Strict:
                                    if (foregroundProcess != null && !foregroundProcess.HasExited)
                                    {
                                        try { foregroundProcess.CloseMainWindow(); System.Threading.Thread.Sleep(SHORT_DELAY_MS); BringAFocusAppToFront(focusAppNames); }
                                        catch (Exception ex) { Debug.WriteLine($"[BlockingTimer] Strict mode (Foreground): Error closing '{foregroundProcessName}': {ex.Message}"); }
                                    }
                                    break;
                            }
                        }
                    }
                }
            }
            catch (System.ComponentModel.Win32Exception ex) { Debug.WriteLine($"[BlockingTimer] Win32Exception: {ex.Message} (Code: {ex.NativeErrorCode})"); }
            catch (ArgumentException ex) { Debug.WriteLine($"[BlockingTimer] ArgumentException: {ex.Message}"); }
            catch (Exception ex) { Debug.WriteLine($"[BlockingTimer] Exception: {ex.ToString()}"); }

            if (settings.BlockMode == BlockMode.Gentle)
            {
                Process[] allProcesses = Process.GetProcesses();
                foreach (Process process in allProcesses)
                {
                    try
                    {
                        if (process.HasExited || string.IsNullOrEmpty(process.MainWindowTitle) || process.MainWindowHandle == IntPtr.Zero || process.MainWindowHandle == foregroundWindowHandle || process.Id == Process.GetCurrentProcess().Id) continue;
                        if (focusAppNames.Any(name => process.ProcessName.Equals(name, StringComparison.OrdinalIgnoreCase))) continue;
                        if (settings.WhitelistedApps != null && settings.WhitelistedApps.Any(app => process.ProcessName.Equals(app, StringComparison.OrdinalIgnoreCase))) continue;
                        MinimizeWindow(process.MainWindowHandle);
                    }
                    catch (Exception ex) { Debug.WriteLine($"[BlockingTimer] Gentle (Background) loop error for {process?.ProcessName}: {ex.Message}"); }
                }
            }
        }

        private void BringAFocusAppToFront(List<string> focusAppNames)
        {
            IntPtr targetFocusAppHandle = IntPtr.Zero;
            foreach (string focusAppName in focusAppNames)
            {
                try
                {
                    Process validProcess = Process.GetProcessesByName(focusAppName).FirstOrDefault(p => !p.HasExited && p.MainWindowHandle != IntPtr.Zero && p.SessionId == Process.GetCurrentProcess().SessionId);
                    if (validProcess != null)
                    {
                        targetFocusAppHandle = validProcess.MainWindowHandle;
                        break;
                    }
                }
                catch (Exception ex) { Debug.WriteLine($"[BlockingTimer] Error finding focus app '{focusAppName}': {ex.Message}"); }
            }
            if (targetFocusAppHandle != IntPtr.Zero)
            {
                ShowWindow(targetFocusAppHandle, SW_RESTORE);
                SetForegroundWindow(targetFocusAppHandle);
            }
        }
        private void MinimizeWindow(IntPtr handle)
        {
            if (handle != IntPtr.Zero) ShowWindow(handle, SW_MINIMIZE);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                countdownTimer?.Dispose();
                blockingTimer?.Dispose();
                eyeStrainTimer?.Dispose();
                standUpTimer?.Dispose();
                hydrationTimer?.Dispose();
                trayIcon?.Dispose();
                toolTip1?.Dispose();
                quoteTimer?.Dispose();
            }
            base.Dispose(disposing);
        }
    }

    public class FocusSession
    {
        public List<string> FocusAppNames { get; set; } = new List<string>();
        public DateTime EndTime { get; set; }
    }

    public class ProcessInfo
    {
        public string ProcessName { get; set; }
        public string MainWindowTitle { get; set; }
        public IntPtr MainWindowHandle { get; set; }
    }
}
