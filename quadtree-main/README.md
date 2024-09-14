# Quadtree Image Decoder

## Overview

This project implements a quadtree-based encoding and decoding mechanism for representing and manipulating 8x8 grids of monochrome images. The quadtree representation is particularly useful for efficiently storing and processing images with large uniform regions.

## Features

- **Decode a Quadtree String**: Converts a string representing a quadtree-encoded 8x8 grid into a human-readable grid format.
- **Build a Quadtree**: Constructs a quadtree representation from a given 8x8 grid.
- **Visual Representation**: Provides functionality to visualize the decoded grid using black (`X`) and white (`.`) pixels.

## How It Works

### Quadtree Encoding

- **Symbols**:
  - `B` (Black): Represents a quadrant completely filled with black pixels (`X`).
  - `W` (White): Represents a quadrant completely filled with white pixels (`.`).
  - `G` (Grey): Represents a mixed quadrant that is subdivided into four smaller quadrants.

### Functions

- `fresh_grid()`: Creates an 8x8 grid initialized with an invalid character (`@`).
- `fill_region(grid, row_l, col_l, size, fill_with)`: Fills a specified region of the grid with a given symbol.
- `decode(s)`: Decodes a quadtree-encoded string into an 8x8 grid.
- `str_to_grid(s)`: Converts a string representation of an 8x8 grid into a 2D list.
- `build_quad_tree(grid, row_l, col_l, size)`: Constructs a quadtree representation from an 8x8 grid.

### Classes

- **`QuadTree`**: Base class for quadtree nodes.
- **`Leaf`**: Represents a solid block (black or white) in the quadtree.
- **`GreyNode`**: Represents a mixed quadrant with four child nodes.

## Running the Code

To test the decoding and quadtree-building functionalities, you can directly run the code. Ensure that you have the necessary Python environment set up and execute the script to see the results.

## Acknowledgments

This project was developed as part of a CS 211 course assignment. Special thanks to the course instructor, Michal Young, for their guidance and support.

