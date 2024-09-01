# RREF Determinant Calculator
A project that calculates a matrix's Row Reduced Echelon Form and Determinants

# Description
- RREF algorithm: The algorithm I came up with myself, though it doesn't feel like I invented anything new, but rather rediscovered it. The way this RREF algorithm works is that there is a loop that goes from through the columns of the matrix from left to right. It starts with the first column and looks for a row that has a pivot, if it isn't already in the right staircase spot (the staircase of 1's that can be seen when row reducing), that pivot row switches with the row that is in the staircase spot. From there we take the number in the pivot/stair, in the column that we're at, and divide the whole row by that number. From there, we have our first 1 within the staircase of 1's. after that we take the numbers in the rows that aren't the pivot/stair row (call these numbers n), and subtract each row in this way: Current_row becomes-> Current_row - n * Pivot_Row. This will zero out everything under and over the stair. This is basically the whole process for row reducing. We do this for every column from left to right. The last part to talk about is if the column isn't a pivot column. The solution to that is to simply add 1 to the variable that is storing which column we're currently on.
  
- Determinant algorithm: This algorithm uses the RREF algorithm to multiply the starting determinant of 1 by what the rows get divided by. So if a pivot row gets divided by n then the determinant becomes 1*n. Additionally, if two rows are switched which each other, then the determinant switches signs. For example, n becomes -n. Lastly, if at any point the else statement that sees there are no pivots is run, it makes the determinant 0 as a matrix that is linearly dependent (doesn't have a pivot is all columns), has a determinant of 0
  
- Linear Dependency: It is initialized as LinearlyIndependent = True, but if the else statement that sees there are no pivots is run, it makes linearlyIndependant = False.
- 
# Future Updates / Roadmap
- Inverse matrix
- Show the output on the GUI rather than just printing it
- basis shifts
- Calculate Lamdas
- Calculate D matrix
- Add this project to a massive math calculator project (including calc 1 & 2, algebra, geometry, and more)

# Built With
Built using Python and the Tkinter library.
