# Where's Waldo?

This project is part of my **CS 211** class and involves working with matrix operations to search for a character named **Waldo** (`W`) in a 2D list (a matrix). The project demonstrates the logic of **universal quantification** and **existential quantification**, applied to both rows and columns of a matrix. This is a fun exercise in matrix traversal and logical operations, inspired by the classic "Where's Waldo?" puzzle.

## Features

- Search for Waldo (`W`) in rows and columns of a matrix.
- Perform checks for both **universal** (all elements) and **existential** (some elements) quantifications.
- Handles edge cases like empty matrices and vacuous truths (e.g., no rows or columns).

## Functions Implemented

Here is a summary of the functions implemented in this project:

1. **all_row_exists_waldo**:  
   Checks if for all rows, there exists at least one Waldo in the row.

2. **all_col_exists_waldo**:  
   Checks if for all columns, there exists at least one Waldo in the column.

3. **all_row_all_waldo**:  
   Checks if for all rows, every column in the row contains Waldo.

4. **all_col_all_waldo**:  
   Checks if for all columns, every row in the column contains Waldo.

5. **exists_row_all_waldo**:  
   Checks if there exists at least one row where every column contains Waldo.

6. **exists_col_all_waldo**:  
   Checks if there exists at least one column where every row contains Waldo.

7. **exists_row_exists_waldo**:  
   Checks if there exists at least one row where there is at least one Waldo.

8. **exists_col_exists_waldo**:  
   Checks if there exists at least one column where there is at least one Waldo.

## Testing

The project includes a set of unit tests to verify that each function works correctly. The test suite is implemented using Python's `unittest` module and can be found in the `tests` directory.
