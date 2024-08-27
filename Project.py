import tkinter as tk
import tkinter.font as tkFont


class MyGUI

    #constructor
    def __init__(self):

        
        #window creation
        self.root = tk.Tk()

        self.root.geometry("1024x680") #set the height and width of window

        self.root.title("Row Reduction Echelon form calculator") #Window Title

        #Fonts
        self.titlefont = ("arial", 18) 
        self.prompt = ("arial", 15) 
        self.UserInput = ("arial", 14) 
        self.buttonfont = ("arial", 12)

        #Frame for Title and first prompt
        self.title_frame = tk.Frame(self.root)
        self.title_frame.pack(anchor='n', pady=10)

        #Frame for matrix and second prompt
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(anchor='n')

        #Frame for the output
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(anchor='n')


        self.title = tk.Label(self.title_frame, text = "Row Reduction Echelon form calculator", font = self.titlefont)
        self.title.pack(anchor='n', pady=10) #anchors the label to the northern part of the window

        self.RowColumnPrompt = tk.Label(self.title_frame, text = "Matrix dimensions:", font = self.prompt) 
        self.RowColumnPrompt.pack(side ='left', anchor = 'n',pady=10, padx=10)

        self.entryBoxRows = tk.Entry(self.title_frame, font = self.UserInput, width = 3)
        self.entryBoxRows.pack(side = 'left', anchor = 'n', pady=13)

        self.xlabel = tk.Label(self.title_frame, text = "X", font = self.prompt) #the x in rows X columns
        self.xlabel.pack(side ='left', anchor = 'n',pady=12)

        self.entryBoxColumns = tk.Entry(self.title_frame, font = self.UserInput, width = 3)
        self.entryBoxColumns.pack(side = 'left', anchor = 'n', pady=12)

        self.LoadDimensionsButton = tk.Button(self.title_frame, font = self.buttonfont, width = 16, text = "Load Dimensions\nand Clear", command=self.generate_matrix_dimensions)
        self.LoadDimensionsButton.pack(side = 'left', anchor = 'n', pady=4, padx = 5)

        self.Calculate = tk.Button(self.title_frame, font = self.buttonfont, width = 8, text = "Calculate", command=self.reduce_matrix)
        self.Calculate.pack(side = 'left', anchor = 'n', pady=4, padx = 5)
        
        #Matrix frame for the input matrix
        self.matrix_frame = tk.Frame(self.input_frame, height = 15, width = 150)
        self.matrix_frame.pack(pady=10)
        
        



        
        self.root.mainloop()

        #reduce_matrix is a jumble of things. It reduces the matrix into RREF, gets the determinant, sees if it's lin dep. or not,
        #and calcualtes the inverse
        #the main part is reduce_matrix, with other lines added in through there to keep track of Det, Lin dependancy, and inverse.
    def reduce_matrix(self):
         matrix = self.grabMatrixData()
         #printing function
         self.printMatrix(matrix)
         stair = 0 #variable that tracks how many pivots have been placed
         pivot=-1 #variable that searchs for possible pivot elements
         columnTraverse = 0
         detCoef = 1 #determinant coefficient
         linearlyIndependant = True


         #since columnTraverse starts at 0, it'll go all the way to cols-1, which also is the last element of the list
         while columnTraverse != self.cols: #while the traversing of the columns hasn't reached the end of the matrix from left to right
            
             pivot = self.pivotSpot(matrix, columnTraverse, stair)
             if pivot == stair:
                 divisionNum = matrix[pivot][columnTraverse]
                 for c in range(self.cols):
                    #Divide the row. Rn->1/divisionNum*Rn
                     matrix[pivot][c] /= divisionNum
                     
                     self.cleanup_matrix(matrix)
                 detCoef *= divisionNum #for determinant calculation

                 print("middle:")
                 self.printMatrix(matrix)
                     
                 
                 for row in range(self.rows):
                     if row == pivot: continue #avoid zeroing out the pivot element
                     scaler = matrix[row][columnTraverse]
                     #subtract Rn-> Rn-CRp   p implying pivot
                     for c in range(self.cols):
                         matrix[row][c] -= scaler*matrix[pivot][c]

                         self.cleanup_matrix(matrix)

                 print("nearend:")
                 self.printMatrix(matrix)
                 
                 stair += 1
                 columnTraverse += 1
             #switch rows.
             elif pivot != -1:
                #Rs <-> Rp, but stair value stays the same, so really after this Rp is the one that should be named Rs
                for c in range(self.cols):
                    matrix[stair][c], matrix[pivot][c] = matrix[pivot][c], matrix[stair][c]

                detCoef = -detCoef #when switches rows, the sign of the coeffiecient switches
             else:
                 columnTraverse += 1
                 linearlyIndependant = False
                 detCoef = 0 #if a matrix in linearly dependent then the determinant is 0
                 
         
         print("final:")
         
         
         self.printMatrix(matrix)

         if detCoef != 0:
            detCoef = self.calculateDeterminant(matrix, detCoef)
         print("determinant is", detCoef)

         #linear dependency
         if linearlyIndependant == True:
            print("The matrix is linearly independent")
         else:
            print("The matrix is linearly dependent")


    def calculateDeterminant(self, matrix, detCoef):
        matDetCoef = 1
        for r in range(self.rows - 1):
            for c in range(r, self.cols):
                if matrix[r][c] != 0:
                    print(matrix[r][c])
                    matDetCoef *= matrix[r][c]


        return detCoef*matDetCoef
         
    #figures out if a column has a pivot element. If it does, return the row that element is in.
    #if it doesn't contain a pivot, return -1 to indicate a column with free variables.
    def pivotSpot(self, matrix, column, stair):
       
       #skip past rows that already have a pivot in them(that's what the stair is for)
        for row in range(stair, self.rows):
            if matrix[row][column]: #if the element isn't a 0 then run
                return row
            
        return -1

    #for some reason some zeros end up as -0.0 which got me confused
    def cleanup_matrix(self, matrix):
        for r in range(self.rows):
            for c in range(self.cols):
                if matrix[r][c] == -0.0:
                    matrix[r][c] = 0.0

    #gets the number of rows and columns
    def RowsColsInput(self) -> tuple[int,int]:
        
        try:
            rows = int(self.entryBoxRows.get())
            cols = int(self.entryBoxColumns.get())
        except ValueError:
            return # basically clear the matrix if non numerical value is inputed
        
        return rows, cols

    #grabs the elements from user input
    def grabMatrixData(self) -> list:
         #get dimensions

         matrix = []
         for row_entries in self.matrix_entries:
            matRow = []
            for entry in row_entries:
                value = entry.get()
                try:
                    #convert the value to float before appending
                    float_value = float(value)
                except ValueError:
                    #handle cases where empty or non numberic strings are inputed
                    float_value = 0
                matRow.append(float_value)
            matrix.append(matRow)
        
        

         return matrix

    #prints matrix in console. used before I implement printing it onto the User Interface
    def printMatrix(self, matrix) -> None:
        for row in matrix:
            print(row)
    
    #generates the input matrix
    def generate_matrix_dimensions(self):
        #clears the previous matrix if it exists
        for elements in self.matrix_frame.winfo_children():
            elements.destroy()

        #call function that gets the rows and columns
        self.rows, self.cols = self.RowsColsInput()

        self.matrix_font = ('Arial', 12)
        
        #Creation of the matrix using the grid
        self.matrix_entries = []
        for r in range(self.rows):
            row_entries = []
            for c in range(self.cols):
                entry = tk.Entry(self.matrix_frame, width = 4, font = self.matrix_font)
                entry.grid(row = r, column=c, padx=5,pady=5)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)















        

MyGUI()
