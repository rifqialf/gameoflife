import sys
import numpy as np
import time


# Read grid from input file
def read_input(filename):
    with open(filename) as f:
        
        # Read only the first line for the dimension
        w, h = map(int, f.readline().split())
        
        # Read the rest of the input file to build the whole grid
        # Create all 0
        grid = []
        for y in range(h):
            grid.append([0] * w)
        
        # Create all alive cells
        for line in f:
            y, x = map(int, line.split())
            grid[y][x] = 1
        
        # Convert the grid into Numpy array
        grid = np.array(grid)
    return grid


# Create a function that counts alive cells in neighborhood of any arbitraty cell
def countlive(grid, x, y, w, h):
    
    # Generate an array based on relative locations of neighboring cells
    nb = np.array([
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ])
    
    # Count the alive cells
    alive = 0
    for dx, dy in nb:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and grid[ny][nx]==1:
            alive += 1

    return alive


# The rule application in one generation of the game
def tick(grid):
    h = len(grid)
    w = len(grid[0])
    
    newgrid = np.array([[0] * w for _ in range(h)])

    for y in range(h):
        for x in range(w):
            live_nb = countlive(grid, x, y, w, h)

            # Applying Game of Life rules based on the number s of neighboring cells
            if grid[y][x] == 1:
                if live_nb == 2 or live_nb == 3:
                    newgrid[y][x] = 1
            else:
                if live_nb == 3:
                    newgrid[y][x] = 1

    return newgrid


# Determine the dimensions of the grid
def grid_size(inputfile):
    width = len(inputfile[0])
    height = len(inputfile)
    return width, height


# Creating a function to write the resultant grid in output file
def save_output(grid, output):
    with open(output, "w") as f:
        
        # Using grid_dims function to capture grid size info
        w, h = grid_size(grid)
        f.write(f"{w} {h}\n")

        # Writing the grid size info in the output
        # Write the alive cells only
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 1:
                    f.write(f"{y} {x}\n")


# Run the game for specified amount of generation
def tickrun(input, output, generation):
    grid = read_input(input) 
    
    for gen in range(generation):
        grid = tick(grid)
        
    save_output(grid, output)
    return grid

        
def main():
    try:
        input = sys.argv[1]
    except IndexError:
        sys.exit("No input filename.")

    try:
        output = sys.argv[2]
    except IndexError:
        sys.exit("No output filename.")

    try:
        grid = read_input(input)
    except FileNotFoundError:
        sys.exit("Input file not found.")

    try:
        generation = int(sys.argv[3])
    except IndexError:
        sys.exit("No number of generations.")
    except ValueError:
        sys.exit("Invalid number of generations.")
    
    # Start CPU and Wall time measurement
    start_time = time.time()
    start_cpu_time = time.process_time()
        
    # Run the whole process
    tickrun(input, output, generation)
    print("Done")
    
    # Ending the time measurement
    end_time = time.time()
    end_cpu_time = time.process_time()
    
    # Calculating the CPU and wall time
    wall_time = end_time - start_time
    cpu_time = end_cpu_time - start_cpu_time

    print(f"Wall Time: {wall_time} seconds")
    print(f"CPU Time: {cpu_time} seconds")
    print()

if __name__ == "__main__":
    main()