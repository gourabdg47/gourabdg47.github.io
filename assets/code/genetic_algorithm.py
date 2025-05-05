import random
import math
import copy
import statistics # For calculating variance
import time
import sys # To check platform

# --- Matplotlib Setup ---
# Explicitly set backend *before* importing pyplot, especially for Windows stability
# Use TkAgg as it's often more robust for interactive plots
try:
    import matplotlib
    # Set backend *before* importing pyplot
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    import numpy as np
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Warning: Matplotlib or NumPy not found. Real-time visualization disabled.")
    print("Install them using: pip install matplotlib numpy")
# --- Configuration Parameters ---

# Grid settings (for evaluating and visualizing the pattern)
GRID_SIZE = 32  # Generate patterns on a GRID_SIZE x GRID_SIZE grid

# Genetic Algorithm settings
POPULATION_SIZE = 50       # Number of individuals (potential artworks) in the population
NUM_GENERATIONS = 300      # Number of generations to run the evolution
TOURNAMENT_SIZE = 5        # Number of individuals participating in a selection tournament
MUTATION_RATE = 0.15       # Probability that a parameter in a genome will mutate
MUTATION_STRENGTH = 0.5    # Magnitude of mutation changes
CROSSOVER_RATE = 0.7       # Probability that two parents will crossover

# Genome settings (parameters for the artwork function)
NUM_SINE_COMPONENTS = 5    # Number of sine waves to sum for the function f(x,y)
PARAM_RANGES = {           # Define the typical range for each parameter
    'amplitude': (0.1, 1.0),
    'frequency': (0.1, 5.0), # Frequency in x and y
    'phase': (0, 2 * math.pi) # Phase shift in x and y
}

# Visualization settings
VISUALIZATION_ENABLED = MATPLOTLIB_AVAILABLE # Only enable if matplotlib is found
UPDATE_INTERVAL = 0.05 # Pause duration in seconds between generations for visualization

# --- Helper Functions ---

def clamp(value, min_val, max_val):
  """Clamps a value within a specified range."""
  return max(min_val, min(value, max_val))

# --- Genome and Artwork Representation ---

def create_random_genome():
  """Creates a genome with random parameters for all sine components."""
  genome = []
  for _ in range(NUM_SINE_COMPONENTS):
    component = {
        'amplitude': random.uniform(*PARAM_RANGES['amplitude']),
        'freq_x': random.uniform(*PARAM_RANGES['frequency']),
        'phase_x': random.uniform(*PARAM_RANGES['phase']),
        'freq_y': random.uniform(*PARAM_RANGES['frequency']),
        'phase_y': random.uniform(*PARAM_RANGES['phase']),
    }
    genome.append(component)
  return genome

def evaluate_artwork_function(genome, x_norm, y_norm):
  """
  Calculates the value of the artwork function f(x, y) for a given genome
  at normalized coordinates (x_norm, y_norm) between 0 and 1.
  """
  value = 0.0
  # Map normalized coordinates to a range suitable for sine waves (e.g., 0 to 2*pi)
  x_mapped = x_norm * 2 * math.pi
  y_mapped = y_norm * 2 * math.pi

  for component in genome:
    # Ensure keys exist before accessing (safer)
    amp = component.get('amplitude', 0)
    freq_x = component.get('freq_x', 1)
    phase_x = component.get('phase_x', 0)
    freq_y = component.get('freq_y', 1)
    phase_y = component.get('phase_y', 0)

    term_x = math.sin(freq_x * x_mapped + phase_x)
    term_y = math.sin(freq_y * y_mapped + phase_y)
    value += amp * term_x * term_y
  return value

def generate_pattern_grid(genome, grid_size):
    """Generates the 2D grid of values for a given genome."""
    if not genome:
        return np.zeros((grid_size, grid_size)) # Return empty grid if no genome

    grid = np.zeros((grid_size, grid_size))
    for i in range(grid_size):
        for j in range(grid_size):
            x_norm = i / (grid_size - 1) if grid_size > 1 else 0.5
            y_norm = j / (grid_size - 1) if grid_size > 1 else 0.5
            grid[i, j] = evaluate_artwork_function(genome, x_norm, y_norm)
    return grid

# --- Fitness Evaluation ---

def calculate_fitness(genome):
  """
  Calculates the fitness of a genome based on the variance of its pattern grid.
  """
  grid = generate_pattern_grid(genome, GRID_SIZE)
  # Flatten the grid to calculate variance on all values
  flat_grid = grid.flatten()

  if len(flat_grid) < 2:
      return 0.0

  try:
      # Use numpy's variance for potentially better performance on arrays
      variance = np.var(flat_grid)
  except Exception: # Catch potential numerical issues
      variance = 0.0

  return variance

# --- Genetic Operators ---
# (tournament_selection, crossover, mutate remain largely the same as before)
# Minor safety checks added previously are kept.

def tournament_selection(population, fitnesses):
  """Selects a parent using tournament selection."""
  actual_tournament_size = min(TOURNAMENT_SIZE, len(population))
  if actual_tournament_size <= 0:
      return population[0] if population else None
  tournament_contenders_indices = random.sample(range(len(population)), actual_tournament_size)
  best_contender_index = -1
  best_fitness = -float('inf')
  for index in tournament_contenders_indices:
    # Check index bounds just in case
    if 0 <= index < len(fitnesses) and fitnesses[index] > best_fitness:
      best_fitness = fitnesses[index]
      best_contender_index = index
  if best_contender_index == -1:
       # Fallback if all fitnesses were -inf or some other issue
      if tournament_contenders_indices: # Ensure list is not empty
        best_contender_index = tournament_contenders_indices[0]
      else: # Extremely unlikely edge case
        return None # Cannot select if no contenders
  # Final check for valid index before returning
  if 0 <= best_contender_index < len(population):
      return population[best_contender_index]
  else: # Fallback if index somehow became invalid
      return population[0] if population else None


def crossover(parent1, parent2):
  """Performs crossover between two parent genomes."""
  # Ensure parents are not None before proceeding
  if parent1 is None or parent2 is None:
      print("Warning: Crossover received None parent(s). Returning copies.")
      return copy.deepcopy(parent1) if parent1 else [], copy.deepcopy(parent2) if parent2 else []

  if random.random() > CROSSOVER_RATE or NUM_SINE_COMPONENTS <= 1:
      return copy.deepcopy(parent1), copy.deepcopy(parent2)

  child1 = []
  child2 = []
  # Ensure crossover point is valid even if NUM_SINE_COMPONENTS is small
  if NUM_SINE_COMPONENTS > 1:
      crossover_point = random.randint(1, NUM_SINE_COMPONENTS - 1)
  else: # Should not happen if check above works, but as safety
      crossover_point = 0 # Effectively no crossover

  # Perform crossover using slicing
  child1.extend(parent1[:crossover_point])
  child1.extend(parent2[crossover_point:])

  child2.extend(parent2[:crossover_point])
  child2.extend(parent1[crossover_point:])

  return child1, child2


def mutate(genome):
  """Applies mutation to a genome."""
  if genome is None: # Handle None genome case
      return None
  mutated_genome = copy.deepcopy(genome)
  for component in mutated_genome:
    for param_type, (min_val, max_val) in PARAM_RANGES.items():
        params_to_mutate = []
        if param_type == 'frequency': params_to_mutate = ['freq_x', 'freq_y']
        elif param_type == 'phase': params_to_mutate = ['phase_x', 'phase_y']
        elif param_type == 'amplitude': params_to_mutate = ['amplitude']

        for p_name in params_to_mutate:
            if p_name in component and random.random() < MUTATION_RATE:
                change = random.uniform(-MUTATION_STRENGTH, MUTATION_STRENGTH) * (max_val - min_val)
                new_value = component[p_name] + change
                component[p_name] = clamp(new_value, min_val, max_val)
  return mutated_genome


# --- Visualization (Matplotlib) ---

def setup_visualization():
    """Initializes the matplotlib figure and axes for animation."""
    fig, ax = plt.subplots()
    # Create an initial empty plot (or plot of zeros)
    initial_grid = np.zeros((GRID_SIZE, GRID_SIZE))
    im = ax.imshow(initial_grid, cmap='viridis', interpolation='nearest', animated=True) # Use animated=True for potential performance boost
    plt.colorbar(im) # Add a colorbar to show value mapping
    ax.set_title("Evolving Pattern (Generation 0)")
    plt.ion() # Turn interactive mode on for non-blocking updates
    fig.canvas.draw() # Initial draw
    plt.show(block=False) # Show non-blocking
    fig.canvas.flush_events() # Ensure the window appears
    return fig, ax, im

def update_visualization(fig, ax, im, genome, generation):
    """Updates the matplotlib plot with the new pattern grid."""
    # Declare global at the beginning of the function scope
    global VISUALIZATION_ENABLED

    if not genome or not VISUALIZATION_ENABLED: # Skip update if no genome or disabled
        return

    try:
        grid = generate_pattern_grid(genome, GRID_SIZE)

        # Update the image data
        im.set_data(grid)

        # Adjust color limits based on the current grid's data range
        min_val, max_val = np.min(grid), np.max(grid)
        # Handle case where min and max are the same (flat color)
        if min_val == max_val:
             min_val -= 0.1 # Add small offset to avoid error
             max_val += 0.1
        im.set_clim(vmin=min_val, vmax=max_val) # Update color limits

        # Update the title
        ax.set_title(f"Evolving Pattern (Generation {generation})")

        # Redraw the figure - use draw_idle for efficiency
        fig.canvas.draw_idle()
        # Process events and pause briefly
        fig.canvas.flush_events() # Crucial for interactive backends
        time.sleep(UPDATE_INTERVAL) # Use time.sleep instead of plt.pause

    except Exception as e:
        # Handle potential errors during plotting (e.g., window closed)
        print(f"\nVisualization error during update: {e}")
        print("Disabling further visualization updates.")
        # Assign to the global variable (already declared global above)
        VISUALIZATION_ENABLED = False # Stop trying to update


# --- Main Evolution Loop ---

def run_evolution():
  """Runs the genetic algorithm and visualization."""
  # Declare global at the beginning of the function scope where it's assigned
  global VISUALIZATION_ENABLED

  # --- Initialization ---
  population = [create_random_genome() for _ in range(POPULATION_SIZE)]
  best_genome_overall = None
  best_fitness_overall = -float('inf')

  # Setup visualization if enabled
  vis_elements = None
  if VISUALIZATION_ENABLED:
      try:
          vis_elements = setup_visualization()
          # Short pause to ensure window is fully up
          if vis_elements: time.sleep(0.1)
      except Exception as e:
          print(f"Error setting up visualization: {e}")
          print("Disabling visualization.")
          # Assign to the global variable (already declared global above)
          VISUALIZATION_ENABLED = False


  print(f"Starting Evolution: Population={POPULATION_SIZE}, Generations={NUM_GENERATIONS}")
  print("-" * 30)

  # --- Evolution Loop ---
  for generation in range(NUM_GENERATIONS):
    start_time = time.time() # Track generation time

    # 1. Evaluate Fitness
    fitnesses = [calculate_fitness(genome) for genome in population]

    # 2. Find Best in Generation and Overall
    current_best_fitness = -float('inf')
    current_best_genome_index = -1
    for i in range(POPULATION_SIZE):
        if fitnesses[i] > current_best_fitness:
            current_best_fitness = fitnesses[i]
            current_best_genome_index = i
        if fitnesses[i] > best_fitness_overall:
            best_fitness_overall = fitnesses[i]
            best_genome_overall = copy.deepcopy(population[i])

    current_best_genome = population[current_best_genome_index] if current_best_genome_index != -1 else None

    gen_time = time.time() - start_time
    print(f"Generation {generation + 1}/{NUM_GENERATIONS} | "
          f"Best Fitness: {current_best_fitness:.4f} | "
          f"Overall Best: {best_fitness_overall:.4f} | "
          f"Time: {gen_time:.2f}s")

    # 3. Update Visualization (if enabled and a best genome exists)
    # Check VISUALIZATION_ENABLED directly (it's global)
    if VISUALIZATION_ENABLED and vis_elements and current_best_genome:
        update_visualization(*vis_elements, current_best_genome, generation + 1)


    # 4. Create Next Generation (Selection, Crossover, Mutation)
    new_population = []
    if current_best_genome: # Elitism
        new_population.append(copy.deepcopy(current_best_genome))

    while len(new_population) < POPULATION_SIZE:
        parent1 = tournament_selection(population, fitnesses)
        parent2 = tournament_selection(population, fitnesses)
        # Skip if selection failed to find valid parents
        if parent1 is None or parent2 is None:
            print("Warning: Skipping reproduction due to selection failure.")
            # Add random individuals if needed to maintain population size
            if len(new_population) < POPULATION_SIZE:
                 new_population.append(create_random_genome())
            continue

        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)

        if len(new_population) < POPULATION_SIZE and child1 is not None:
             new_population.append(child1)
        if len(new_population) < POPULATION_SIZE and child2 is not None:
             new_population.append(child2)

    # Handle cases where mutation/crossover might have returned None
    population = [ind for ind in new_population if ind is not None]
    # If population dipped below target size due to errors, refill (optional)
    while len(population) < POPULATION_SIZE:
        print("Warning: Repopulating due to errors in reproduction.")
        population.append(create_random_genome())


  # --- Post-Evolution ---
  print("-" * 30)
  print("Evolution Finished!")
  print(f"Best Fitness Achieved: {best_fitness_overall:.4f}")
  print("Parameters of the Best Genome:")
  if best_genome_overall:
      for i, component in enumerate(best_genome_overall):
          print(f"  Component {i+1}:")
          for key, value in component.items():
              print(f"    {key}: {value:.4f}")

      # Keep the final plot open if visualization was enabled
      # Check VISUALIZATION_ENABLED directly
      if MATPLOTLIB_AVAILABLE and vis_elements and VISUALIZATION_ENABLED:
          print("\nDisplaying final best pattern. Close the plot window to exit.")
          # Update one last time with the overall best
          fig, ax, im = vis_elements
          # Need to ensure update_visualization doesn't disable it right before this
          if VISUALIZATION_ENABLED: # Check again just in case
              update_visualization(fig, ax, im, best_genome_overall, NUM_GENERATIONS)
              ax.set_title(f"Final Best Pattern (Generation {NUM_GENERATIONS})")
              plt.ioff() # Turn interactive mode off
              plt.show() # Block until window is closed

  else:
      print("No best genome found.")

  return best_genome_overall, best_fitness_overall

# --- Run the Script ---
if __name__ == "__main__":
    # Check for matplotlib availability before running
    if not MATPLOTLIB_AVAILABLE:
        print("\nCannot run visualization without Matplotlib and NumPy.")
        print("Running evolution without visualization...")
        # Optionally run the core logic without plotting
        # best_genome, best_fitness = run_evolution()
    else:
        best_genome, best_fitness = run_evolution()

