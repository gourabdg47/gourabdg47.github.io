using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

namespace FocusTime
{
    public class CircularProgressBar : UserControl
    {
        private int _value;
        private int _maximum = 100;
        private Color _progressColor = Color.Coral;
        private Color _textColor = Color.FromArgb(75, 85, 199); // Default to primaryColor from MainForm
        private float _progressThickness = 10f;
        private float _backgroundThickness = 10f;
        private Color _backgroundColorCircular = Color.LightGray;

        public int Value
        {
            get => _value;
            set
            {
                if (value < 0) _value = 0;
                else if (value > _maximum) _value = _maximum;
                else _value = value;
                this.Invalidate(); // Redraw control when value changes
            }
        }

        public int Maximum
        {
            get => _maximum;
            set
            {
                if (value < 1) _maximum = 1;
                else _maximum = value;
                if (_value > _maximum) _value = _maximum;
                this.Invalidate();
            }
        }

        public Color ProgressColor
        {
            get => _progressColor;
            set
            {
                _progressColor = value;
                this.Invalidate();
            }
        }

        public Color TextColor
        {
            get => _textColor;
            set
            {
                _textColor = value;
                this.Invalidate();
            }
        }

        public CircularProgressBar()
        {
            this.DoubleBuffered = true;
            this.Size = new Size(150, 150); // Default size
            this.BackColor = Color.Transparent; // Default background for the control itself
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            float diameter = Math.Min(this.Width, this.Height) - _progressThickness;
            RectangleF rect = new RectangleF(
                (this.Width - diameter) / 2,
                (this.Height - diameter) / 2,
                diameter,
                diameter);

            // Draw background circle
            using (Pen backgroundPen = new Pen(_backgroundColorCircular, _backgroundThickness))
            {
                e.Graphics.DrawEllipse(backgroundPen, rect);
            }

            // Draw progress arc
            if (_maximum > 0 && _value > 0)
            {
                float sweepAngle = 360f * _value / _maximum;
                using (Pen progressPen = new Pen(_progressColor, _progressThickness))
                {
                    progressPen.StartCap = LineCap.Round;
                    progressPen.EndCap = LineCap.Round;
                    e.Graphics.DrawArc(progressPen, rect, -90, sweepAngle);
                }
            }

            // Optionally, draw text (e.g., percentage) in the center
            // string text = $"{(_value * 100 / _maximum)}%";
            // using (Font font = new Font(this.Font.FontFamily, Math.Max(8, diameter / 5), FontStyle.Bold))
            // using (SolidBrush textBrush = new SolidBrush(_textColor))
            // e.Graphics.DrawString(text, font, textBrush, rect, new StringFormat { Alignment = StringAlignment.Center, LineAlignment = StringAlignment.Center });
        }
    }
}