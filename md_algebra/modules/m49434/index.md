Solving Systems with Gaussian Elimination

  m49434
  Solving Systems with Gaussian Elimination
  In this section, you will:
Write the augmented matrix of a system of equations.
Write the system of equations from an augmented matrix.
Perform row operations on a matrix.
Solve a system of linear equations using matrices.

  69e0b9a7-0928-46a6-bb59-6cd28f18eec9

Learning Objectives
Use row operations on a matrix (IA 4.5.2)
Solve systems of equations using matrices (IA 4.5.3)

Objective 1: Use row operations on a matrix (IA 4.5.2)In the last section, we learned how to write the augmented matrix for a system of equations.
Once a system of equations is in its augmented matrix form, we will solve by elimination by performing operations on the rows that will lead us to the solution. Our goal will be to get 1 on the diagonal of the matrix and all entries below the diagonal must be zeros.

Row Operations
In a matrix, the following operations can be performed on any row and the resulting matrix will be equivalent to the original matrix.
Interchange any two rows.
Multiply a row by any real number except 0.
Add a nonzero multiple of one row to another row.
These actions are called row operations and will help us use the matrix to solve a system of equations.

  
 Use the indicated row operations on the augmented matrix:
  

  
    ⓐ Interchange rows 2 and 3.
ⓑ
 Multiply row 2 by 5.

ⓒ Multiply row 3 by −2 and add to row 1.

 [6-5211-43-31|35-1] 

  
    ⓐ Interchange rows 2 and 3.

     
    
  
  
  
    ⓑ Multiply row 2 by 5.
    
    
  
  
  
    ⓒ Multiply row 3 by −2 and  add to row 1.

    
    
  
  

Use the indicated row operations on the augmented matrix:

  
    ⓐ Interchange rows 1 and 3.

ⓑ Multiply row 3 by 3.

ⓒ Multiply row 3 by 2 and add to row 2.

 5-2-2-24-1-44-230-1 

Use the needed row operation that will get the first entry in row 2 to be zero in the augmented matrix:  [1−14−8|20]. 

To make the 4 a 0, we could multiply row 1 by −4 and then add it to row 2.

Practice Makes Perfect
Use the needed row operation that will get the first entry in row 2 to be zero in the augmented matrix

 1-123-62
Objective 2: Solve systems of equations using matrices (IA 4.5.3)To solve a system of equations using matrices, we transform the augmented matrix into a matrix in row-echelon form using row operations. For a consistent and independent system of equations, the augmented matrix is in row-echelon form when to the left of the vertical line, each entry on the diagonal is a 1 and all entries below the diagonal are zeros.

    
  

Once we get the augmented matrix into row-echelon form, we can write the equivalent system of equations and solve for at least one variable. We then substitute this value in another equation to continue to solve for the other variables.
Solving a system of equations using matrices.Write the augmented matrix for the system of equations.
Using row operations get the entry in row 1, column 1 to be 1.
Using row operations, get zeros in column 1 below the 1.
Using row operations, get the entry in row 2, column 2 to be 1.
Continue the process until the matrix is in row-echelon form.
Write the corresponding system of equations.
Use substitution to find the remaining variables.
Write the solution as an ordered pair or triple.
Check that the solution makes the original equations true.

Solve the system of equations using matrices

 {3x+8y+2z=−52x+5y−3z=0x+2y−2z=−1 

Write the augmented matrix for the system of equations.

Interchange row 1 and row 3 to get a 1 in the first row and first column.

Using row operations, get zeros in column 1 below the 1

The entry in row 2, column 2 is now 1.

Continue the process until the matrixis in row-echelon form.

The matrix is now in row-echelon form.

Write the corresponding system of equations.

Use substitution to find the remaining variables.

Write the solution as an ordered pair or triple.

Check that the solution makes the original equations true.

Practice Makes Perfect
Solve the system of equations using matrices

 x-y-z=1-x+2y-3z=-43x-2y-7z=0

German mathematician Carl Friedrich Gauss (1777–1855).Carl Friedrich Gauss lived during the late 18th century and early 19th century, but he is still considered one of the most prolific mathematicians in history. His contributions to the science of mathematics and physics span fields such as algebra, number theory, analysis, differential geometry, astronomy, and optics, among others. His discoveries regarding matrix theory changed the way mathematicians have worked for the last two centuries.

 We first encountered Gaussian elimination in Systems of Linear Equations: Two Variables. In this section, we will revisit this technique for solving systems, this time using matrices.
Writing the Augmented Matrix of a System of Equations
A matrix can serve as a device for representing and solving a system of equations. To express a system in matrix form, we extract the coefficients of the variables and the constants, and these become the entries of the matrix. We use a vertical line to separate the coefficient entries from the constants, essentially replacing the equal signs. When a system is written in this form, we call it an augmented matrix.
For example, consider the following 
 
  2×2
 
 system of equations. 
 
  
   
    3x+4y=7
   
  
  
   
    4x−2y=5
   
  
 

 
We can write this system as an augmented matrix:
   
 
  [ 
   
    
     
      3
     
     
      4
     
    
    
     
      4
     
     
      
       −2
      
     
    

    |
     
     
      
       7
      
     
     
      
       5
      
     

    
   
   ]
 

We can also write a matrix containing just the coefficients. This is called the coefficient matrix.
 
 
  [ 
   
    
     
      3
     
     
      4
     
    
    
     
      4
     
     
      
       −2
      
     
    

   
   ]
 
 
A three-by-three system of equations such as
   
 
  
   
    
     
      3x−y−z=0
     
    
   
   
    
     
             x+y=5
     
    
   
   
    
     
           2x−3z=2
     
    
   

  
 

has a coefficient matrix
 
 
  [ 
   
    
     
      3
     
     
      
       −1
      
     
     
      
       −1
      
     
    
    
     
      1
     
     
      1
     
     
      0
     
    
    
     
      2
     
     
      0
     
     
      
       −3
      
     
    

   
   ]
 

and is represented by the augmented matrix
  	 
 
  [ 
   
    
     
      3
     
     
      
       −1
      
     
     
      
       −1
      
     
    
    
     
      1
     
     
      1
     
     
      0
     
    
    
     
      2
     
     
      0
     
     
      
       −3
      
     
    

    |
     
     
      
       0
      
     
     
      
       5
      
     
     
      
       2
      
     

    
   
   ]
 

Notice that the matrix is written so that the variables line up in their own columns: x-terms go in the first column, y-terms in the second column, and z-terms in the third column. It is very important that each equation is written in standard form 
 
  ax+by+cz=d
 
 so that the variables line up. When there is a missing variable term in an equation, the coefficient is 0.How To
Given a system of equations, write an augmented matrix.
Write the coefficients of the x-terms as the numbers down the first column.
Write the coefficients of the y-terms as the numbers down the second column.
If there are z-terms, write the coefficients as the numbers down the third column.
Draw a vertical line and write the constants to the right of the line.

Writing the Augmented Matrix for a System of Equations
Write the augmented matrix for the given system of equations.
   
 
  
   
    
     
        x+2y−z=3
     
    
   
   
    
     
      2x−y+2z=6
     
    
   
   
    
     
       x−3y+3z=4
     
    
   

  
 

The augmented matrix displays the coefficients of the variables, and an additional column for the constants.
   
 
  [ 
   
    
     
      1
     
     
      2
     
     
      
       −1
      
     
    
    
     
      2
     
     
      
       −1
      
     
     
      2
     
    
    
     
      1
     
     
      
       −3
      
     
     
      3
     
    

    |
     
     
      
       3
      
     
     
      
       6
      
     
     
      
       4
      
     

    
   
   ]
 

Try It

Write the augmented matrix of the given system of equations.
     
 
  
   
    4x−3y=11
   
  
  
   
    3x+2y=4
   
  
 

 

 
  [ 
   
    
     
      4
     
     
      
       −3
      
     
    
    
     
      3
     
     
      
       2
      
     
    

   |
    
     
      
       
        11
       
      
     
     
      
       
        4
       
      
     

    
   
   ]
 

Writing a System of Equations from an Augmented Matrix
We can use augmented matrices to help us solve systems of equations because they simplify operations when the systems are not encumbered by the variables. However, it is important to understand how to move back and forth between formats in order to make finding solutions smoother and more intuitive. Here, we will use the information in an augmented matrix to write the system of equations in standard form.

Writing a System of Equations from an Augmented Matrix Form
Find the system of equations from the augmented matrix.
   
 
  [ 
   
    
     
      1
     
     
      
       −3
      
     
     
      
       −5
      
     
    
    
     
      2
     
     
      
       −5
      
     
     
      
       −4
      
     
    
    
     
      
       −3
      
     
     
      5
     
     
      4
     
    

    |
     
     
      
       
        −2
       
      
     
     
      
       5
      
     
     
      
       6
      
     

    
   
   ]
 

When the columns represent the variables 
 
  x,
 
 
 
  y,
 
 and 
 
  z,
 
 
 
 
  [ 
   
    
     
      1
     
     
      
       −3
      
     
     
      
       −5
      
     
    
    
     
      2
     
     
      
       −5
      
     
     
      
       −4
      
     
    
    
     
      
       −3
      
     
     
      5
     
     
      4
     
    

    |
     
     
      
       
        −2
       
      
     
     
      
       5
      
     
     
      
       6
      
     

    
   
   ]→
   
    
     
      x−3y−5z=−2
     
    
   
   
    
     
      2x−5y−4z=5
     
    
   
   
    
     
      −3x+5y+4z=6
     
    
   

  
 

Try It

Write the system of equations from the augmented matrix.
 
 
  [ 
   
    
     
      1
     
     
      
       −1
      
     
     
      
       1
      
     
    
    
     
      2
     
     
      
       −1
      
     
     
      
       3
      
     
    
    
     
      0
     
     
      
       1
      
     
     
      
       1
      
     
    

   |
    
     
      
       
        5
       
      
     
     
      
       
        1
       
      
     
     
      
       
        −9
       
      
     

    
   
   ]
 
 

 
  
   
    x−y+z=5
   
  
  
   
    2x−y+3z=1
   
  
  
   
    y+z=−9
   
  
 

 

Performing Row Operations on a Matrix
Now that we can write systems of equations in augmented matrix form, we will examine the various row operations that can be performed on a matrix, such as addition, multiplication by a constant, and interchanging rows.
Performing row operations on a matrix is the method we use for solving a system of equations. In order to solve the system of equations, we want to convert the matrix to row-echelon form, in which there are ones down the main diagonal from the upper left corner to the lower right corner, and zeros in every position below the main diagonal as shown.
 
 
  
   
    
     
      Row-echelon form
     
    
   
   
    
     
      [ 
       
        
         
          1
         
         
          a
         
         
          b
         
        
        
         
          0
         
         
          1
         
         
          d
         
        
        
         
          0
         
         
          0
         
         
          1
         
        

       
       ]
     
    
   

  
 

We use row operations corresponding to equation operations to obtain a new matrix that is row-equivalent in a simpler form. Here are the guidelines to obtaining row-echelon form.

In any nonzero row, the first nonzero number is a 1. It is called a leading 1.
Any all-zero rows are placed at the bottom on the matrix.
Any leading 1 is below and to the right of a previous leading 1.
Any column containing a leading 1 has zeros in all other positions in the column.

To solve a system of equations we can perform the following row operations to convert the coefficient matrix to row-echelon form and do back-substitution to find the solution.Interchange rows. (Notation: 
 
  
   R
   i
  
  ↔
   R
   j
  

 
 )
Multiply a row by a constant. (Notation: 
 
  c
   R
   i
  

 
 )
Add the product of a row multiplied by a constant to another row. (Notation: 
 
  
   R
   i
  
  +c
   R
   j
  
  )
 
 
Each of the row operations corresponds to the operations we have already learned to solve systems of equations in three variables. With these operations, there are some key moves that will quickly achieve the goal of writing a matrix in row-echelon form. To obtain a matrix in row-echelon form for finding solutions, we use Gaussian elimination, a method that uses row operations to obtain a 1 as the first entry so that row 1 can be used to convert the remaining rows.

Gaussian Elimination
The Gaussian elimination method refers to a strategy used to obtain the row-echelon form of a matrix. The goal is to write matrix 
 
  A
 
 with the number 1 as the entry down the main diagonal and have all zeros below.
   
 
  A=[ 
   
    
     
      
       
        a
        
         11
        
       

      
     
     
      
       
        a
        
         12
        
       

      
     
     
      
       
        a
        
         13
        
       

      
     
    
    
     
      
       
        a
        
         21
        
       

      
     
     
      
       
        a
        
         22
        
       

      
     
     
      
       
        a
        
         23
        
       

      
     
    
    
     
      
       
        a
        
         31
        
       

      
     
     
      
       
        a
        
         32
        
       

      
     
     
      
       
        a
        
         33
        
       

      
     
    

   
   ]
   →
   
    After Gaussian elimination
   
  
  A=[ 
   
    
     
      1
     
     
      
       
        b
        
         12
        
       

      
     
     
      
       
        b
        
         13
        
       

      
     
    
    
     
      0
     
     
      
       1
      
     
     
      
       
        b
        
         23
        
       

      
     
    
    
     
      0
     
     
      
       0
      
     
     
      
       1
      
     
    

   
   ]
 

The first step of the Gaussian strategy includes obtaining a 1 as the first entry, so that row 1 may be used to alter the rows below.

How To
Given an augmented matrix, perform row operations to achieve row-echelon form.

The first equation should have a leading coefficient of 1. Interchange rows or multiply by a constant, if necessary.
Use row operations to obtain zeros down the first column below the first entry of 1.
Use row operations to obtain a 1 in row 2, column 2.
Use row operations to obtain zeros down column 2, below the entry of 1.
Use row operations to obtain a 1 in row 3, column 3.
Continue this process for all rows until there is a 1 in every entry down the main diagonal and there are only zeros below.
If any rows contain all zeros, place them at the bottom.

Solving a 
 
  2×2
 
 System by Gaussian Elimination
Solve the given system by Gaussian elimination.
 
 
  
   
    
     
      2x+3y=6
     
    
   
   
    
     
         x−y=
       1
       2
      

     
    
   

  
 

First, we write this as an augmented matrix.
   
 
  [ 
   
    
     
      2
     
     
      3
     
    
    
     
      1
     
     
      
       −1
      
     
    

    |
     
     
      
       6
      
     
     
      
       
        
         1
         2
        

       
      
     

    
   
   ]
 

We want a 1 in row 1, column 1. This can be accomplished by interchanging row 1 and row 2.
   
 
  
   R
   1
  
  ↔
   R
   2
  
  →[ 
   
    
     
      1
     
     
      
       −1
      
     
     
      
     
    
    
     
      2
     
     
      3
     
     
      
     
    

   |
    
     
      
       
      
      
       
        
         1
         2
        

       
      
     
     
      
       
      
      
       6
      
     

    
   
   ]
 

We now have a 1 as the first entry in row 1, column 1. Now let’s obtain a 0 in row 2, column 1. This can be accomplished by multiplying row 1 by 
 
  −2,
 
 and then adding the result to row 2. 
 
  −2
   R
   1
  
  +
   R
   2
  
  =
   R
   2
  
  →[ 
   
    
     
      1
     
     
      
       −1
      
     
     
      
     
    
    
     
      0
     
     
      5
     
     
      
     
    

   |
    
     
      
       
      
      
       
        
         1
         2
        

       
      
     
     
      
       
      
      
       5
      
     

    
   
   ]
 

We only have one more step, to multiply row 2 by 
 
  
   1
   5
  
  .
 
 
   
 
  
   1
   5
  
  
   R
   2
  
  =
   R
   2
  
  →[ 
   
    
     
      1
     
     
      
       −1
      
     
     
      
     
    
    
     
      0
     
     
      1
     
     
      
     
    

   |
    
     
      
       
      
      
       
        
         1
         2
        

       
      
     
     
      
       
      
      
       1
      
     

    
   
   ]
 

Use back-substitution. The second row of the matrix represents 
 
  y=1.
 
 Back-substitute 
 
  y=1
 
 into the first equation.
   
 
  
   
    
     
      x−(1)=
       1
       2
      

     
    
   
   
    
     
              x=
       3
       2
      

     
    
   

  
 

The solution is the point 
 
  (
   
    
     3
     2
    
    ,1
   
  ).
 
 

Try It

Solve the given system by Gaussian elimination.
   
 
  
   
    
     
      4x+3y=11
     
    
   
   
    
     
       x−3y=−1
     
    
   

  
 

 
 
  (
   
    2,1
   
  )
 
 

Using Gaussian Elimination to Solve a System of Equations
Use Gaussian elimination to solve the given 
 
  2×2
 

system of equations.
   
 
  
   
    
     
       2x+y=1
     
    
   
   
    
     
      4x+2y=6
     
    
   

  
 

Write the system as an augmented matrix.
   
 
  [ 
   
    
     
      2
     
     
      1
     
    
    
     
      4
     
     
      2
     
    

    |
     
     
      
       1
      
     
     
      
       6
      
     

    
   
   ]
 

Obtain a 1 in row 1, column 1. This can be accomplished by multiplying the first row by 
 
  
   1
   2
  
  .
 
 
   
 
  
   1
   2
  
  
   R
   1
  
  =
   R
   1
  
  →[ 
   
    
     
      1
     
     
      
       
        1
        2
       

      
     
    
    
     
      4
     
     
      2
     
    

    |
     
     
      
       
        
         1
         2
        

       
      
     
     
      
       6
      
     

    
   
   ]
 

Next, we want a 0 in row 2, column 1. Multiply row 1 by 
 
  −4
 
 and add row 1 to row 2. 
 
  −4
   R
   1
  
  +
   R
   2
  
  =
   R
   2
  
  →[ 
   
    
     
      1
     
     
      
       
        1
        2
       

      
     
    
    
     
      0
     
     
      0
     
    

    |
     
     
      
       
        
         1
         2
        

       
      
     
     
      
       4
      
     

    
   
   ]
 

The second row represents the equation 
 
  0=4.
 
 Therefore, the system is inconsistent and has no solution.

Solving a Dependent System
Solve the system of equations.
   
 
  
   
    3x+4y=12
   
  
  
   
    6x+8y=24
   
  
 

 

Perform row operations on the augmented matrix to try and achieve row-echelon form. 
 
  A=[ 
   
    
     
      
       3
      
      
       
      
      
       4
      
      
       
      
     
     
      
       6
      
      
       
      
      
       8
      
      
       
      
     

    
   |
    
     
      
     
     
      
       12
      
     
    
    
     
      
     
     
      
       24
      
     
    

   
   ]
 

 
 
  
   
    
     
    
   
   
    
     
      
       
        
         
          −
           1
           2
          
          
           R
           2
          
          +
           R
           1
          
          =
           R
           1
          
          →[ 
           
            
             
              
               0
              
              
               
              
              
               0
              
              
               
              
             
             
              
               6
              
              
               
              
              
               8
              
              
               
              
             

            
           |
            
             
              
             
             
              
               0
              
             
            
            
             
              
             
             
              
               24
              
             
            

           
           ]
         
        
       
       
        
         
          
           R
           1
          
          ↔
           R
           2
          
          →[ 
           
            
             
              
               6
              
              
               
              
              
               8
              
              
               
              
             
             
              
               0
              
              
               
              
              
               0
              
              
               
              
             

            
           |
            
             
              
             
             
              
               24
              
             
            
            
             
              
             
             
              
               0
              
             
            

           
           ]
         
        
       

      
     
    
   

  
 

The matrix ends up with all zeros in the last row: 
 
  0y=0.
 
 Thus, there are an infinite number of solutions and the system is classified as dependent. To find the generic solution, return to one of the original equations and solve for 
 
  y.
 
 
   
 
  
   
    
     
      3x+4y=12
     
    
   
   
    
     
              4y=12−3x
     
    
   
   
    
     
                y=3−
       3
       4
      
      x
     
    
   

  
 

So the solution to this system is 
 
  (
   
    x,3−
     3
     4
    
    x
   
  ).
 
 

Performing Row Operations on a 3×3 Augmented Matrix to Obtain Row-Echelon Form
Perform row operations on the given matrix to obtain row-echelon form.
   
 
  [ 
   
    
     
      1
     
     
      
       −3
      
     
     
      4
     
    
    
     
      2
     
     
      
       −5
      
     
     
      6
     
    
    
     
      
       −3
      
     
     
      3
     
     
      4
     
    

    |
     
     
      
       3
      
     
     
      
       6
      
     
     
      
       6
      
     

    
   
   ]
 

The first row already has a 1 in row 1, column 1. The next step is to multiply row 1 by 
 
  −2
 
 and add it to row 2. Then replace row 2 with the result.
   
 
  −2
   R
   1
  
  +
   R
   2
  
  =
   R
   2
  
  →[ 
   
    
     
      1
     
     
      
     
     
      
       −3
      
     
     
      
     
     
      4
     
     
      
     
    
    
     
      0
     
     
      
     
     
      1
     
     
      
     
     
      
       −2
      
     
     
      
     
    
    
     
      
       −3
      
     
     
      
     
     
      3
     
     
      
     
     
      4
     
     
      
     
    

   |
    
     
      
       
      
      
       3
      
     
     
      
       
      
      
       0
      
     
     
      
       
      
      
       6
      
     

    
   
   ]
 

Next, obtain a zero in row 3, column 1.
   
 
  3
   R
   1
  
  +
   R
   3
  
  =
   R
   3
  
  →[ 
   
    
     
      1
     
     
      
     
     
      
       −3
      
     
     
      
     
     
      4
     
     
      
     
    
    
     
      0
     
     
      
     
     
      1
     
     
      
     
     
      
       −2
      
     
     
      
     
    
    
     
      0
     
     
      
     
     
      
       −6
      
     
     
      
     
     
      
       16
      
     
     
      
     
    

   |
    
     
      
       
      
      
       3
      
     
     
      
       
      
      
       0
      
     
     
      
       
      
      
       
        15
       
      
     

    
   
   ]
 

Next, obtain a zero in row 3, column 2.
   
 
  6
   R
   2
  
  +
   R
   3
  
  =
   R
   3
  
  →[ 
   
    
     
      1
     
     
      
     
     
      
       −3
      
     
     
      
     
     
      4
     
     
      
     
    
    
     
      0
     
     
      
     
     
      1
     
     
      
     
     
      
       −2
      
     
     
      
     
    
    
     
      0
     
     
      
     
     
      0
     
     
      
     
     
      4
     
     
      
     
    

   |
    
     
      
       
      
      
       3
      
     
     
      
       
      
      
       0
      
     
     
      
       
      
      
       
        15
       
      
     

    
   
   ]
 

The last step is to obtain a 1 in row 3, column 3.
   
 
  
   1
   4
  
  
   R
   3
  
  =
   R
   3
  
  →[ 
   
    
     
      1
     
     
      
       −3
      
     
     
      4
     
    
    
     
      0
     
     
      1
     
     
      
       −2
      
     
    
    
     
      0
     
     
      0
     
     
      1
     
    

    |
     
     
      
       3
      
     
     
      
       
        0
       
      
     
     
      
       
        
         
          15
         
         4
        

       
      
     

    
   
   ]
 

Try It

Write the system of equations in row-echelon form.
   
 
  
   
    
     
       x−2y+3z=9
     
    
   
   
    
     
      −x+3y=−4
     
    
   
   
    
     
      2x−5y+5z=17
     
    
   

  
 

 
  [ 
   
    
     
      
       
        1
       
      
      
       
        −
         5
         2
        

       
      
      
       
        
         5
         2
        

       
      
     
     
      
       
        ​0
       
      
      
       
        1
       
      
      
       5
      
     
     
      
       
        0
       
      
      
       
        0
       
      
      
       
        1
       
      
     

    
   |
    
     
      
       
        
         17
        
        2
       

      
     
    
    
     
      9
     
    
    
     
      2
     
    

   
   ]
 
 

Solving a System of Linear Equations Using Matrices
We have seen how to write a system of equations with an augmented matrix, and then how to use row operations and back-substitution to obtain row-echelon form. Now, we will take row-echelon form a step farther to solve a 3 by 3 system of linear equations. The general idea is to eliminate all but one variable using row operations and then back-substitute to solve for the other variables.

Solving a System of Linear Equations Using Matrices
Solve the system of linear equations using matrices.
   
 
  
   
    
     
      
       
        
         
        
       
       
        
         
        
       
       
        
         
          x−y+z=8
         
        
       

      
     
    
   
   
    
     
      2x+3y−z=−2
     
    
   
   
    
     
      3x−2y−9z=9
     
    
   

  
 

First, we write the augmented matrix.
   
 
  [ 
   
    
     
      1
     
     
      
       −1
      
     
     
      1
     
    
    
     
      2
     
     
      3
     
     
      
       −1
      
     
    
    
     
      3
     
     
      
       −2
      
     
     
      
       −9
      
     
    

     |
     
     
      
       8
      
     
     
      
       
        −2
       
      
     
     
      
       9
      
     

    
   
   ]
 

Next, we perform row operations to obtain row-echelon form.
   
 
  
   
    
     
      −2
       R
       1
      
      +
       R
       2
      
      =
       R
       2
      
      →[ 
       
        
         
          1
         
         
          
         
         
          
           −1
          
         
         
          
         
         
          1
         
         
          
         
        
        
         
          0
         
         
          
         
         
          5
         
         
          
         
         
          
           −3
          
         
         
          
         
        
        
         
          3
         
         
          
         
         
          
           −2
          
         
         
          
         
         
          
           −9
          
         
         
          
         
        

       |
        
         
          
           
          
          
           8
          
         
         
          
           
          
          
           
            −18
           
          
         
         
          
           
          
          
           9
          
         

        
       
       ]
     
    
    
     
    
    
     
    
    
     
    
    
     
      −3
       R
       1
      
      +
       R
       3
      
      =
       R
       3
      
      →[ 
       
        
         
          1
         
         
          
         
         
          
           −1
          
         
         
          
         
         
          1
         
         
          
         
        
        
         
          0
         
         
          
         
         
          5
         
         
          
         
         
          
           −3
          
         
         
          
         
        
        
         
          0
         
         
          
         
         
          1
         
         
          
         
         
          
           −12
          
         
         
          
         
        

       |
        
         
          
           
          
          
           8
          
         
         
          
           
          
          
           
            −18
           
          
         
         
          
           
          
          
           
            −15
           
          
         

        
       
       ]
     
    
   

  
 

The easiest way to obtain a 1 in row 2 of column 1 is to interchange 
 
  
   R
   2
  

 
 and 
 
  
   R
   3
  
  .
 
 
   
 
  Interchange
   R
   2
  
  and
   R
   3
  
  →[ 
   
    
     
      1
     
     
      
     
     
      
       −1
      
     
     
      
     
     
      1
     
     
      
     
     
      8
     
    
    
     
      0
     
     
      
     
     
      1
     
     
      
     
     
      
       −12
      
     
     
      
     
     
      
       −15
      
     
    
    
     
      0
     
     
      
     
     
      5
     
     
      
     
     
      
       −3
      
     
     
      
     
     
      
       −18
      
     
    

   
   ]
 

Then
   
 
  
   
    
   
  
  
   
    
     
      
       
        −5
         R
         2
        
        +
         R
         3
        
        =
         R
         3
        
        →[ 
         
          
           
            
             1
            
            
             
            
            
             
              −1
             
            
            
             
            
            
             1
            
            
             
            
           
           
            
             0
            
            
             
            
            
             1
            
            
             
            
            
             
              −12
             
            
            
             
            
           
           
            
             0
            
            
             
            
            
             0
            
            
             
            
            
             
              57
             
            
            
             
            
           

          
         |
          
           
            
           
           
            8
           
          
          
           
            
           
           
            
             −15
            
           
          
          
           
            
           
           
            
             57
            
           
          

         
         ]
       
      
      
       
      
      
       
      
      
       
      
      
       
        −
         1
         
          57
         
        
        
         R
         3
        
        =
         R
         3
        
        →[ 
         
          
           
            
             1
            
            
             
            
            
             
              −1
             
            
            
             
            
            
             1
            
            
             
            
           
           
            
             0
            
            
             
            
            
             1
            
            
             
            
            
             
              −12
             
            
            
             
            
           
           
            
             0
            
            
             
            
            
             0
            
            
             
            
            
             1
            
            
             
            
           

          
         |
          
           
            
           
           
            8
           
          
          
           
            
           
           
            
             −15
            
           
          
          
           
            
           
           
            1
           
          

         
         ]
       
      
     

    
   
  
 

The last matrix represents the equivalent system.
   
 
  
   
    
     
      x−y+z=8
     
    
   
   
    
     
        y−12z=−15
     
    
   
   
    
     
                  z=1
     
    
   

  
 

Using back-substitution, we obtain the solution as 
 
  (
   
    4,−3,1
   
  ).
 
 

Solving a Dependent System of Linear Equations Using Matrices
Solve the following system of linear equations using matrices.
   
 
  
   
    
     
      −x−2y+z=−1
     
    
   
   
    
     
       2x+3y=2
     
    
   
   
    
     
      y−2z=0
     
    
   

  
 

Write the augmented matrix.
   
 
  [ 
   
    
     
      
−1
      
     
     
      
−2
      
     
     
      1
     
    
    
     
      2
     
     
      3
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      
−2
      
     
    

    |
     
     
      
       
        −1
       
      
     
     
      
       2
      
     
     
      
       0
      
     

    
   
   ]
 

First, multiply row 1 by 
 
  −1
 
 to get a 1 in row 1, column 1. Then, perform row operations to obtain row-echelon form. 
 
  −
   R
   1
  
  →

  [ 
   
    
     
      
1
      
     
     
      
2
      
     
     
      −1
     
    
    
     
      2
     
     
      3
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      
−2
      
     
    

    |
     
     
      
       
        1
       
      
     
     
      
       2
      
     
     
      
       0
      
     

    
   
   ]
 
 

 
 
  
   R
   2
  
  ↔
   R
   3
  
  →[ 
   
    
     
      1
     
     
      
     
     
      2
     
     
      
     
     
      
       −1
      
     
    
    
     
      0
     
     
      
     
     
      1
     
     
      
     
     
      
       −2
      
     
    
    
     
      2
     
     
      
     
     
      3
     
     
      
     
     
      0
     
    

    |
    
     
      
       
      
      
       1
      
     
     
      
       
      
      
       0
      
     
     
      
       
      
      
       2
      
     

    
   
   ]
 

 
 
  −2
   R
   1
  
  +
   R
   3
  
  =
   R
   3
  
  →[ 
   
    
     
      
       1
      
      
       
      
      
       2
      
      
       
      
      
       
        −1
       
      
      
       
      
     
     
      
       0
      
      
       
      
      
       1
      
      
       
      
      
       
        −2
       
      
      
       
      
     
     
      
       0
      
      
       
      
      
       
        −1
       
      
      
       
      
      
       2
      
      
       
      
     

    
   |
    
     
      
     
     
      1
     
    
    
     
      
     
     
      0
     
    
    
     
      
     
     
      0
     
    

   
   ]
 

 
 
  
   R
   2
  
  +
   R
   3
  
  =
   R
   3
  
  →[ 
   
    
     
      
       1
      
      
       
      
      
       2
      
      
       
      
      
       
        −1
       
      
      
       
      
     
     
      
       0
      
      
       
      
      
       1
      
      
       
      
      
       
        −2
       
      
      
       
      
     
     
      
       0
      
      
       
      
      
       0
      
      
       
      
      
       0
      
      
       
      
     

    
   |
    
     
      
     
     
      1
     
    
    
     
      
     
     
      1
     
    
    
     
      
     
     
      0
     
    

   
   ]
 

The last matrix represents the following system.
   
 
  
   
    
     
      x+2y−z=1
     
    
   
   
    
     
             y−2z=0
     
    
   
   
    
     
                     0=0
     
    
   

  
 

We see by the identity 
 
  0=0
 
 that this is a dependent system with an infinite number of solutions. We then find the generic solution. By solving the second equation for 
 
  y
 
 and substituting it into the first equation we can solve for 
 
  z
 
 in terms of 
 
  x.
 

 
 
  
   
    
     
      x+2y−z=1
     
    
   
   
    
     
                       y=2z
     
    
   
   
    
     
    
   
   
    
     
      x+2(2z)−z=1
     
    
   
   
    
     
                x+3z=1
     
    
   
   
    
     
                       z=
       
        1−x
       
       3
      

     
    
   

  
 

Now we substitute the expression for 
 
  z
 
 into the second equation to solve for 
 
  y
 
 in terms of 
 
  x.
 
  
 
  
   
    
     y−2z=0
     
    
   
   
    
     z=
       
        1−x
       
       3
      

     
    
   
   
    
     
    
   
   
    
     y−2(
       
        
         
          1−x
         
         3
        

       
      )=0
     
    
   
   
    
     y=
       
        2−2x
       
       3
      

     
    
   

  
 

The generic solution is 
 
  (
   
    x,
     
      2−2x
     
     3
    
    ,
     
      1−x
     
     3
    

   
  ).
 
 

Try It

Solve the system using matrices.
   
 
  
   
    x+4y−z=4
   
  
  
   
    2x+5y+8z=15
   
  
  
   
    x+3y−3z=1
   
  
 

 

 
 
  (
   
    1,1,1
   
  )
 
 

Q&A
Can any system of linear equations be solved by Gaussian elimination?
Yes, a system of linear equations of any size can be solved by Gaussian elimination.

How To
Given a system of equations, solve with matrices using a calculator.
Save the augmented matrix as a matrix variable 
 
  [A],[B],[C], ….
 

Use the ref( function in the calculator, calling up each matrix variable as needed.

Solving Systems of Equations with Matrices Using a Calculator
Solve the system of equations.
 
 
  
   
    
     
       5x+3y+9z=−1
     
    
   
   
    
     
      −2x+3y−z=−2
     
    
   
   
    
     
      −x−4y+5z=1
     
    
   

  
 

Write the augmented matrix for the system of equations.
 
 
  [ 
   
    
     
      5
     
     
      3
     
     
      9
     
    
    
     
      
       −2
      
     
     
      3
     
     
      
       −1
      
     
    
    
     
      
       −1
      
     
     
      
       −4
      
     
     
      5
     
    

    |
     
     
      
       −1
      
     
     
      
       
        −2
       
      
     
     
      
       
        −1
       
      
     

    
   
   ]
 

On the matrix page of the calculator, enter the augmented matrix above as the matrix variable 
 
  [ A ].
 
 
 
 
  [A]=[ 
   
    
     
      5
     
     
      
     
     
      3
     
     
      
     
     
      9
     
     
      
     
     
      
       −1
      
     
    
    
     
      
       −2
      
     
     
      
     
     
      3
     
     
      
     
     
      
       −1
      
     
     
      
     
     
      
       −2
      
     
    
    
     
      
       −1
      
     
     
      
     
     
      
       −4
      
     
     
      
     
     
      5
     
     
      
     
     
      1
     
    

   
   ]
 

Use the ref( function in the calculator, calling up the matrix variable 
 
  [ A ].
 
 
 
 
  ref([A])
 

Evaluate.
 
 
  
   
    
     
    
   
   
    
     
      [ 
       
        
         
          1
         
         
          
           
            3
            5
           

          
         
         
          
           
            9
            5
           

          
         
         
          
            -
           
            1
            5
           

          
         
        
        
         
          0
         
         
          
           1
          
         
         
          
           
            
             13
            
            
             21
            
           

          
         
         
          
           −
            4
            7
           

          
         
        
        
         
          0
         
         
          
           0
          
         
         
          
           1
          
         
         
          
           −
            
             24
            
            
             187
            
           

          
         
        

       
       ]→
       
        
         
          x+
           3
           5
          
          y+
           9
           5
          
          z=−
           1
           5
          

         
        
       
       
        
         y+
           
            13
           
           
            21
           
          
          z=−
           4
           7
          

         
        
       
       
        
         z=−
           
            24
           
           
            187
           
          

         
        
       

      
     
    
   

  
 

Using back-substitution, the solution is 
 
  (
   
    
     
      61
     
     
      187
     
    
    ,−
     
      92
     
     
      187
     
    
    ,−
     
      24
     
     
      187
     
    

   
  ).
 
 

Applying 2 × 2 Matrices to Finance
Carolyn invests a total of $12,000 in two municipal bonds, one paying 10.5% interest and the other paying 12% interest. The annual interest earned on the two investments last year was $1,335. How much was invested at each rate?

We have a system of two equations in two variables. Let 
 
  x=
 
 the amount invested at 10.5% interest, and 
 
  y=
 
 the amount invested at 12% interest.
   
 
  
   
    
     
                     x+y=12,000
     
    
   
   
    
     
      0.105x+0.12y=1,335
     
    
   

  
 

As a matrix, we have
   
 
  [ 
   
    
     
      1
     
     
      1
     
    
    
     
      
       0.105
      
     
     
      
       0.12
      
     
    

    |
     
     
      
       
        12,000
       
      
     
     
      
       
        1,335
       
      
     

    
   
   ]
 

Multiply row 1 by 
 
  −0.105
 
 and add the result to row 2. 
 
  [ 
   
    
     
      1
     
     
      1
     
    
    
     
      0
     
     
      
       0.015
      
     
    

    |
     
     
      
       
        12,000
       
      
     
     
      
       
        75
       
      
     

    
   
   ]
 

Then,
 
 
  
   
    
     
      0.015y=75
     
    
   
   
    
     
              y=5,000
     
    
   

  
 

So 
 
  12,000−5,000=7,000.
 
 Thus, $5,000 was invested at 12% interest and $7,000 at 10.5% interest.

Applying 3 × 3 Matrices to Finance
Ava invests a total of $10,000 in three accounts, one paying 5% interest, another paying 8% interest, and the third paying 9% interest. The annual interest earned on the three investments last year was $770. The amount invested at 9% was twice the amount invested at 5%. How much was invested at each rate?

We have a system of three equations in three variables. Let 
 
  x
 
 be the amount invested at 5% interest, let 
 
  y
 
 be the amount invested at 8% interest, and let 
 
  z
 
 be the amount invested at 9% interest. Thus,
   
 
  
   
    
     
                          x+y+z=10,000
     
    
   
   
    
     
      0.05x+0.08y+0.09z=770
     
    
   
   
    
     
                              2x−z=0
     
    
   

  
 

As a matrix, we have
   
 
  [ 
   
    
     
      1
     
     
      1
     
     
      1
     
    
    
     
      
       0.05
      
     
     
      
       0.08
      
     
     
      
       0.09
      
     
    
    
     
      2
     
     
      0
     
     
      
       −1
      
     
    

    |
     
     
      
       
        10,000
       
      
     
     
      
       
        770
       
      
     
     
      
       0
      
     

    
   
   ]
 

Now, we perform Gaussian elimination to achieve row-echelon form.
 
 
  
   
    
     
      
       
        
         
        
       
       
        
         
          −0.05
           R
           1
          
          +
           R
           2
          
          =
           R
           2
          
          →[ 
           
            
             
              
               1
              
              
               
              
              
               1
              
              
               
              
              
               1
              
              
               
              
             
             
              
               0
              
              
               
              
              
               
                0.03
               
              
              
               
              
              
               
                0.04
               
              
              
               
              
             
             
              
               2
              
              
               
              
              
               0
              
              
               
              
              
               
                −1
               
              
              
               
              
             

            
           |
            
             
              
             
             
              
               10,000
              
             
            
            
             
              
             
             
              
               270
              
             
            
            
             
              
             
             
              0
             
            

           
           ]
         
        
       

      
     
    
   
   
    
     
      −2
       R
       1
      
      +
       R
       3
      
      =
       R
       3
      
      →[ 
       
        
         
          
           1
          
          
           
          
          
           1
          
          
           
          
          
           1
          
          
           
          
         
         
          
           0
          
          
           
          
          
           
            0.03
           
          
          
           
          
          
           
            0.04
           
          
          
           
          
         
         
          
           0
          
          
           
          
          
           
            −2
           
          
          
           
          
          
           
            −3
           
          
          
           
          
         

        
       |
        
         
          
         
         
          
           10,000
          
         
        
        
         
          
         
         
          
           270
          
         
        
        
         
          
         
         
          
           −20,000
          
         
        

       
       ]
     
    
   
   
    
     
      
       1
       
        0.03
       
      
      
       R
       2
      
      =
       R
       2
      
      →[ 
       
        
         
          
           0
          
          
           
          
          
           1
          
          
           
          
          
           1
          
          
           
          
         
         
          
           0
          
          
           
          
          
           1
          
          
           
          
          
           
            
             4
             3
            

           
          
          
           
          
         
         
          
           0
          
          
           
          
          
           
            −2
           
          
          
           
          
          
           
            −3
           
          
          
           
          
         

        
       |
        
         
          
         
         
          
           10,000
          
         
        
        
         
          
         
         
          
           9,000
          
         
        
        
         
          
         
         
          
           −20,000
          
         
        

       
       ]
     
    
   
   
    
     
      2
       R
       2
      
      +
       R
       3
      
      =
       R
       3
      
      →[ 
       
        
         
          
           1
          
          
           
          
          
           1
          
          
           
          
          
           1
          
          
           
          
         
         
          
           0
          
          
           
          
          
           1
          
          
           
          
          
           
            
             4
             3
            

           
          
          
           
          
         
         
          
           0
          
          
           
          
          
           0
          
          
           
          
          
           
            −
             1
             3
            

           
          
          
           
          
         

        
       |
        
         
          
         
         
          
           10,000
          
         
        
        
         
          
         
         
          
           9,000
          
         
        
        
         
          
         
         
          
           −2,000
          
         
        

       
       ]
     
    
   

  
 

The third row tells us 
 
  −
   1
   3
  
  z=−2,000;
 
 thus 
 
  z=6,000.
 
 The second row tells us 
 
  y+
   4
   3
  
  z=9,000.
 
 Substituting 
 
  z=6,000,
 
 we get 
 
  
   
    
     
      y+
       4
       3
      
      (6,000)=9,000
     
    
   
   
    
     
      y+8,000=9,000
     
    
   
   
    
     
      y=1,000
     
    
   

  
 

The first row tells us 
 
  x+y+z=10,000.
 
 Substituting 
 
  y=1,000
 
 and 
 
  z=6,000,
 
 we get 
 
  
   
    
     
      x+1,000+6,000=10,000
     
    
   
   
    
     
                                   x=3,000
     
    
   

  
 

The answer is $3,000 invested at 5% interest, $1,000 invested at 8%, and $6,000 invested at 9% interest.

Try It

A small shoe company took out a loan of $1,500,000 to expand their inventory. Part of the money was borrowed at 7%, part was borrowed at 8%, and part was borrowed at 10%. The amount borrowed at 10% was four times the amount borrowed at 7%, and the annual interest on all three loans was $130,500. Use matrices to find the amount borrowed at each rate.
$150,000 at 7%, $750,000 at 8%, $600,000 at 10%

Media
Access these online resources for additional instruction and practice with solving systems of linear equations using Gaussian elimination.

Solve a System of Two Equations Using an Augmented Matrix
Solve a System of Three Equations Using an Augmented Matrix
Augmented Matrices on the Calculator

Key Concepts

An augmented matrix is one that contains the coefficients and constants of a system of equations. See .
A matrix augmented with the constant column can be represented as the original system of equations. See .
Row operations include multiplying a row by a constant, adding one row to another row, and interchanging rows.
We can use Gaussian elimination to solve a system of equations. See , , and .
Row operations are performed on matrices to obtain row-echelon form. See .
To solve a system of equations, write it in augmented matrix form. Perform row operations to obtain row-echelon form. Back-substitute to find the solutions. See  and .
A calculator can be used to solve systems of equations using matrices. See .
Many real-world problems can be solved using augmented matrices. See  and .

Section Exercises

Verbal

Can any system of linear equations be written as an augmented matrix? Explain why or why not. Explain how to write that augmented matrix.
Yes.  For each row, the coefficients of the variables are written across the corresponding row, and a vertical bar is placed; then the constants are placed to the right of the vertical bar.

Can any matrix be written as a system of linear equations? Explain why or why not. Explain how to write that system of equations.
Is there only one correct method of using row operations on a matrix? Try to explain two different row operations possible to solve the augmented matrix 
 
  [ 
   
    
     
      9
     
     
      3
     
    
    
     
      1
     
     
      
       −2
      
     
    

    |
     
     
      
       0
      
     
     
      
       6
      
     

    
   
   ].
 

No, there are numerous correct methods of using row operations on a matrix. Two possible ways are the following: (1) Interchange rows 1 and 2. Then 
 
  
   R
   2
  
  =
   R
   2
  
  −9
   R
   1
  
  .
 
 (2) 
 
  
   R
   2
  
  =
   R
   1
  
  −9
   R
   2
  
  .
 
 Then divide row 1 by 9.
Can a matrix whose entry is 0 on the diagonal be solved? Explain why or why not. What would you do to remedy the situation?
Can a matrix that has 0 entries for an entire row have one solution? Explain why or why not.
No. A matrix with 0 entries for an entire row would have either zero or infinitely many solutions.

Algebraic
For the following exercises, write the augmented matrix for the linear system.
 
 
  
   
    8x−37y=8
   
  
  
   
    2x+12y=3
   
  
 

 

 
 
  
   
    
     
        16y=4
     
    
   
   
    
     
      9x−y=2
     
    
   

  
 

 
 
  [ 
   
    
     
      
       0
      
      
       
      
      
       
        16
       
      
      
       
      
     
     
      
       9
      
      
       
      
      
       
        −1
       
      
      
       
      
     

    
   |
    
     
      
     
     
      4
     
    
    
     
      
     
     
      2
     
    

   
   ]
 

 
 
  
   
    
     
      3x+2y+10z=3
     
    
   
   
    
     
      −6x+2y+5z=13
     
    
   
   
    
     
                  4x+z=18
     
    
   

  
 

 
 
  
   
    
     
    
   
   
    
     
       x+5y+8z=19
     
    
   
   
    
     
      12x+3y=4
     
    
   
   
    
     
      3x+4y+9z=−7
     
    
   

  
 

 
 
  [ 
   
    
     
      
       1
      
      
       
      
      
       5
      
      
       
      
      
       8
      
      
       
      
     
     
      
       
        12
       
      
      
       
      
      
       3
      
      
       
      
      
       0
      
      
       
      
     
     
      
       3
      
      
       
      
      
       4
      
      
       
      
      
       9
      
      
       
      
     

    
   |
    
     
      
     
     
      
       19
      
     
    
    
     
      
     
     
      4
     
    
    
     
      
     
     
      
       −7
      
     
    

   
   ]
 

 
 
  
   
    
     
      6x+12y+16z=4
     
    
   
   
    
     
       19x−5y+3z=−9
     
    
   
   
    
     
                  x+2y=−8
     
    
   

  
 

For the following exercises, write the linear system from the augmented matrix.

 
 
  [ 
   
    
     
      
       −2
      
     
     
      5
     
    
    
     
      6
     
     
      
       −18
      
     
    

    |
     
     
      
       5
      
     
     
      
       
        26
       
      
     

    
   
   ]
 

 
 
  
   
    −2x+5y=5
   
  
  
   
    6x−18y=26
   
  
 

 

 
 
  [ 
   
    
     
      3
     
     
      4
     
    
    
     
      
       10
      
     
     
      
       17
      
     
    

    |
     
     
      
       
        10
       
      
     
     
      
       
        439
       
      
     

    
   
   ]
 

 
 
  [ 
   
    
     
      3
     
     
      2
     
     
      0
     
    
    
     
      
       −1
      
     
     
      
       −9
      
     
     
      4
     
    
    
     
      8
     
     
      5
     
     
      7
     
    

    |
     
     
      
       3
      
     
     
      
       
        −1
       
      
     
     
      
       8
      
     

    
   
   ]
 

 
 
  
   
    3x+2y=3
   
  
  
   
    −x−9y+4z=−1
   
  
  
   
    8x+5y+7z=8
   
  
 

 

 
 
  [ 
   
    
     
      8
     
     
      
       29
      
     
     
      1
     
    
    
     
      
       −1
      
     
     
      7
     
     
      5
     
    
    
     
      0
     
     
      0
     
     
      3
     
    

    |
     
     
      
       
        43
       
      
     
     
      
       
        38
       
      
     
     
      
       
        10
       
      
     

    
   
   ]
 

 
 
  [ 
   
    
     
      4
     
     
      5
     
     
      
       −2
      
     
    
    
     
      0
     
     
      1
     
     
      
       58
      
     
    
    
     
      8
     
     
      7
     
     
      
       −3
      
     
    

    |
     
     
      
       
        12
       
      
     
     
      
       2
      
     
     
      
       
        −5
       
      
     

    
   
   ]
 

 
 
  
   
    
     
      4x+5y−2z=12
     
    
   
   
    
     
             y+58z=2
     
    
   
   
    
     
      8x+7y−3z=−5
     
    
   

  
 

For the following exercises, solve the system by Gaussian elimination.

 
 
  [ 
   
    
     
      1
     
     
      0
     
    
    
     
      0
     
     
      0
     
    

    |
     
     
      
       3
      
     
     
      
       0
      
     

    
   
   ]
 

 
 
  [ 
   
    
     
      1
     
     
      0
     
    
    
     
      1
     
     
      0
     
    

    |
     
     
      
       1
      
     
     
      
       2
      
     

    
   
   ]
 

No solutions

 
 
  [ 
   
    
     
      1
     
     
      2
     
    
    
     
      4
     
     
      5
     
    

    |
     
     
      
       3
      
     
     
      
       6
      
     

    
   
   ]
 

 
 
  [ 
   
    
     
      
       −1
      
     
     
      2
     
    
    
     
      4
     
     
      
       −5
      
     
    

    |
     
     
      
       
        −3
       
      
     
     
      
       6
      
     

    
   
   ]
 

 
 
  (−1,−2)
 
 

 
 
  [ 
   
    
     
      
       −2
      
     
     
      0
     
    
    
     
      0
     
     
      2
     
    

    |
     
     
      
       1
      
     
     
      
       
        −1
       
      
     

    
   
   ]
 

 
 
  
   
    
     
       2x−3y=−9
     
    
   
   
    
     
      5x+4y=58
     
    
   

  
 

 
 
  (
   
    6,7
   
  )
 
 

 
 
  
   
    6x+2y=−4
   
  
  
   
    3x+4y=−17
   
  
 

 

 
 
  
   
    
     
      2x+3y=12
     
    
   
   
    
     
       4x+y=14
     
    
   

  
 

 
 
  (
   
    3,2
   
  )
 
 

 
 
  
   
    
     
      −4x−3y=−2
     
    
   
   
    
     
       3x−5y=−13
     
    
   

  
 

 
 
  
   
    
     
      −5x+8y=3
     
    
   
   
    
     
      10x+6y=5
     
    
   

  
 

 
 
  (
   
    
     1
     5
    
    ,
     1
     2
    

   
  )
 
 

 
 
  
   
    
     
       3x+4y=12
     
    
   
   
    
     
      −6x−8y=−24
     
    
   

  
 

 
 
  
   
    
     
      −60x+45y=12
     
    
   
   
    
     
       20x−15y=−4
     
    
   

  
 

 
 
  (
   
    x,
     4
     
      15
     
    
    (5x+1)
   
  )
 
 

 
 
  
   
    11x+10y=43
   
  
  
   
    15x+20y=65
   
  
 

 

 
 
  
   
    
     
      2x−y=2
     
    
   
   
    
     
      3x+2y=17
     
    
   

  
 

 
 
  (
   
    3,4
   
  )
 
 

 
 
  
   
    
     
      
       
        
       
      
      
       
        −1.06x−2.25y=5.51
       
      
     

    
   
   
    
     
      −5.03x−1.08y=5.40
     
    
   

  
 

 
 
  
   
    
     3
     4
    
    x−
     3
     5
    
    y=4
   
  
  
   
    
     1
     4
    
    x+
     2
     3
    
    y=1
   
  
 

 
 
 
  (
   
    
     
      196
     
     
      39
     
    
    ,−
     5
     
      13
     
    

   
  )
 
 

 
 
  
   
    
     1
     4
    
    x−
     2
     3
    
    y=−1
   
  
  
   
    
     1
     2
    
    x+
     1
     3
    
    y=3
   
  
 

 

 
 
  [ 
   
    
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      1
     
    
    
     
      0
     
     
      0
     
     
      1
     
    

    |
     
     
      
       
        31
       
      
     
     
      
       
        45
       
      
     
     
      
       
        87
       
      
     

    
   
   ]
 

 
 
  (
   
    31,−42,87
   
  )
 
 

 
 
  [ 
   
    
     
      1
     
     
      0
     
     
      1
     
    
    
     
      1
     
     
      1
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      1
     
    

    |
     
     
      
       
        50
       
      
     
     
      
       
        20
       
      
     
     
      
       
        −90
       
      
     

    
   
   ]
 

 
 
  [ 
   
    
     
      1
     
     
      2
     
     
      3
     
    
    
     
      0
     
     
      5
     
     
      6
     
    
    
     
      0
     
     
      0
     
     
      8
     
    

    |
     
     
      
       4
      
     
     
      
       7
      
     
     
      
       9
      
     

    
   
   ]
 

 
 
  (
   
    
     
      21
     
     
      40
     
    
    ,
     1
     
      20
     
    
    ,
     9
     8
    

   
  )
 
 

 
 
  [ 
   
    
     
      
       −0.1
      
     
     
      
       0.3
      
     
     
      
       −0.1
      
     
    
    
     
      
       −0.4
      
     
     
      
       0.2
      
     
     
      
       0.1
      
     
    
    
     
      
       0.6
      
     
     
      
       0.1
      
     
     
      
       0.7
      
     
    

    |
     
     
      
       
        0.2
       
      
     
     
      
       
        0.8
       
      
     
     
      
       
        −0.8
       
      
     

    
   
   ]
 

 
 
  
   
    
     
      −2x+3y−2z=3
     
    
   
   
    
     
           4x+2y−z=9
     
    
   
   
    
     
      4x−8y+2z=−6
     
    
   

  
 

 
 
  (
   
    
     
      18
     
     
      13
     
    
    ,
     
      15
     
     
      13
     
    
    ,−
     
      15
     
     
      13
     
    

   
  )
 
 

 
 
  
   
    
     
           x+y−4z=−4
     
    
   
   
    
     
       5x−3y−2z=0
     
    
   
   
    
     
       2x+6y+7z=30
     
    
   

  
 

 
 
  
   
    
     
           2x+3y+2z=1
     
    
   
   
    
     
       −4x−6y−4z=−2
     
    
   
   
    
     
      10x+15y+10z=5
     
    
   

  
 

 
 
  (
   
    x,y,
     1
     2
    
    (1−2x−3y)
   
  )
 
 

 
 
  
   
    
     
         x+2y−z=1
     
    
   
   
    
     
      −x−2y+2z=−2
     
    
   
   
    
     
      3x+6y−3z=5
     
    
   

  
 

 
 
  
   
    
     
         x+2y−z=1
     
    
   
   
    
     
      −x−2y+2z=−2
     
    
   
   
    
     
      3x+6y−3z=3
     
    
   

  
 

 
 
  (
   
    x,−
     x
     2
    
    ,−1
   
  )
 
 

 
 
  
   
    
     
x+y=2
     
    
   
   
    
     
        x+z=1
     
    
   
   
    
     
      −y−z=−3
     
    
   

  
 

 
 
  
   
    
     
      x+y+z=100
     
    
   
   
    
     
         x+2z=125
     
    
   
   
    
     
      −y+2z=25
     
    
   

  
 

 
 
  (
   
    125,−25,0
   
  )
 
 

 
 
  
   
    
     1
     4
    
    x−
     2
     3
    
    z=−
     1
     2
    

   
  
  
   
    
     1
     5
    
    x+
     1
     3
    
    y=
     4
     7
    

   
  
  
   
    
     1
     5
    
    y−
     1
     3
    
    z=
     2
     9
    

   
  
 

 

 
 
  
   
    
     
      −
       1
       2
      
      x+
       1
       2
      
      y+
       1
       7
      
      z=−
       
        53
       
       
        14
       
      

     
    
   
   
    
     
        
       1
       2
      
      x−
       1
       2
      
      y+
       1
       4
      
      z=3
     
    
   
   
    
     
         
       1
       4
      
      x+
       1
       5
      
      y+
       1
       3
      
      z=
       
        23
       
       
        15
       
      

     
    
   

  
 

 
 
  (
   
    8,1,−2
   
  )
 
 

 
 
  
   
    
     
      −
       1
       2
      
      x−
       1
       3
      
      y+
       1
       4
      
      z=−
       
        29
       
       6
      

     
    
   
   
    
     
        
       1
       5
      
      x+
       1
       6
      
      y−
       1
       7
      
      z=
       
        431
       
       
        210
       
      

     
    
   
   
    
     
      −
       1
       8
      
      x+
       1
       9
      
      y+
       1
       
        10
       
      
      z=−
       
        49
       
       
        45
       
      

     
    
   

  
 

Extensions
For the following exercises, use Gaussian elimination to solve the system.

 
  
   
    
     
      
       
        x−1
       
       7
      
      +
       
        y−2
       
       8
      
      +
       
        z−3
       
       4
      
      =0
     
    
   
   
    
     x+y+z=6
     
    
   
   
    
     
      
       
        x+2
       
       3
      
      +2y+
       
        z−3
       
       3
      
      =5
     
    
   

  
 

 
 
  (
   
    1,2,3
   
  )
 
 

 
 
  
   
    
     
      
       
        x−1
       
       4
      
      −
       
        y+1
       
       4
      
      +3z=−1
     
    
   
   
    
     
       
       
        x+5
       
       2
      
      +
       
        y+7
       
       4
      
      −z=4
     
    
   
   
    
     
              x+y−
       
        z−2
       
       2
      
      =1
     
    
   

  
 

 
  
   
    
     
       
        x−3
       
       4
      
      −
       
        y−1
       
       3
      
      +2z=−1
     
    
   
   
    
     
      
       
        x+5
       
       2
      
      +
       
        y+5
       
       2
      
      +
       
        z+5
       
       2
      
      =8
     
    
   
   
    
     x+y+z=1
     
    
   

  
 

 
 
  (
   
    x,
     
      31
     
     
      28
     
    
    −
     
      3x
     
     4
    
    ,
     1
     
      28
     
    
    (−7x−3)
   
  )
 
 

 
 
  
   
    
     
      
       
        x−3
       
       
        10
       
      
      +
       
        y+3
       
       2
      
      −2z=3
     
    
   
   
    
     
      
       
        x+5
       
       4
      
      −
       
        y−1
       
       8
      
      +z=
       3
       2
      

     
    
   
   
    
     
      
       
        x−1
       
       4
      
      +
       
        y+4
       
       2
      
      +3z=
       3
       2
      

     
    
   

  
 

 
  
   
    
     
      
       
        x−3
       
       4
      
      −
       
        y−1
       
       3
      
      +2z=−1
     
    
   
   
    
     
      
       
        x+5
       
       2
      
      +
       
        y+5
       
       2
      
      +
       
        z+5
       
       2
      
      =7
     
    
   
   
    
     x+y+z=1
     
    
   

  
 

No solutions exist.

Real-World Applications
For the following exercises, set up the augmented matrix that describes the situation, and solve for the desired solution.

Every day, Angeni's cupcake store sells 5,000 cupcakes in chocolate and vanilla flavors. If the chocolate flavor is 3 times as popular as the vanilla flavor, how many of each cupcake does the store sell per day?
At Bakari's competing cupcake store, $4,520 worth of cupcakes are sold daily. The chocolate cupcakes cost $2.25 and the red velvet cupcakes cost $1.75. If the total number of cupcakes sold per day is 2,200, how many of each flavor are sold each day?
860 red velvet, 1,340 chocolate

You invested $10,000 into two accounts: one that has simple 3% interest, the other with 2.5% interest. If your total interest payment after one year was $283.50, how much was in each account after the year passed?
You invested $2,300 into account 1, and $2,700 into account 2. If the total amount of interest after one year is $254, and account 2 has 1.5 times the interest rate of account 1, what are the interest rates? Assume simple interest rates.
4% for account 1, 6% for account 2

Bikes’R’Us manufactures bikes, which sell for $250. It costs the manufacturer $180 per bike, plus a startup fee of $3,500. After how many bikes sold will the manufacturer break even?
A major appliance store has agreed to order vacuums from a startup founded by college engineering students. The store would be able to purchase the vacuums for $86 each, with a delivery fee of $9,200, regardless of how many vacuums are sold. If the store needs to start seeing a profit after 230 units are sold, how much should they charge for the vacuums?
$126

The three most popular ice cream flavors are chocolate, strawberry, and vanilla, comprising 83% of the flavors sold at an ice cream shop. If vanilla sells 1% more than twice strawberry, and chocolate sells 11% more than vanilla, how much of the total ice cream consumption are the vanilla, chocolate, and strawberry flavors?
At an ice cream shop, three flavors are increasing in demand.  Last year, banana, pumpkin, and rocky road ice cream made up 12% of total ice cream sales. This year, the same three ice creams made up 16.9% of ice cream sales. The rocky road sales doubled, the banana sales increased by 50%, and the pumpkin sales increased by 20%. If the rocky road ice cream had one less percent of sales than the banana ice cream, find out the percentage of ice cream sales each individual ice cream made last year.
Banana was 3%, pumpkin was 7%, and rocky road was 2%

A bag of mixed nuts contains cashews, pistachios, and almonds. There are 1,000 total nuts in the bag, and there are 100 less almonds than pistachios. The cashews weigh 3 g, pistachios weigh 4 g, and almonds weigh 5 g. If the bag weighs 3.7 kg, find out how many of each type of nut is in the bag.
A bag of mixed nuts contains cashews, pistachios, and almonds. Originally there were 900 nuts in the bag. 30% of the almonds, 20% of the cashews, and 10% of the pistachios were eaten, and now there are 770 nuts left in the bag. Originally, there were 100 more cashews than almonds. Figure out how many of each type of nut was in the bag to begin with.
100 almonds, 200 cashews, 600 pistachios

augmented matrix
a coefficient matrix adjoined with the constant column separated by a vertical line within the matrix brackets

coefficient matrix
a matrix that contains only the coefficients from a system of equations

Gaussian elimination
using elementary row operations to obtain a matrix in row-echelon form

main diagonal
entries from the upper left corner diagonally to the lower right corner of a square matrix

row-echelon form
after performing row operations, the matrix form that contains ones down the main diagonal and zeros at every space below the diagonal

row-equivalent
two matrices 
 
  A
 
 and 
 
  B
 
 are row-equivalent if one can be obtained from the other by performing basic row operations

row operations
adding one row to another row, multiplying a row by a constant, interchanging rows, and so on, with the goal of achieving row-echelon form
