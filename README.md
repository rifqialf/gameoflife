# Game of Life

## Description
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively).

Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any **live** cell with fewer than two live neighbours dies, as if by underpopulation.
* Any **live** cell with two or three live neighbours lives on to the next generation.
* Any **live** cell with more than three live neighbours dies, as if by overpopulation.
* Any **dead** cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Implementation
* Our script will thet the input file name, output file name, and the number of generations as arguments
* It will load initial pattern of the grid from the input file.
* It will apply the rules for the number of generations.
* It will store the final grid in to the output file.

## File Format
* Grid will be read from a text
* First line of the text file indicated the width and height of the grup, unsigned integers separated space.
* All other lines will indicate the position of the living cells. Each line will have horizontal and vertical position of a living cell.

 1. The position is based on zero-indexing, i.e. top left cell is 0.0
 2. Horizontal index increases from left to right
 3. Vertical index increases from top to bottom

## Implementation
There are two versions you can use:
* Jupyter Notebook (with explanations and ready-to-run kernels; recommended)
* Python file (description below)

To run the Python version, simply run the Python file from terminal. Examples are shown below.
```Python
# For Dask version
python game_dask.py "bench/1000x1000_0.2.txt" "bench/output.txt" 10 2 2

# For Non-Dask version
python game_nodask.py "bench/1000x1000_0.2.txt" "bench/output.txt" 10

```

