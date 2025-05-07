Matrices and Matrix Operations

  m49433
  Matrices and Matrix Operations
  In this section, you will:
Find the sum and difference of two matrices.
Find scalar multiples of a matrix.
Find the product of two matrices.

  508a4d4e-0136-4c6c-87b8-e210022d69b4

Learning Objectives

Write the augmented matrix for a system of equations (IA 4.5.1)
Add, subtract matrices and multiply a matrix by a scalar

Objective 1: Write the augmented matrix for a system of equations (IA 4.5.1)A matrix is a rectangular array of numbers arranged in rows and columns.A matrix with m rows and n columns has dimension m×n.
Each number in the matrix is called an element or entry in the matrix.
The matrix on the left below has 2 rows and 3 columns and so it has order 2×3. We say it is a 2 by 3 matrix.

    
  We will use a matrix to represent systems of equations.
Each column then would be the coefficients of one of the variables in the system or the constants.
A vertical line replaces the equal signs.
We call the resulting matrix the augmented matrix for the system of equations.

  
    
  
Write each system of linear equations as an augmented matrix

  ⓐ
 3x-y=-12y=2x+5
  
  ⓑ
 4x+3y=-2x-2y-3z=72x-y+2z=-6
  

  ⓐ
 We first rewrite the second equation in standard form 
 3x-y=-1-2x+2y=5 
Next we write the augmented matrix
 3x-y=-1-2x+2y=5
⇒

[

3

−1

−2

2

|

−1

5

]

xy

 

ⓑ
 Each equation is in standard form
Write the augmented matrix
 4x+3y=-2x-2y-3z=72x-y+2z=-6

⇒

[

4

3

0

1

−2

−3

2

−1

2

|

−2

7

−6

]

xyz

  
  
Practice Makes Perfect
Write each system of linear equations as an augmented matrix

  
 2x-5y=-34x=3y-1
  

  
 4x+3y-2z=-3-2x+y-3z=4-x-4y+5z=-2
  

Objective 2: Add, subtract matrices and multiply a matrix by a scalarWe add or subtract matrices by adding or subtracting corresponding entries.
In order to do this, the entries must correspond. Therefore, addition and subtraction of matrices is only possible when the matrices have the same dimensions. We can add or subtract a 3 × 3 matrix and another 3 × 3 matrix, but we cannot add or subtract a 2 × 3 matrix and a 3 × 3 matrix because some entries in one matrix will not have a corresponding entry in the other matrix.

The process of scalar multiplication involves multiplying each entry in a matrix by a scalar. A scalar multiple is any entry of a matrix that results from scalar multiplication.

  ⓐ
Add the two matrices A=abcd B=efgh
  
 ⓑ Subtract the two matrices A=2-453 B=6978
  

  ⓒ Multiply the matrix A=2-453 by 5.
  

  ⓐ
 A+B=abcd+efgh=a+eb+fc+gd+h
  
  ⓑ
 A-B=2-453-6978=2-6-4-95-73-8=-4-13-2-5
  
  ⓒ
 5A=5(2)5(-4)5(5)5(3)=10-202515
  

Practice Makes Perfect 
Perform the indicated operations

  Add the two matrices A=lmnp B=qrst 

  Subtract the two matrices A=-3210 B=-5415
  

  Multiply the matrix A=2-453 by –2
  

  Find 2A+3B when A=1-648 and B=1-53-1
  

(credit: “SD Dirk,” Flickr)Two club soccer teams, the Wildcats and the Mud Cats, are hoping to obtain new equipment for an upcoming season.  shows the needs of both teams.

  

  
  Wildcats
  Mud Cats

  Goals
  6
  10

  Balls
  30
  24

  Jerseys
  14
  20

A goal costs $300; a ball costs $10; and a jersey costs $30. How can we find the total cost for the equipment needed for each team? In this section, we discover a method in which the data in the soccer equipment table can be displayed and used for calculating other information. Then, we will be able to calculate the cost of the equipment.

Finding the Sum and Difference of Two Matrices
To solve a problem like the one described for the soccer teams, we can use a matrix, which is a rectangular array of numbers. A row in a matrix is a set of numbers that are aligned horizontally. A column in a matrix is a set of numbers that are aligned vertically. Each number is an entry, sometimes called an element, of the matrix. Matrices (plural) are enclosed in [  ] or (  ), and are usually named with capital letters. For example, three matrices named 
A,B,

 and 
 
  C
 
 are shown below. 
    
      A=[ 
        
          
            
              1
            
            
              2
            
          
          
            
              3
            
            
              4
            
          

        
       ],B=[ 
        
          
            
              1
            
            
              2
            
            
              7
            
          
          
            
              0
            
            
              
                −5
              
            
            
              6
            
          
          
            
              7
            
            
              8
            
            
              2
            
          

        
       ],C=[ 
        
          
            
              
                −1
              
            
          
          
            
              
                0
              
            
          
          
            
              
                3
              
            
          

        
          
            
              3
            
          
          
            
              2
            
          
          
            
              1
            
          

        
       ]
    
  
  

 Describing Matrices
  A matrix is often referred to by its size or dimensions: 
 
  m×n
 
 indicating 
    
    m
    
   rows and 
    
    n
    
   columns. Matrix entries are defined first by row and then by column. For example, to locate the entry in matrix 
    
    A
    
   identified as 
    
    
        a
        
          ij
        
      
      ,
    
   we look for the entry in row 
    
    i,
    
   column 
    
    j.
    
   In matrix 
    
    A,  
    
   shown below, the entry in row 2, column 3 is 
    
    
        a
        
          23
        
      
      .
    
  
   
    
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
    
  
  
  A square matrix is a matrix with dimensions 
 
  n×n,
 
 meaning that it has the same number of rows as columns. The 
    
    3×3
    
   matrix above is an example of a square matrix.A row matrix is a matrix consisting of one row with dimensions 
 
  1×n.
 

   
    
      [ 
        
          
            
              
                
                  a
                  
                    11
                  
                

              
            
            
              
                
                  a
                  
                    12
                  
                

              
            
            
              
                
                  a
                  
                    13
                  
                

              
            
          

        
       ]
    
  
  
  A column matrix is a matrix consisting of one column with dimensions 
 
  m×1.
 

   
    
      [ 
        
          
            
              
                
                  a
                  
                    11
                  
                

              
            
          
          
            
              
                
                  a
                  
                    21
                  
                

              
            
          
          
            
              
                
                  a
                  
                    31
                  
                

              
            
          

        
       ]
    
  
  
A matrix may be used to represent a system of equations. In these cases, the numbers represent the coefficients of the variables in the system. Matrices often make solving systems of equations easier because they are not encumbered with variables. We will investigate this idea further in the next section, but first we will look at basic matrix operations.

Matrices
  A matrix is a rectangular array of numbers that is usually named by a capital letter: 
    
    A,B,C,
    
   and so on. Each entry in a matrix is referred to as 
    
    
        a
        
          ij
        
      
      ,
    
   such that 
    
    i
    
   represents the row and 
    
    j
    
   represents the column. Matrices are often referred to by their dimensions: 
 
  m×n
 
 indicating 
    
    m
    
   rows and 
    
    n
    
   columns.

  
    Finding the Dimensions of the Given Matrix and Locating Entries
    Given matrix 
      
        A:
      
    
    
   
ⓐWhat are the dimensions of matrix 
       
         A?
       
     
     
     ⓑWhat are the entries at 
       
         
           a
           
             31
           
         

       
      and 
       
         
           a
           
             22
           
         
         ?
       
     

        
 
  A=[ 
   
    
     
      2
     
     
      
     
     
      1
     
     
      0
     
    
    
     
      2
     
     
      
     
     
      4
     
     
      7
     
    
    
     
      3
     
     
      
     
     
      1
     
     
      
       −2
      
     
    

   
   ]
 

   
  

  
ⓐThe dimensions are 
 
  3×3
 
 because there are three rows and three columns.
    ⓑEntry 
      
        
          a
          
            31
          
        

      
     is the number at row 3, column 1, which is 3. The entry 
      
        
          a
          
            22
          
        

      
     is the number at row 2, column 2, which is 4. Remember, the row comes first, then the column.
  

 

 Adding and Subtracting Matrices
We use matrices to list data or to represent systems. Because the entries are numbers, we can perform operations on matrices. We add or subtract matrices by adding or subtracting corresponding entries.
  In order to do this, the entries must correspond. Therefore, addition and subtraction of matrices is only possible when the matrices have the same dimensions. We can add or subtract a 
 
  3×3
 
 matrix and another 
 
  3×3
 
 matrix, but we cannot add or subtract a 
 
  2×3
 
 matrix and a 
 
  3×3
 
 matrix because some entries in one matrix will not have a corresponding entry in the other matrix.

Adding and Subtracting Matrices
  Given matrices 
    
    A
    
   and 
    
    B
    
   of like dimensions, addition and subtraction of 
    
    A
    
   and 
    
    B
    
   will produce matrix 
    
    C
    
   or matrix 
    
    D
    
   of the same dimension. 
    
      A+B=Csuch that 
        a
        
          ij
        
      
      +
        b
        
          ij
        
      
      =
        c
        
          ij
        
      

    
  
  
   
    
      A−B=Dsuch that 
        a
        
          ij
        
      
      −
        b
        
          ij
        
      
      =
        d
        
          ij
        
      

    
  
  
Matrix addition is commutative.
   
    
      A+B=B+A
    
  
  
It is also associative.
   
    
      (
        
          A+B
        
        )+C=A+(
          
            B+C
          
          )
    
  
  

  
    Finding the Sum of Matrices
    Find the sum of 
      
        A
      
     and 
      
        B,
      
     given 
 
  A=[ 
   
    
     
      a
     
     
      b
     
    
    
     
      c
     
     
      d
     
    

   
   ]  and  B=[ 
   
    
     
      e
     
     
      f
     
    
    
     
      g
     
     
      h
     
    

   
   ]
 

  

  Add corresponding entries.
     
 
  
   
    
     
      A+B=[ 
       
        
         
          a
         
         
          b
         
        
        
         
          c
         
         
          d
         
        

       
       ]+[ 
       
        
         
          e
         
         
          f
         
        
        
         
          g
         
         
          h
         
        

       
       ]
     
    
   
   
    
     
              =[ 
       
        
         
          
           a+e
          
         
         
          
         
         
          
           b+f
          
         
        
        
         
          
           c+g
          
         
         
          
         
         
          
           d+h
          
         
        

       
       ]
     
    
   

  
 

  
  

    Adding Matrix A and Matrix B
    Find the sum of 
      
        A
      
     and 
      
        B.
      
    
    
     
 
  A=[ 
   
    
     
      4
     
     
      1
     
    
    
     
      3
     
     
      2
     
    

   
   ] and  B=[ 
   
    
     
      5
     
     
      9
     
    
    
     
      0
     
     
      7
     
    

   
   ]
 

  

    Add corresponding entries. Add the entry in row 1, column 1, 
      
        
          a
          
            11
          
        
        ,
      
     of matrix 
      
        A
      
     to the entry in row 1, column 1, 
      
        
          b
          
            11
          
        
        ,
      
     of 
      
        B.
      
     Continue the pattern until all entries have been added. 
 
  
   
    
     
      A+B=[ 
       
        
         
          4
         
         
          1
         
        
        
         
          3
         
         
          2
         
        

       
       ]+[ 
       
        
         
          5
         
         
          9
         
        
        
         
          0
         
         
          7
         
        

       
       ]
     
    
   
   
    
     
              =[ 
       
        
         
          
           4+5
          
         
         
          
         
         
          
           1+9
          
         
        
        
         
          
           3+0
          
         
         
          
         
         
          
           2+7
          
         
        

       
       ]
     
    
   
   
    
     
              =[ 
       
        
         
          9
         
         
          
           10
          
         
        
        
         
          3
         
         
          9
         
        

       
       ]
     
    
   

  
 

  

  
    Finding the Difference of Two Matrices
    Find the difference of 
      
        A
      
     and 
      
        B.
      
    
    
     
 
  A=[ 
   
    
     
      
       −2
      
     
     
      3
     
    
    
     
      0
     
     
      1
     
    

   
   ] and  B=[ 
   
    
     
      8
     
     
      1
     
    
    
     
      5
     
     
      4
     
    

   
   ]
 

  

  We subtract the corresponding entries of each matrix.
     
 
  
   
    
     
      A−B=[ 
       
        
         
          
           −2
          
         
         
          3
         
        
        
         
          0
         
         
          1
         
        

       
       ]−[ 
       
        
         
          8
         
         
          1
         
        
        
         
          5
         
         
          4
         
        

       
       ]
     
    
   
   
    
     
              =[ 
       
        
         
          
           −2−8
          
         
         
          
         
         
          
           3−1
          
         
        
        
         
          
           0−5
          
         
         
          
         
         
          
           1−4
          
         
        

       
       ]
     
    
   
   
    
     
              =[ 
       
        
         
          
           −10
          
         
         
          
         
         
          2
         
        
        
         
          
           −5
          
         
         
          
         
         
          
           −3
          
         
        

       
       ]
     
    
   

  
 

  
  

    Finding the Sum and Difference of Two 3 x 3 Matrices
    Given 
      
        A
      
     and 
      
        B:
      
    
    

ⓐFind the sum.
ⓑFind the difference.

     
 
  A=[ 
   
    
     
      2
     
     
      
       −10
      
     
     
      
       −2
      
     
    
    
     
      
       14
      
     
     
      
       12
      
     
     
      
       10
      
     
    
    
     
      4
     
     
      
       −2
      
     
     
      2
     
    

   
   ]and B=[ 
   
    
     
      6
     
     
      
       10
      
     
     
      
       −2
      
     
    
    
     
      0
     
     
      
       −12
      
     
     
      
       −4
      
     
    
    
     
      
       −5
      
     
     
      2
     
     
      
       −2
      
     
    

   
   ]
 

  

  
ⓐAdd the corresponding entries.
       
 
  
   
    
     
    
   
   
    
     
      A+B=[ 
       
        
         
          2
         
         
          
           −10
          
         
         
          
           −2
          
         
        
        
         
          
           14
          
         
         
          
           12
          
         
         
          
           10
          
         
        
        
         
          4
         
         
          
           −2
          
         
         
          
           2
          
         
        

       
       ]+[ 
       
        
         
          6
         
         
          
           10
          
         
         
          
           −2
          
         
        
        
         
          0
         
         
          
           −12
          
         
         
          
           −4
          
         
        
        
         
          
           −5
          
         
         
          
           2
          
         
         
          
           −2
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           2+6
          
         
         
          
           −10+10
          
         
         
          
           −2−2
          
         
        
        
         
          
           14+0
          
         
         
          
           12−12
          
         
         
          
           10−4
          
         
        
        
         
          
           4−5
          
         
         
          
           −2+2
          
         
         
          
           2−2
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          8
         
         
          
           0
          
         
         
          
           −4
          
         
        
        
         
          
           14
          
         
         
          
           0
          
         
         
          
           6
          
         
        
        
         
          
           −1
          
         
         
          
           0
          
         
         
          
           0
          
         
        

       
       ]
     
    
   

  
 

  ⓑSubtract the corresponding entries.
     
 
  
   
    
     
    
   
   
    
     
      A−B=[ 
       
        
         
          2
         
         
          
           −10
          
         
         
          
           −2
          
         
        
        
         
          
           14
          
         
         
          
           12
          
         
         
          
           10
          
         
        
        
         
          4
         
         
          
           −2
          
         
         
          2
         
        

       
       ]−[ 
       
        
         
          6
         
         
          
           10
          
         
         
          
           −2
          
         
        
        
         
          0
         
         
          
           −12
          
         
         
          
           −4
          
         
        
        
         
          
           −5
          
         
         
          2
         
         
          
           −2
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           2−6
          
         
         
          
           −10−10
          
         
         
          
           −2+2
          
         
        
        
         
          
           14−0
          
         
         
          
           12+12
          
         
         
          
           10+4
          
         
        
        
         
          
           4+5
          
         
         
          
           −2−2
          
         
         
          
           2+2
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           −4
          
         
         
          
           −20
          
         
         
          
           0
          
         
        
        
         
          
           14
          
         
         
          
           24
          
         
         
          
           14
          
         
        
        
         
          9
         
         
          
           −4
          
         
         
          
           4
          
         
        

       
       ]
     
    
   

  
 

  

Try It
Add matrix 
    
    A
    
   and matrix 
    
    B.
    
  
  
     
 
  A=[ 
   
    
     
      2
     
     
      6
     
    
    
     
      1
     
     
      0
     
    
    
     
      1
     
     
      
−3
      
     
    

   
   ] and  B=[ 
   
    
     
      3
     
     
      
−2
      
     
    
    
     
      1
     
     
      5
     
    
    
     
      
−4
      
     
     
      3
     
    

   
   ]
 

  
    
      A+B=[ 
        
          
            
              2
            
          
          
            
              1
            
          
          
            
              1
            
          

        
          
            
              
                6
              
            
          
          
            
              
                ​​​0
              
            
          
          
            
              
                −3
              
            
          

        
       ]+[ 
        
          
            
              
                3
              
            
          
          
            
              
                1
              
            
          
          
            
              
                −4
              
            
          

        
          
            
              
                −2
              
            
          
          
            
              
                5
              
            
          
          
            
              
                3
              
            
          

        
       ]=[ 
        
          
            
              
                2+3
              
            
          
          
            
              
                1+1
              
            
          
          
            
              
                1+(−4)
              
            
          

        
          
            
              
                6+(−2)
              
            
          
          
            
              
                0+5
              
            
          
          
            
              
                −3+3
              
            
          

        
       ]=[ 
        
          
            
              
                5
              
            
          
          
            
              
                2
              
            
          
          
            
              
                −3
              
            
          

        
          
            
              4
            
          
          
            
              5
            
          
          
            
              0
            
          

        
       ]
  
  
  

  
    Finding Scalar Multiples of a Matrix
    Besides adding and subtracting whole matrices, there are many situations in which we need to multiply a matrix by a constant called a scalar. Recall that a scalar is a real number quantity that has magnitude, but not direction. For example, time, temperature, and distance are scalar quantities. The process of scalar multiplication involves multiplying each entry in a matrix by a scalar. A scalar multiple is any entry of a matrix that results from scalar multiplication.
    Consider a real-world scenario in which a university needs to add to its inventory of computers, computer tables, and chairs in two of the campus labs due to increased enrollment. They estimate that 15% more equipment is needed in both labs. The school’s current inventory is displayed in .

    

        
        

          
            
            Lab A
            Lab B
          

        

          
            Computers
            15
            27
          
          
            Computer Tables
            16
            34
          
          
            Chairs
            16
            34
          
        

Converting the data to a matrix, we have
     
      
        
          C
          
            2013
          
        
        =[ 
          
            
              
                
                  15
                
              
            
            
              
                
                  16
                
              
            
            
              
                
                  16
                
              
            

          
            
              
                
                  27
                
              
            
            
              
                
                  34
                
              
            
            
              
                
                  34
                
              
            

          
         ]
      
    
    
    To calculate how much computer equipment will be needed, we multiply all entries in matrix 
      
        C
      
     by 0.15.
     
      
        (0.15)
          C
          
            2013
          
        
        =[ 
          
            
              
                
                  (0.15)15
                
              
            
            
              
                
                  (0.15)16
                
              
            
            
              
                
                  (0.15)16
                
              
            

          
            
              
                
                  (0.15)27
                
              
            
            
              
                
                  (0.15)34
                
              
            
            
              
                
                  (0.15)34
                
              
            

          
         ]=[ 
          
            
              
                
                  2.25
                
              
            
            
              
                
                  2.4
                
              
            
            
              
                
                  2.4
                
              
            

          
            
              
                
                  4.05
                
              
            
            
              
                
                  5.1
                
              
            
            
              
                
                  5.1
                
              
            

          
         ]
      
    
    
    We must round up to the next integer, so the amount of new equipment needed is
     
      
        [ 
          
            
              
                3
              
            
            
              
                3
              
            
            
              
                3
              
            

          
            
              
                5
              
            
            
              
                6
              
            
            
              
                6
              
            

          
         ]
      
    
    
    Adding the two matrices as shown below, we see the new inventory amounts.
     
      
        [ 
          
            
              
                
                  15
                
              
            
            
              
                
                  16
                
              
            
            
              
                
                  16
                
              
            

          
            
              
                
                  27
                
              
            
            
              
                
                  34
                
              
            
            
              
                
                  34
                
              
            

          
         ]+[ 
          
            
              
                3
              
            
            
              
                3
              
            
            
              
                3
              
            

          
            
              
                5
              
            
            
              
                6
              
            
            
              
                6
              
            

          
         ]=[ 
          
            
              
                
                  18
                
              
            
            
              
                
                  19
                
              
            
            
              
                
                  19
                
              
            

          
            
              
                
                  32
                
              
            
            
              
                
                  40
                
              
            
            
              
                
                  40
                
              
            

          
         ]
      
    
    
    This means
     
      
        
          C
          
            2014
          
        
        =[ 
          
            
              
                
                  18
                
              
            
            
              
                
                  19
                
              
            
            
              
                
                  19
                
              
            

          
            
              
                
                  32
                
              
            
            
              
                
                  40
                
              
            
            
              
                
                  40
                
              
            

          
         ]
      
    
    
    Thus, Lab A will have 18 computers, 19 computer tables, and 19 chairs; Lab B will have 32 computers, 40 computer tables, and 40 chairs.

    

      Scalar Multiplication
      Scalar multiplication involves finding the product of a constant by each entry in the matrix. Given
       
 
  A=[ 
   
    
     
      
       
        a
        
         11
        
       

      
     
     
      
     
     
      
     
     
      
       
        a
        
         12
        
       

      
     
    
    
     
      
       
        a
        
         21
        
       

      
     
     
      
     
     
      
     
     
      
       
        a
        
         22
        
       

      
     
    

   
   ]
 

the scalar multiple 
        
          cA
        
       is
       
 
  
   
    
     
      cA=c[ 
       
        
         
          
           
            a
            
             11
            
           

          
         
         
          
         
         
          
           
            a
            
             12
            
           

          
         
        
        
         
          
           
            a
            
             21
            
           

          
         
         
          
         
         
          
           
            a
            
             22
            
           

          
         
        

       
       ]
     
    
   
   
    
     
         =[ 
       
        
         
          
           c
            a
            
             11
            
           

          
         
         
          
         
         
          
           c
            a
            
             12
            
           

          
         
        
        
         
          
           c
            a
            
             21
            
           

          
         
         
          
         
         
          
           c
            a
            
             22
            
           

          
         
        

       
       ]
     
    
   

  
 

Scalar multiplication is distributive. For the matrices 
        
          A,B,
        
       and 
        
          C
        
       with scalars 
        
          a
        
       and 
        
          b,
        
      
       
 
  
   
    
   
  
  
   
    
     
      
       
        a(A+B)=aA+aB
       
      
     
     
      
       
        (a+b)A=aA+bA
       
      
     

    
   
  
 

    
      
        
          Multiplying the Matrix by a Scalar
          Multiply matrix 
            
              A
            
           by the scalar 3.
           
            
              A=[ 
                
                  
                    
                      8
                    
                    
                      1
                    
                  
                  
                    
                      5
                    
                    
                      4
                    
                  

                
               ]
            
          
          
        
        

          Multiply each entry in 
            
              A
            
           by the scalar 3.
           
 
  
   
    
     
      3A=3[ 
       
        
         
          8
         
         
          
           1
          
         
        
        
         
          5
         
         
          
           4
          
         
        

       
       ]
     
    
   
   
    
     
      = [ 
       
        
         
          
           3⋅8
          
         
         
          
           3⋅1
          
         
        
        
         
          
           3⋅5
          
         
         
          
           3⋅4
          
         
        

       
       ]
     
    
   
   
    
     
      = [ 
       
        
         
          
           24
          
         
         
          3
         
        
        
         
          
           15
          
         
         
          
           12
          
         
        

       
       ]
     
    
   

  
 

        
        

    
      Try It
    
      Given matrix 
        
          B,
        
       find 
        
          −2B
        
       where 
          
            B=[ 
              
                
                  
                    4
                  
                  
                    1
                  
                
                
                  
                    3
                  
                  
                    2
                  
                

              
             ]
          
        
        
       
        
          −2B=[ 
            
              
                
                  
−8
                  
                
                
                  
−2
                  
                
              
              
                
                  
−6
                  
                
                
                  
−4
                  
                
              

            
           ]
        
      
      

    
    
    
      
          Finding the Sum of Scalar Multiples
          Find the sum 
            
              3A+2B.
            
          
          
           
 
  A=[ 
   
    
     
      1
     
     
      
       −2
      
     
     
      0
     
    
    
     
      0
     
     
      
       −1
      
     
     
      2
     
    
    
     
      4
     
     
      3
     
     
      
       −6
      
     
    

   
   ]and B=[ 
   
    
     
      
       −1
      
     
     
      2
     
     
      1
     
    
    
     
      0
     
     
      
       −3
      
     
     
      2
     
    
    
     
      0
     
     
      1
     
     
      
       −4
      
     
    

   
   ]
 

        
        

          First, find 
            
              3A,
            
           then 
            
              2B.
            
          
           
 
  
   
    
     
      
       
        
         
        
       
       
        
         
        
       
       
        
         
          3A=[ 
           
            
             
              
               3⋅1
              
             
             
              
               3(−2)
              
             
             
              
               3⋅0
              
             
            
            
             
              
               3⋅0
              
             
             
              
               3(−1)
              
             
             
              
               3⋅2
              
             
            
            
             
              
               3⋅4
              
             
             
              
               3⋅3
              
             
             
              
               3(−6)
              
             
            

           
           ]
         
        
       

      
     
    
   
   
    
     
      =[ 
       
        
         
          3
         
         
          
           −6
          
         
         
          
           0
          
         
        
        
         
          0
         
         
          
           −3
          
         
         
          
           6
          
         
        
        
         
          
           12
          
         
         
          
           9
          
         
         
          
           −18
          
         
        

       
       ]
     
    
   

  
 

 
 
  
   
    
     
      
       
        
         
        
       
       
        
         
        
       
       
        
         
          2B=[ 
           
            
             
              
               2(−1)
              
             
             
              
               2⋅2
              
             
             
              
               2⋅1
              
             
            
            
             
              
               2⋅0
              
             
             
              
               2(−3)
              
             
             
              
               2⋅2
              
             
            
            
             
              
               2⋅0
              
             
             
              
               2⋅1
              
             
             
              
               2(−4)
              
             
            

           
           ]
         
        
       

      
     
    
   
   
    
     
      =[ 
       
        
         
          
           −2
          
         
         
          4
         
         
          2
         
        
        
         
          0
         
         
          
           −6
          
         
         
          4
         
        
        
         
          0
         
         
          2
         
         
          
           −8
          
         
        

       
       ]
     
    
   

  
 

Now, add 
            
              3A+2B.
            
          
          
 
 
  
   
    
     
    
   
   
    
     
    
   
   
    
     
      3A+2B=[ 
       
        
         
          3
         
         
          
           −6
          
         
         
          0
         
        
        
         
          0
         
         
          
           −3
          
         
         
          6
         
        
        
         
          
           12
          
         
         
          9
         
         
          
           −18
          
         
        

       
       ]+[ 
       
        
         
          
           −2
          
         
         
          4
         
         
          2
         
        
        
         
          0
         
         
          
           −6
          
         
         
          4
         
        
        
         
          0
         
         
          2
         
         
          
           −8
          
         
        

       
       ]
     
    
   
   
    
     
                  =[ 
       
        
         
          
           3−2
          
         
         
          
           −6+4
          
         
         
          
           0+2
          
         
        
        
         
          
           0+0
          
         
         
          
           −3−6
          
         
         
          
           6+4
          
         
        
        
         
          
           12+0
          
         
         
          
           9+2
          
         
         
          
           −18−8
          
         
        

       
       ]
     
    
   
   
    
     
                  =[ 
       
        
         
          1
         
         
          
           −2
          
         
         
          2
         
        
        
         
          0
         
         
          
           −9
          
         
         
          
           10
          
         
        
        
         
          
           12
          
         
         
          
           11
          
         
         
          
           −26
          
         
        

       
       ]
     
    
   

  
 

      
  

  Finding the Product of Two MatricesIn addition to multiplying a matrix by a scalar, we can multiply two matrices. Finding the product of two matrices is only possible when the inner dimensions are the same, meaning that the number of columns of the first matrix is equal to the number of rows of the second matrix. If 
      
        A
      
     is an 
 
  m×r
 
 matrix and 
      
        B
      
     is an 
 
  r×n
 
 matrix, then the product matrix 
      
        AB
      
     is an 
 
  m×n
 
 matrix. For example, the product 
      
        AB
      
     is possible because the number of columns in 
      
        A
      
     is the same as the number of rows in 
      
        B.
      
     If the inner dimensions do not match, the product is not defined.

We multiply entries of 
      
        A
      
     with entries of 
      
        B
      
     according to a specific pattern as outlined below. The process of matrix multiplication becomes clearer when working a problem with real numbers.
    To obtain the entries in row 
      
        i
      
     of 
      
        AB,
      
     we multiply the entries in row 
      
        i
      
     of 
      
        A
      
     by column 
      
        j
      
     in 
      
        B
      
     and add. For example, given matrices 
      
        A
      
     and 
      
        B,
      
     where the dimensions of 
      
        A
      
     are 
      
        2×3
      
     and the dimensions of 
      
        B
      
     are 
      
        3×3,
      
     the product of 
      
        AB
      
     will be a 
      
        2×3
      
     matrix. 
 
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
        
       

      
     
    

   
   ]and B=[ 
   
    
     
      
       
        b
        
         11
        
       

      
     
     
      
       
        b
        
         12
        
       

      
     
     
      
       
        b
        
         13
        
       

      
     
    
    
     
      
       
        b
        
         21
        
       

      
     
     
      
       
        b
        
         22
        
       

      
     
     
      
       
        b
        
         23
        
       

      
     
    
    
     
      
       
        b
        
         31
        
       

      
     
     
      
       
        b
        
         32
        
       

      
     
     
      
       
        b
        
         33
        
       

      
     
    

   
   ]
 

Multiply and add as follows to obtain the first entry of the product matrix 
      
        AB.
      
    
    
    To obtain the entry in row 1, column 1 of 
        
          AB,
        
       multiply the first row in 
        
          A
        
       by the first column in 
        
          B,
        
       and add.
         
          
            [ 
              
                
                  
                    
                      
                        a
                        
                          11
                        
                      

                    
                  
                  
                    
                      
                        a
                        
                          12
                        
                      

                    
                  
                  
                    
                      
                        a
                        
                          13
                        
                      

                    
                  
                

              
             ][ 
              
                
                  
                    
                      
                        b
                        
                          11
                        
                      

                    
                  
                
                
                  
                    
                      
                        b
                        
                          21
                        
                      

                    
                  
                
                
                  
                    
                      
                        b
                        
                          31
                        
                      

                    
                  
                

              
             ]=
              a
              
                11
              
            
            ⋅
              b
              
                11
              
            
            +
              a
              
                12
              
            
            ⋅
              b
              
                21
              
            
            +
              a
              
                13
              
            
            ⋅
              b
              
                31
              
            

          
        
        
      To obtain the entry in row 1, column 2 of 
        
          AB,
        
       multiply the first row of 
        
          A
        
       by the second column in 
        
          B,
        
       and add.
         
          
            [ 
              
                
                  
                    
                      
                        a
                        
                          11
                        
                      

                    
                  
                  
                    
                      
                        a
                        
                          12
                        
                      

                    
                  
                  
                    
                      
                        a
                        
                          13
                        
                      

                    
                  
                

              
             ][ 
              
                
                  
                    
                      
                        b
                        
                          12
                        
                      

                    
                  
                
                
                  
                    
                      
                        b
                        
                          22
                        
                      

                    
                  
                
                
                  
                    
                      
                        b
                        
                          32
                        
                      

                    
                  
                

              
             ]=
              a
              
                11
              
            
            ⋅
              b
              
                12
              
            
            +
              a
              
                12
              
            
            ⋅
              b
              
                22
              
            
            +
              a
              
                13
              
            
            ⋅
              b
              
                32
              
            
          
        
        
      To obtain the entry in row 1, column 3 of 
        
          AB,
        
       multiply the first row of 
        
          A
        
       by the third column in 
        
          B,
        
       and add.
         
          
            [ 
              
                
                  
                    
                      
                        a
                        
                          11
                        
                      

                    
                  
                  
                    
                      
                        a
                        
                          12
                        
                      

                    
                  
                  
                    
                      
                        a
                        
                          13
                        
                      

                    
                  
                

              
             ][ 
              
                
                  
                    
                      
                        b
                        
                          13
                        
                      

                    
                  
                
                
                  
                    
                      
                        b
                        
                          23
                        
                      

                    
                  
                
                
                  
                    
                      
                        b
                        
                          33
                        
                      

                    
                  
                

              
             ]=
              a
              
                11
              
            
            ⋅
              b
              
                13
              
            
            +
              a
              
                12
              
            
            ⋅
              b
              
                23
              
            
            +
              a
              
                13
              
            
⋅
           
              b
              
                33
              
            

          
        
        
    We proceed the same way to obtain the second row of 
      
        AB.
      
     In other words, row 2 of 
      
        A
      
     times column 1 of 
      
        B;
      
     row 2 of 
      
        A
      
     times column 2 of 
      
        B;
      
     row 2 of 
      
        A
      
     times column 3 of 
      
        B.
      
     When complete, the product matrix will be
     
 
  AB=[ 
   
    
     
      
       
        
         
          a
          
           11
          
         
         ⋅
          b
          
           11
          
         
         +
          a
          
           12
          
         
         ⋅
          b
          
           21
          
         
         +
          a
          
           13
          
         
         ⋅
          b
          
           31
          
         

        
       
       
        
         
        
       
      

     
    
    
     
      
       
        a
        
         21
        
       
       ⋅
        b
        
         11
        
       
       +
        a
        
         22
        
       
       ⋅
        b
        
         21
        
       
       +
        a
        
         23
        
       
       ⋅
        b
        
         31
        
       

      
     
    

   
    
     
      
       
        
         
          a
          
           11
          
         
         ⋅
          b
          
           12
          
         
         +
          a
          
           12
          
         
         ⋅
          b
          
           22
          
         
         +
          a
          
           13
          
         
         ⋅
          b
          
           32
          
         

        
       
       
        
         
        
       
      

     
    
    
     
      
       
        a
        
         21
        
       
       ⋅
        b
        
         12
        
       
       +
        a
        
         22
        
       
       ⋅
        b
        
         22
        
       
       +
        a
        
         23
        
       
       ⋅
        b
        
         32
        
       

      
     
    

   
    
     
      
       
        
         
          a
          
           11
          
         
         ⋅
          b
          
           13
          
         
         +
          a
          
           12
          
         
         ⋅
          b
          
           23
          
         
         +
          a
          
           13
          
         
         ⋅
          b
          
           33
          
         

        
       
       
        
         
        
       
      

     
    
    
     
      
       
        a
        
         21
        
       
       ⋅
        b
        
         13
        
       
       +
        a
        
         22
        
       
       ⋅
        b
        
         23
        
       
       +
        a
        
         23
        
       
       ⋅
        b
        
         33
        
       

      
     
    

   
   ]
 

    

      Properties of Matrix Multiplication
      For the matrices 
        
          A,B,
        
       and 
        
          C
        
       the following properties hold.Matrix multiplication is associative: 
          
            (
              
                AB
              
              )C=A(
                
                  BC
                
                ).
          
        
        
        Matrix multiplication is distributive: 
 
  
   
    
     
      
       
        
       
      
      
       
        C(A+B)=CA+CB,
       
      
     

    
   
   
    
     
      (A+B)C=AC+BC.
     
    
   

  
 

      Note that matrix multiplication is not commutative.
  

    
      
          Multiplying Two Matrices
          Multiply matrix 
            
              A
            
           and matrix 
            
              B.
            
          
          
           
 
  A=[ 
   
    
     
      1
     
     
      2
     
    
    
     
      3
     
     
      4
     
    

   
   ] and  B=[ 
   
    
     
      5
     
     
      6
     
    
    
     
      7
     
     
      8
     
    

   
   ]
 

        
        

        First, we check the dimensions of the matrices. Matrix 
          
            A          
         has dimensions 
          
            2×2          
         and matrix 
          
            B          
         has dimensions 
          
            2×2.          
         The inner dimensions are the same so we can perform the multiplication. The product will have the dimensions 
          
            2×2.
          
        
        We perform the operations outlined previously.

            
          

       

    
      
          Multiplying Two Matrices
          Given 
            
              A
            
           and 
            
              B:
            
          
          
          
ⓐ
Find 
              
                AB.
              
            
            
            ⓑ
Find 
              
                BA.
              
            
            
           
 
  A=[ 
   
    
     
      
       
        
         
          
           −1
          
         
         
          2
         
         
          3
         
        

       
      
     
    
    
     
      
       
        
         
          
           4
          
         
         
          0
         
         
          5
         
        

       
      
     
    

   
   ]and  B=[ 
   
    
     
      
       5
      
     
    
    
     
      
       −4
      
     
    
    
     
      
       2
      
     
    

   
    
     
      
       −1
      
     
    
    
     
      
       0
      
     
    
    
     
      
       3
      
     
    

   
   ]
 

        

        
ⓐAs the dimensions of 
 
  A
 
 are 
 
  2×3
 
 and the dimensions of 
 
  B
 
 are 
 
  3×2,
 
 these matrices can be multiplied together because the number of columns in 
 
  A
 
 matches the number of rows in 
 
  B.
 
 The resulting product will be a 
 
  2×2
 
 matrix, the number of rows in 
 
  A
 
 by the number of columns in 
 
  B.
 

         
 
  
   
    
     
    
   
   
    
     
      AB=[ 
       
        
         
          
           −1
          
         
         
          2
         
         
          3
         
        
        
         
          4
         
         
          0
         
         
          5
         
        

       
       ]  [ 
       
        
         
          5
         
         
          
           −1
          
         
        
        
         
          
           −4
          
         
         
          0
         
        
        
         
          2
         
         
          3
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           −1(5)+2(−4)+3(2)
          
         
         
          
           −1(−1)+2(0)+3(3)
          
         
        
        
         
          
           4(5)+0(−4)+5(2)
          
         
         
          
           4(−1)+0(0)+5(3)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           −7
          
         
         
          
           10
          
         
        
        
         
          
           30
          
         
         
          
           11
          
         
        

       
       ]
     
    
   

  
 

        ⓑThe dimensions of 
 
  B
 
 are 
 
  3 × 2
 
 and the dimensions of 
 
  A
 
 are 
 
  2 × 3.
 
 The inner dimensions match so the product is defined and will be a 
 
  3 × 3
 
 matrix.
         
 
  
   
    
     
    
   
   
    
     
      BA=[ 
       
        
         
          5
         
         
          
           −1
          
         
        
        
         
          
           −4
          
         
         
          0
         
        
        
         
          2
         
         
          3
         
        

       
       ]  [ 
       
        
         
          
           −1
          
         
         
          2
         
         
          3
         
        
        
         
          4
         
         
          0
         
         
          5
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           5(−1)+−1(4)
          
         
         
          
           5(2)+−1(0)
          
         
         
          
           5(3)+−1(5)
          
         
        
        
         
          
           −4(−1)+0(4)
          
         
         
          
           −4(2)+0(0)
          
         
         
          
           −4(3)+0(5)
          
         
        
        
         
          
           2(−1)+3(4)
          
         
         
          
           2(2)+3(0)
          
         
         
          
           2(3)+3(5)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           −9
          
         
         
          
           10
          
         
         
          
           10
          
         
        
        
         
          4
         
         
          
           −8
          
         
         
          
           −12
          
         
        
        
         
          
           10
          
         
         
          4
         
         
          
           21
          
         
        

       
       ]
     
    
   

  
 

        
          Analysis 
          Notice that the products 
 
  AB
 
 and 
 
  BA
 
 are not equal.
           
 
  AB=[ 
   
    
     
      
       −7
      
     
     
      
       10
      
     
    
    
     
      
       30
      
     
     
      
       11
      
     
    

   
   ]≠[ 
   
    
     
      
       −9
      
     
     
      
       10
      
     
     
      
       10
      
     
    
    
     
      4
     
     
      
       −8
      
     
     
      
       −12
      
     
    
    
     
      
       10
      
     
     
      4
     
     
      
       21
      
     
    

   
   ]=BA
 

          This illustrates the fact that matrix multiplication is not commutative.

      

    
      Q&A
      Is it possible for AB to be defined but not BA?
      Yes, consider a matrix A with dimension 
 
  3×4
 
 and matrix B with dimension 
 
  4×2.
 
 For the product AB the inner dimensions are 4 and the product is defined, but for the product BA the inner dimensions are 2 and 3 so the product is undefined.

    
      
        
          Using Matrices in Real-World Problems
          Let’s return to the problem presented at the opening of this section. We have , representing the equipment needs of two soccer teams.

          

  
  Wildcats
  Mud Cats

  Goals
  6
  10

  Balls
  30
  24

  Jerseys
  14
  20

We are also given the prices of the equipment, as shown in .
         

Goal
$300

Ball
$10

Jersey
$30

We will convert the data to matrices. Thus, the equipment need matrix is written as
           
 
  E=[ 
   
    
     
      6
     
    
    
     
      
       30
      
     
    
    
     
      
       14
      
     
    

   
    
     
      
       10
      
     
    
    
     
      
       24
      
     
    
    
     
      
       20
      
     
    

   
   ]
 

          The cost matrix is written as
           
 
  C=[ 
   
    
     
      
       300
      
     
     
      
       10
      
     
     
      
       30
      
     
    

   
   ]
 

          We perform matrix multiplication to obtain costs for the equipment. 
 
  
   
    
     
    
   
   
    
     
    
   
   
    
     
      CE=[ 
       
        
         
          
           300
          
         
         
          
           10
          
         
         
          
           30
          
         
        

       
       ][ 
       
        
         
          6
         
         
          
           10
          
         
        
        
         
          
           30
          
         
         
          
           24
          
         
        
        
         
          
           14
          
         
         
          
           20
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           300(6)+10(30)+30(14)
          
         
         
          
           300(10)+10(24)+30(20)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           2,520
          
         
         
          
           3,840
          
         
        

       
       ]
     
    
   

  
 

The total cost for equipment for the Wildcats is $2,520, and the total cost for equipment for the Mud Cats is $3,840.

      
    

    
      How To
      Given a matrix operation, evaluate using a calculator.
      
Save each matrix as a matrix variable 
 
  [ A ],[ B ],[ C ],...
 

      Enter the operation into the calculator, calling up each matrix variable as needed.
      If the operation is defined, the calculator will present the solution matrix; if the operation is undefined, it will display an error message.

    
      
        
          Using a Calculator to Perform Matrix Operations
          Find 
 
  AB−C
 

given
           
 
  A=[ 
   
    
     
      
       −15
      
     
     
      
       25
      
     
     
      
       32
      
     
    
    
     
      
       41
      
     
     
      
       −7
      
     
     
      
       −28
      
     
    
    
     
      
       10
      
     
     
      
       34
      
     
     
      
       −2
      
     
    

   
   ],B=[ 
   
    
     
      
       45
      
     
     
      
       21
      
     
     
      
       −37
      
     
    
    
     
      
       −24
      
     
     
      
       52
      
     
     
      
       19
      
     
    
    
     
      6
     
     
      
       −48
      
     
     
      
       −31
      
     
    

   
   ],and C=[ 
   
    
     
      
       −100
      
     
     
      
       −89
      
     
     
      
       −98
      
     
    
    
     
      
       25
      
     
     
      
       −56
      
     
     
      
       74
      
     
    
    
     
      
       −67
      
     
     
      
       42
      
     
     
      
       −75
      
     
    

   
   ].
 

        
          On the matrix page of the calculator, we enter matrix 
 
  A
 
 above as the matrix variable 
 
  [ A ],
 
 matrix 
 
  B
 
 above as the matrix variable 
 
  [ B ],
 
 and matrix 
 
  C
 
 above as the matrix variable 
 
  [ C ].
 

        On the home screen of the calculator, we type in the problem and call up each matrix variable as needed.
         
 
  
[
A
]

[
B
]

−

[
C
]

 

The calculator gives us the following matrix.
         
 
  [ 
   
    
     
      
       −983
      
     
     
      
       −462
      
     
     
      
       136
      
     
    
    
     
      
       1,820
      
     
     
      
       1,897
      
     
     
      
       −856
      
     
    
    
     
      
       −311
      
     
     
      
       2,032
      
     
     
      
       413
      
     
    

   
   ]
 

        
        

    Media
      Access these online resources for additional instruction and practice with matrices and matrix operations.

     Dimensions of a Matrix
        Matrix Addition and Subtraction
          Matrix Operations
            Matrix Multiplication
    

Key ConceptsA matrix is a rectangular array of numbers. Entries are arranged in rows and columns.
The dimensions of a matrix refer to the number of rows and the number of columns. A 
 
  3×2
 
 matrix has three rows and two columns. See .
We add and subtract matrices of equal dimensions by adding and subtracting corresponding entries of each matrix. See , , , and .
Scalar multiplication involves multiplying each entry in a matrix by a constant. See .
Scalar multiplication is often required before addition or subtraction can occur. See .
Multiplying matrices is possible when inner dimensions are the same—the number of columns in the first matrix must match the number of rows in the second.
The product of two matrices, 
 
  A
 
 and 
 
  B,
 
 is obtained by multiplying each entry in row 1 of 
 
  A
 
 by each entry in column 1 of 
 
  B;
 
 then multiply each entry of row 1 of 
 
  A
 
 by each entry in columns 2 of 
 
  B,
 
 and so on. See  and .
Many real-world problems can often be solved using matrices. See .
We can use a calculator to perform matrix operations after saving each matrix as a matrix variable. See .

Section Exercises
Verbal

Can we add any two matrices together? If so, explain why; if not, explain why not and give an example of two matrices that cannot be added together.

No, they must have the same dimensions. An example would include two matrices of different dimensions.  One cannot add the following two matrices because the first is a 
 
  2×2
 
 matrix and the second is a 
 
  2×3
 
 matrix. 
 
  [ 
   
    
     
      1
     
     
      2
     
    
    
     
      3
     
     
      4
     
    

   
   ]+[ 
   
    
     
      6
     
     
      5
     
     
      4
     
    
    
     
      3
     
     
      2
     
     
      1
     
    

   
   ]
 
 has no sum.

Can we multiply any column matrix by any row matrix? Explain why or why not.
Can both the products 
 
  AB
 
 and 
 
  BA
 
 be defined? If so, explain how; if not, explain why.

Yes, if the dimensions of 
 
  A
 
 are 
 
  m×n
 
 and the dimensions of 
 
  B
 
 are 
 
  n×m,
 
 both products will be defined. 
Can any two matrices of the same size be multiplied? If so, explain why, and if not, explain why not and give an example of two matrices of the same size that cannot be multiplied together.
Does matrix multiplication commute? That is, does 
 
  AB=BA?
 
 If so, prove why it does. If not, explain why it does not.

Not necessarily. To find 
 
  AB,
 
 we multiply the first row of 
 
  A
 
 by the first column of 
 
  B
 
 to get the first entry of 
 
  AB.
 
 To find 
 
  BA,
 
 we multiply the first row of 
 
  B
 
 by the first column of 
 
  A
 
 to get the first entry of 
 
  BA.
 
 Thus, if those are unequal, then the matrix multiplication does not commute. 

Algebraic
For the following exercises, use the matrices below and perform the matrix addition or subtraction. Indicate if the operation is undefined.
 
 
  A=[ 
   
    
     
      1
     
     
      3
     
    
    
     
      0
     
     
      7
     
    

   
   ],B=[ 
   
    
     
      2
     
     
      
       14
      
     
    
    
     
      
       22
      
     
     
      6
     
    

   
   ],C=[ 
   
    
     
      1
     
     
      5
     
    
    
     
      8
     
     
      
       92
      
     
    
    
     
      
       12
      
     
     
      6
     
    

   
   ],D=[ 
   
    
     
      
       10
      
     
     
      
       14
      
     
    
    
     
      7
     
     
      2
     
    
    
     
      5
     
     
      
       61
      
     
    

   
   ],E=[ 
   
    
     
      6
     
     
      
       12
      
     
    
    
     
      
       14
      
     
     
      5
     
    

   
   ],F=[ 
   
    
     
      0
     
     
      9
     
    
    
     
      
       78
      
     
     
      
       17
      
     
    
    
     
      
       15
      
     
     
      4
     
    

   
   ]
 

 
 
  A+B
 

 
 
  C+D
 

 
 
  [ 
   
    
     
      
       11
      
     
     
      
       19
      
     
    
    
     
      
       15
      
     
     
      
       94
      
     
    
    
     
      
       17
      
     
     
      
       67
      
     
    

   
   ]
 

 
 
  A+C
 

 
 
  B−E
 

 
 
  [ 
   
    
     
      
       −4
      
     
     
      2
     
    
    
     
      8
     
     
      1
     
    

   
   ]
 

 
 
  C+F
 

 
 
  D−B
 

Undidentified; dimensions do not match 

For the following exercises, use the matrices below to perform scalar multiplication.
 
 
  A=[ 
   
    
     
      4
     
     
      6
     
    
    
     
      
       13
      
     
     
      
       12
      
     
    

   
   ],B=[ 
   
    
     
      3
     
     
      9
     
    
    
     
      
       21
      
     
     
      
       12
      
     
    
    
     
      0
     
     
      
       64
      
     
    

   
   ],C=[ 
   
    
     
      
       16
      
     
     
      3
     
     
      7
     
     
      
       18
      
     
    
    
     
      
       90
      
     
     
      5
     
     
      3
     
     
      
       29
      
     
    

   
   ],D=[ 
   
    
     
      
       18
      
     
     
      
       12
      
     
     
      
       13
      
     
    
    
     
      8
     
     
      
       14
      
     
     
      6
     
    
    
     
      7
     
     
      4
     
     
      
       21
      
     
    

   
   ]
 

 
 
  5A
 

 
 
  3B
 

 
 
  [ 
   
    
     
      9
     
     
      
       27
      
     
    
    
     
      
       63
      
     
     
      
       36
      
     
    
    
     
      0
     
     
      
       192
      
     
    

   
   ]
 

 
 
  −2B
 

 
 
  −4C
 

 
 
  [ 
   
    
     
      
       −64
      
     
     
      
       −12
      
     
     
      
       −28
      
     
     
      
       −72
      
     
    
    
     
      
       −360
      
     
     
      
       −20
      
     
     
      
       −12
      
     
     
      
       −116
      
     
    

   
   ]
 

 
 
  
   1
   2
  
  C
 

 
 
  100D
 

 
 
  [ 
   
    
     
      
       1,800
      
     
     
      
       1,200
      
     
     
      
       1,300
      
     
    
    
     
      
       800
      
     
     
      
       1,400
      
     
     
      
       600
      
     
    
    
     
      
       700
      
     
     
      
       400
      
     
     
      
       2,100
      
     
    

   
   ]
 

For the following exercises, use the matrices below to perform matrix multiplication.
 
 
  A=[ 
   
    
     
      
       −1
      
     
     
      5
     
    
    
     
      3
     
     
      2
     
    

   
   ],B=[ 
   
    
     
      3
     
     
      6
     
     
      4
     
    
    
     
      
       −8
      
     
     
      0
     
     
      
       12
      
     
    

   
   ],C=[ 
   
    
     
      4
     
     
      
       10
      
     
    
    
     
      
       −2
      
     
     
      6
     
    
    
     
      5
     
     
      9
     
    

   
   ],D=[ 
   
    
     
      2
     
     
      
       −3
      
     
     
      
       12
      
     
    
    
     
      9
     
     
      3
     
     
      1
     
    
    
     
      0
     
     
      8
     
     
      
       −10
      
     
    

   
   ]
 

 
 
  AB
 

 
 
  BC
 
 

 
 
  [ 
   
    
     
      
       20
      
     
     
      
       102
      
     
    
    
     
      
       28
      
     
     
      
       28
      
     
    

   
   ]
 

 
 
  CA
 
 
 
 
  BD
 
 

 
 
  [ 
   
    
     
      
       60
      
     
     
      
       41
      
     
     
      2
     
    
    
     
      
       −16
      
     
     
      
       120
      
     
     
      
       −216
      
     
    

   
   ]
 

 
 
  DC
 
 
 
 
  CB
 
 

 
 
  [ 
   
    
     
      
       −68
      
     
     
      
       24
      
     
     
      
       136
      
     
    
    
     
      
       −54
      
     
     
      
       −12
      
     
     
      
       64
      
     
    
    
     
      
       −57
      
     
     
      
       30
      
     
     
      
       128
      
     
    

   
   ]
 

For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed.
 
 
  A=[ 
   
    
     
      2
     
     
      
       −5
      
     
    
    
     
      6
     
     
      7
     
    

   
   ],B=[ 
   
    
     
      
       −9
      
     
     
      6
     
    
    
     
      
       −4
      
     
     
      2
     
    

   
   ],C=[ 
   
    
     
      0
     
     
      9
     
    
    
     
      7
     
     
      1
     
    

   
   ],D=[ 
   
    
     
      
       −8
      
     
     
      7
     
     
      
       −5
      
     
    
    
     
      4
     
     
      3
     
     
      2
     
    
    
     
      0
     
     
      9
     
     
      2
     
    

   
   ],E=[ 
   
    
     
      4
     
     
      5
     
     
      3
     
    
    
     
      7
     
     
      
       −6
      
     
     
      
       −5
      
     
    
    
     
      1
     
     
      0
     
     
      9
     
    

   
   ]
 

 
 
  A+B−C
 

 
 
  4A+5D
 

Undefined; dimensions do not match. 

 
 
  2C+B
 

 
 
  3D+4E
 

 
 
  [ 
   
    
     
      
       −8
      
     
     
      
       41
      
     
     
      
       −3
      
     
    
    
     
      
       40
      
     
     
      
       −15
      
     
     
      
       −14
      
     
    
    
     
      4
     
     
      
       27
      
     
     
      
       42
      
     
    

   
   ]
 

 
 
  C−0.5D
 

 
 
  100D−10E
 

 
 
  [ 
   
    
     
      
       −840
      
     
     
      
       650
      
     
     
      
       −530
      
     
    
    
     
      
       330
      
     
     
      
       360
      
     
     
      
       250
      
     
    
    
     
      
       −10
      
     
     
      
       900
      
     
     
      
       110
      
     
    

   
   ]
 

For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. (Hint: 
 
  
   A
   2
  
  =A⋅A
 

)

 
 
  A=[ 
   
    
     
      
       −10
      
     
     
      
       20
      
     
    
    
     
      5
     
     
      
       25
      
     
    

   
   ],B=[ 
   
    
     
      
       40
      
     
     
      
       10
      
     
    
    
     
      
       −20
      
     
     
      
       30
      
     
    

   
   ],C=[ 
   
    
     
      
       −1
      
     
     
      0
     
    
    
     
      0
     
     
      
       −1
      
     
    
    
     
      1
     
     
      0
     
    

   
   ]
 

 
 
  AB
 

 
 
  BA
 
 

 
 
  [ 
   
    
     
      
       −350
      
     
     
      
       1,050
      
     
    
    
     
      
       350
      
     
     
      
       350
      
     
    

   
   ]
 

 
 
  CA
 

 
 
  BC
 

 Undefined; inner dimensions do not match. 

 
 
  
   A
   2
  

 

 
 
  
   B
   2
  

 

 
 
  [ 
   
    
     
      
       1,400
      
     
     
      
       700
      
     
    
    
     
      
       −1,400
      
     
     
      
       700
      
     
    

   
   ]
 

 
 
  
   C
   2
  

 

 
 
  
   B
   2
  
  
   A
   2
  

 

 
 
  [ 
   
    
     
      
       332,500
      
     
     
      
       927,500
      
     
    
    
     
      
       −227,500
      
     
     
      
       87,500
      
     
    

   
   ]
 

 
 
  
   A
   2
  
  
   B
   2
  

 

 
 
  
   
    (AB)
   
   2
  

 

 
 
  [ 
   
    
     
      
       490,000
      
     
     
      0
     
    
    
     
      0
     
     
      
       490,000
      
     
    

   
   ]
 

 
 
  
   
    (BA)
   
   2
  

 

For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. (Hint: 
 
  
   A
   2
  
  =A⋅A
 

)
 
 
  A=[ 
   
    
     
      1
     
     
      0
     
    
    
     
      2
     
     
      3
     
    

   
   ],B=[ 
   
    
     
      
       −2
      
     
     
      3
     
     
      4
     
    
    
     
      
       −1
      
     
     
      1
     
     
      
       −5
      
     
    

   
   ],C=[ 
   
    
     
      
       0.5
      
     
     
      
       0.1
      
     
    
    
     
      1
     
     
      
       0.2
      
     
    
    
     
      
       −0.5
      
     
     
      
       0.3
      
     
    

   
   ],D=[ 
   
    
     
      1
     
     
      0
     
     
      
       −1
      
     
    
    
     
      
       −6
      
     
     
      7
     
     
      5
     
    
    
     
      4
     
     
      2
     
     
      1
     
    

   
   ]
 

 
 
  AB
 

 
 
  [ 
   
    
     
      
       −2
      
     
     
      3
     
     
      4
     
    
    
     
      
       −7
      
     
     
      9
     
     
      
       −7
      
     
    

   
   ]
 

 
 
  BA
 

 
 
  BD
 

 
 
  [ 
   
    
     
      
       −4
      
     
     
      
       29
      
     
     
      
       21
      
     
    
    
     
      
       −27
      
     
     
      
       −3
      
     
     
      1
     
    

   
   ]
 

 
 
  DC
 

 
 
  
   D
   2
  

 

 
 
  [ 
   
    
     
      
       −3
      
     
     
      
       −2
      
     
     
      
       −2
      
     
    
    
     
      
       −28
      
     
     
      
       59
      
     
     
      
       46
      
     
    
    
     
      
       −4
      
     
     
      
       16
      
     
     
      7
     
    

   
   ]
 

 
 
  
   A
   2
  

 

 
 
  
   D
   3
  

 

 
 
  [ 
   
    
     
      1
     
     
      
       −18
      
     
     
      
       −9
      
     
    
    
     
      
       −198
      
     
     
      
       505
      
     
     
      
       369
      
     
    
    
     
      
       −72
      
     
     
      
       126
      
     
     
      
       91
      
     
    

   
   ]
 

 
 
  (AB)C
 

 
 
  A(BC)
 

 
 
  [ 
   
    
     
      0
     
     
      
       1.6
      
     
    
    
     
      9
     
     
      
       −1
      
     
    

   
   ]
 

Technology
For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. Use a calculator to verify your solution.
 
 
  A=[ 
   
    
     
      
       −2
      
     
     
      0
     
     
      9
     
    
    
     
      1
     
     
      8
     
     
      
       −3
      
     
    
    
     
      
       0.5
      
     
     
      4
     
     
      5
     
    

   
   ],B=[ 
   
    
     
      
       0.5
      
     
     
      3
     
     
      0
     
    
    
     
      
       −4
      
     
     
      1
     
     
      6
     
    
    
     
      8
     
     
      7
     
     
      2
     
    

   
   ],C=[ 
   
    
     
      1
     
     
      0
     
     
      1
     
    
    
     
      0
     
     
      1
     
     
      0
     
    
    
     
      1
     
     
      0
     
     
      1
     
    

   
   ]
 

 
 
  AB
 

 
 
  BA
 

 
 
  [ 
   
    
     
      2
     
     
      
       24
      
     
     
      
       −4.5
      
     
    
    
     
      
       12
      
     
     
      
       32
      
     
     
      
       −9
      
     
    
    
     
      
       −8
      
     
     
      
       64
      
     
     
      
       61
      
     
    

   
   ]
 

 
 
  CA
 

 
 
  BC
 

 
 
  [ 
   
    
     
      
       0.5
      
     
     
      3
     
     
      
       0.5
      
     
    
    
     
      2
     
     
      1
     
     
      2
     
    
    
     
      
       10
      
     
     
      7
     
     
      
       10
      
     
    

   
   ]
 

 
 
  ABC
 

Extensions
For the following exercises, use the matrix below to perform the indicated operation on the given matrix.
 
 
  B=[ 
   
    
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      1
     
    
    
     
      0
     
     
      1
     
     
      0
     
    

   
   ]
 

 
 
  
   B
   2
  

 

 
 
  [ 
   
    
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      1
     
    

   
   ]
 

 
 
  
   B
   3
  

 

 
 
  
   B
   4
  

 

 
 
  [ 
   
    
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      1
     
    

   
   ]
 

 
 
  
   B
   5
  

 

Using the above questions, find a formula for 
 
  
   B
   n
  
  .
 
 Test the formula for 
 
  
   B
   
    201
   
  

 
 and 
 
  
   B
   
    202
   
  
  ,
 
 using a calculator.

 
 
  
   B
   n
  
  ={ 
   
    
     [ 
      
       
        
         1
        
        
         0
        
        
         0
        
       
       
        
         0
        
        
         1
        
        
         0
        
       
       
        
         0
        
        
         0
        
        
         1
        
       

      
      ], neven,
    
   
   
    
     [ 
      
       
        
         1
        
        
         0
        
        
         0
        
       
       
        
         0
        
        
         0
        
        
         1
        
       
       
        
         0
        
        
         1
        
        
         0
        
       

      
      ], nodd.
    
   
  
   
 

column a set of numbers aligned vertically in a matrix

entry an element, coefficient, or constant in a matrix

matrix a rectangular array of numbers

row a set of numbers aligned horizontally in a matrix
scalar multiple an entry of a matrix that has been multiplied by a scalar
