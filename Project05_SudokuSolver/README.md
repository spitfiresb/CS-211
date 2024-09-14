# Sudoku Solver

This is a Python-based Sudoku solver that can solve a Sudoku puzzle provided via a file. It includes an optional graphical display to visualize the board before and after solving the puzzle.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Format](#file-format)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Description

The Sudoku Solver reads a puzzle from a file, checks its consistency, and solves it using a backtracking algorithm. The solver also provides an optional graphical interface for visualizing the puzzle during and after solving.

## Features

- Solves Sudoku puzzles via a command-line interface.
- Optional graphical display of the puzzle before and after solving.
- Validates puzzle consistency before attempting to solve it.
- Reads the puzzle from a file in a simple format.
  
## Requirements

- Python 3.x
- `argparse` for command-line argument parsing
- `sdk_reader` for reading puzzle input
- `sdk_display` for graphical display (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sudoku-solver.git
   cd sudoku-solver
