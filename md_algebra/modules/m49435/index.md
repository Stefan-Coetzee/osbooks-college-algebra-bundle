Solving Systems with Inverses

  m49435
  Solving Systems with Inverses
  In this section, you will:
Find the inverse of a matrix.
Solve a system of linear equations using an inverse matrix.

  634d2387-7429-480f-a04e-867c2f9699fb

  Learning Objectives
Evaluate the determinant of a 2×2 matrix (IA 4.6.1)
Evaluate the determinant of a 3x3 matrix (IA 4.6.2)

Objective 1: Evaluate the determinant of a 2×2 matrix (IA 4.6.1)If a matrix has the same number of rows and columns, we call it a square matrix. Each square matrix has a real number associated with it called its determinant.
DeterminantThe determinant of any square matrix abcd , where a, b, c, and d are real numbers, is abcd=ad-bc To get the real number value of the determinate we subtract the products of the diagonals, as shown.
 
    
  
  
Find the determinant of the 2x2 matrix 4-23-1
  

  
    Write the determinant
     
    
  
  
  
    Subtract the products of the diagonals
     4(-1)-3(-2) 
  
  
    Simplify
     -4+62 
  

Practice Makes Perfect
Find the determinant of the 2x2 matrices.

  
 6-23-1
  

  
 -48-35
  
Objective 2: Evaluate the determinant of a 3×3 matrix (IA 4.6.2)To evaluate the determinant of a 3×3 matrix, we must be able to evaluate the minor of an entry in the determinant.
The minor of an entry is the 2×2 determinant found by eliminating the row and column in the 3×3 determinant that contains the entry.
For example, to find the minor of entry a1, we eliminate the row and column which contain it. So, we eliminate the first row and first column. Then we write the 2×2 determinant that remains.

    
  
To find the minor of entry b2, we eliminate the row and column that contain it. So, we eliminate the second row and second column. Then we write the 2×2 determinant that remains.

    
  

For the determinant |4−2310−3−2−42|, find and then evaluate the minor of ⓐ a1 ⓑ b3 

ⓐ

Eliminate the row and column that contains a1. 

Write the 2×2 determinant that remains.

Evaluate.

Simplify.

ⓑ

Eliminate the row and column that contains b3. 

Write the 2×2 determinant that remains.

Evaluate.

Simplify.

For the following determinant, find and then evaluate the minor of c2

 4-2310-3-2-42 

Eliminate the row and column that contains c2. 

Write the 2×2 determinant that remains.

Evaluate and simplify.
________________________________________

Strategy for evaluating the determinant of a 3x3 matrix
To evaluate a 3×3 determinant we can expand by minors using any row or column. Choosing a row or column other than the first row sometimes makes the work easier.
When we expand by any row or column, we must be careful about the sign of the terms in the expansion. To determine the sign of the terms, we use the following sign pattern chart.
 +-+-+-+-+ 

Expanding by minors along the first row to evaluate a 3x3 determinant.
To evaluate a 3×3 determinant by expanding by minors along the first row, we use the following pattern:

    
  NOTE: We can evaluate the determinant of a matrix by expanding minors along any row or column. When a row or a column has a zero entry, expanding by that row or column results in less calculations.

  
Evaluate the determinant of the 3x3 matrix by expanding by minors along the first row
  
 2-3-1320-1-1-2

Expand by minors along the first row

Evaluate each determinant.

Simplify.

Simplify.

Simplify.

Practice Makes Perfect
  Evaluate the determinant of the 3x3 matrix by expanding by minors along the first row.
 -5-1-440-32-26
  

Soriya plans to invest $10,500 into two different bonds to spread out her risk. The first bond has an annual return of 10%, and the second bond has an annual return of 6%. In order to receive an 8.5% return from the two bonds, how much should Soriya invest in each bond? What is the best method to solve this problem?
  There are several ways we can solve this problem. As we have seen in previous sections, systems of equations and matrices are useful in solving real-world problems involving finance. After studying this section, we will have the tools to solve the bond problem using the inverse of a matrix.

  
    Finding the Inverse of a Matrix
    We know that the multiplicative inverse of a real number 
      
       a
      
     is 
      
       
          a
          
            −1
          
        
        ,
      
     and 
      
       a
          a
          
            −1
          
        
        =
          a
          
            −1
          
        
        a=(
          
            
              1
              a
            

          
          )a=1.
      
     For example, 
      
       
          2
          
            −1
          
        
        =
          1
          2
        

      
     and 
      
       (
          
            
              1
              2
            

          
          )2=1.
      
     The multiplicative inverse of a matrix is similar in concept, except that the product of matrix 
      
A
      
     and its inverse 
      
       
          A
          
            −1
          
        

      
     equals the identity matrix. The identity matrix is a square matrix containing ones down the main diagonal and zeros everywhere else. We identify identity matrices by 
      
       
          I
          n
        

      
     where 
      
       n
      
     represents the dimension of the matrix. Observe the following equations.  
 
  
   I
   2
  
  =[ 
   
    
     
      1
     
     
      
     
     
      0
     
    
    
     
      0
     
     
      
     
     
      1
     
    

   
   ]
 

 
 
  
   I
   3
  
  =[ 
   
    
     
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
 

The identity matrix acts as a 1 in matrix algebra. For example, 
      
       AI=IA=A.
      
    
    
    A matrix that has a multiplicative inverse has the properties
     
      
        
          
            A
              A
              
                −1
              
            
            =I
          
        
        
          
            
              A
              
                −1
              
            
            A=I
          
        
      

    
    
    A matrix that has a multiplicative inverse is called an invertible matrix. Only a square matrix may have a multiplicative inverse, as the reversibility, 
      
       A
          A
          
            −1
          
        
        =
          A
          
            −1
          
        
        A=I,
      
     is a requirement. Not all square matrices have an inverse, but if 
      
       A
      
     is invertible, then 
      
       
          A
          
            −1
          
        

      
     is unique. We will look at two methods for finding the inverse of a 
      
       2×2
      
     matrix and a third method that can be used on both 
      
       2×2
      
     and 
 
  3×3
 
 matrices.

      The Identity Matrix and Multiplicative Inverse
      The identity matrix, 
        
          
            I
            n
          
          ,        
       is a square matrix containing ones down the main diagonal and zeros everywhere else.
       
 
  
   
    
     
    
   
   
    
     
      
       
        
         
          
           
            
             
            
           
           
            
             
              
               I
               2
              
              =[ 
               
                
                 
                  1
                 
                 
                  0
                 
                
                
                 
                  0
                 
                 
                  1
                 
                

               
               ]
               
                
                 
                
                
                 
                
                
                 
                
                
                 
                
               

              
               I
               3
              
              =[ 
               
                
                 
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
             
            
           

          
         
        
       
       
        
         
                 2×2                3×3
         
        
       

      
     
    
   

  
 

If 
        
          A        
       is an 
 n×n

matrix and 
        
          B        
       is an 
 n×n

matrix such that 
        
          AB=BA=
            I
            n
          
          ,        
       then 
        
          B=
            A
            
              −1
            
          
          ,        
       the multiplicative inverse of a matrix 
        
          A.
        
      
      

    
      
        
          Showing That the Identity Matrix Acts as a 1  
          Given matrix A, show that 
            
              AI=IA=A.
            
          
          
           
            
              A=[ 
                
                  
                    
                      
                        3
                      
                    
                    
                      4
                    
                  
                  
                    
                      
                        −2
                      
                    
                    
                      5
                    
                  

                
               ]
            
          
          
        
        

          Use matrix multiplication to show that the product of 
            
              A
            
           and the identity is equal to the product of the identity and A.
           
 
  AI=[ 
   
    
     
      3
     
     
      
     
     
      4
     
    
    
     
      
       −2
      
     
     
      
     
     
      5
     
    

   
   ]
   
    
     
    
   

  [ 
   
    
     
      1
     
     
      
     
     
      0
     
    
    
     
      0
     
     
      
     
     
      1
     
    

   
   ]=[ 
   
    
     
      
       3⋅1+4⋅0
      
     
     
      
     
     
      
     
     
      
       3⋅0+4⋅1
      
     
    
    
     
      
       −2⋅1+5⋅0
      
     
     
      
     
     
      
     
     
      
       −2⋅0+5⋅1
      
     
    

   
   ]=[ 
   
    
     
      3
     
     
      
     
     
      4
     
    
    
     
      
       −2
      
     
     
      
     
     
      5
     
    

   
   ]
 

 
 
  IA=[ 
   
    
     
      1
     
     
      
     
     
      0
     
    
    
     
      0
     
     
      
     
     
      1
     
    

   
   ]
   
    
     
    
   

  [ 
   
    
     
      3
     
     
      
     
     
      4
     
    
    
     
      
       −2
      
     
     
      
     
     
      5
     
    

   
   ]=[ 
   
    
     
      
       1⋅3+0⋅(−2)
      
     
     
      
     
     
      
     
     
      
       1⋅4+0⋅5
      
     
    
    
     
      
       0⋅3+1⋅(−2)
      
     
     
      
     
     
      
     
     
      
       0⋅4+1⋅5
      
     
    

   
   ]=[ 
   
    
     
      3
     
     
      
     
     
      4
     
    
    
     
      
       −2
      
     
     
      
     
     
      5
     
    

   
   ]
 

    

    
      How To
      Given two matrices, show that one is the multiplicative inverse of the other.
      
      Given matrix 
          
            A
          
         of order 
 
  n×n
 
 and matrix 
          
            B
          
         of order 
 
  n×n
 
 multiply 
          
            AB.
          
        
        
        If 
          
            AB=I,
          
         then find the product 
          
            BA.
          
         If 
          
            BA=I,
          
         then 
          
            B=
              A
              
                −1
              
            

          
         and 
          
            A=
              B
              
                −1
              
            
            .
          
        
        
      

    
      
          Showing That Matrix A Is the Multiplicative Inverse of Matrix B
          Show that the given matrices are multiplicative inverses of each other.
           
 
  A=[ 
   
    
     
      1
     
     
      
     
     
      5
     
    
    
     
      
       −2
      
     
     
      
     
     
      
       −9
      
     
    

   
   ],B=[ 
   
    
     
      
       −9
      
     
     
      
     
     
      
       −5
      
     
    
    
     
      2
     
     
      
     
     
      1
     
    

   
   ]
 

        
          Multiply 
            
              AB
            
           and 
            
              BA.
            
           If both products equal the identity, then the two matrices are inverses of each other.
           
 
  
   
    
     
      AB=[ 
       
        
         
          1
         
         
          
         
         
          5
         
        
        
         
          
           −2
          
         
         
          
         
         
          
           −9
          
         
        

       
       ]·[ 
       
        
         
          
           −9
          
         
         
          
         
         
          
           −5
          
         
        
        
         
          2
         
         
          
         
         
          1
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           1(−9)+5(2)
          
         
         
          
         
         
          
           1(−5)+5(1)
          
         
        
        
         
          
           −2(−9)−9(2)
          
         
         
          
         
         
          
           −2(−5)−9(1)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          1
         
         
          
         
         
          0
         
        
        
         
          0
         
         
          
         
         
          1
         
        

       
       ]
     
    
   

  
 

 
 
  
   
    
     
      BA=[ 
       
        
         
          
           −9
          
         
         
          
         
         
          
           −5
          
         
        
        
         
          2
         
         
          
         
         
          1
         
        

       
       ]·[ 
       
        
         
          1
         
         
          
         
         
          5
         
        
        
         
          
           −2
          
         
         
          
         
         
          
           −9
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           −9(1)−5(−2)
          
         
         
          
         
         
          
           −9(5)−5(−9)
          
         
        
        
         
          
           2(1)+1(−2)
          
         
         
          
         
         
          
           2(5)+1(−9)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          1
         
         
          
         
         
          0
         
        
        
         
          0
         
         
          
         
         
          1
         
        

       
       ]
     
    
   

  
 

 
            
              A
            
           and 
            B
           are inverses of each other.
        
      

    
      Try It
      Show that the following two matrices are inverses of each other.
           
 
  A=[ 
   
    
     
      1
     
     
      
     
     
      4
     
    
    
     
      
       −1
      
     
     
      
     
     
      
       −3
      
     
    

   
   ],B=[ 
   
    
     
      
       −3
      
     
     
      
     
     
      
       −4
      
     
    
    
     
      1
     
     
      
     
     
      1
     
    

   
   ]
 

         
 
  
   
    
     
      AB=[ 
       
        
         
          1
         
         
          
         
         
          4
         
        
        
         
          
           −1
          
         
         
          
         
         
          
           −3
          
         
        

       
       ]
       
        
         
        
       

      [ 
       
        
         
          
           −3
          
         
         
          
         
         
          
           −4
          
         
        
        
         
          1
         
         
          
         
         
          1
         
        

       
       ]=[ 
       
        
         
          
           1(−3)+4(1)
          
         
         
          
         
         
          
           1(−4)+4(1)
          
         
        
        
         
          
           −1(−3)+−3(1)
          
         
         
          
         
         
          
           −1(−4)+−3(1)
          
         
        

       
       ]=[ 
       
        
         
          1
         
         
          
         
         
          0
         
        
        
         
          0
         
         
          
         
         
          1
         
        

       
       ]
     
    
   
   
    
     
      BA=[ 
       
        
         
          
           −3
          
         
         
          
         
         
          
           −4
          
         
        
        
         
          1
         
         
          
         
         
          1
         
        

       
       ]
       
        
         
        
       

      [ 
       
        
         
          1
         
         
          
         
         
          4
         
        
        
         
          
           −1
          
         
         
          
         
         
          
           −3
          
         
        

       
       ]=[ 
       
        
         
          
           −3(1)+−4(−1)
          
         
         
          
         
         
          
           −3(4)+−4(−3)
          
         
        
        
         
          
           1(1)+1(−1)
          
         
         
          
         
         
          
           1(4)+1(−3)
          
         
        

       
       ]=[ 
       
        
         
          1
         
         
          
         
         
          0
         
        
        
         
          0
         
         
          
         
         
          1
         
        

       
       ]
     
    
   

  
 

      

    
      Finding the Multiplicative Inverse Using Matrix Multiplication
      We can now determine whether two matrices are inverses, but how would we find the inverse of a given matrix? Since we know that the product of a matrix and its inverse is the identity matrix, we can find the inverse of a matrix by setting up an equation using matrix multiplication.

      
        
            Finding the Multiplicative Inverse Using Matrix Multiplication
            Use matrix multiplication to find the inverse of the given matrix.
             
 
  A=[ 
   
    
     
      1
     
     
      
     
     
      
       −2
      
     
    
    
     
      2
     
     
      
     
     
      
       −3
      
     
    

   
   ]
 

          

            For this method, we multiply 
              
                A
              
             by a matrix containing unknown constants and set it equal to the identity.
             
 
  [ 
   
    
     
      1
     
     
      
       −2
      
     
    
    
     
      2
     
     
      
       −3
      
     
    

   
   ]  [ 
   
    
     
      a
     
     
      b
     
    
    
     
      c
     
     
      d
     
    

   
   ]=[ 
   
    
     
      1
     
     
      0
     
    
    
     
      0
     
     
      1
     
    

   
   ]
 

Find the product of the two matrices on the left side of the equal sign.
             
 
  [ 
   
    
     
      1
     
     
      
       −2
      
     
    
    
     
      2
     
     
      
       −3
      
     
    

   
   ]  [ 
   
    
     
      a
     
     
      b
     
    
    
     
      c
     
     
      d
     
    

   
   ]=[ 
   
    
     
      
       1a−2c
      
     
     
      
       1b−2d
      
     
    
    
     
      
       2a−3c
      
     
     
      
       2b−3d
      
     
    

   
   ]
 

Next, set up a system of equations with the entry in row 1, column 1 of the new matrix equal to the first entry of the identity, 1. Set the entry in row 2, column 1 of the new matrix equal to the corresponding entry of the identity, which is 0. 
              
                
                  
                    1a−2c=1   
                      R
                      1
                    

                  
                
                
                  
                    2a−3c=0   
                      R
                      2
                    

                  
                
              

            
            
            Using row operations, multiply and add as follows: 
              
                (−2)
                  R
                  1
                
                +
                  R
                  2
                
                →
                  R
                  2
                
                .
              
             Add the equations, and solve for 
              
                c.
              
            
             
 
  
   
    
     
      1a−2c=1
     
    
   
   
    
     
      0+1c=−2
     
    
   
   
    
     
      c=−2
     
    
   

  
 

Back-substitute to solve for 
              
                a.
              
            
            
             
 
  
   
    
     
      a−2(−2)=1
     
    
   
   
    
     
      a+4=1
     
    
   
   
    
     
      a=−3
     
    
   

  
 

Write another system of equations setting the entry in row 1, column 2 of the new matrix equal to the corresponding entry of the identity, 0. Set the entry in row 2, column 2 equal to the corresponding entry of the identity.
             
 
  
   
    
     
      1b−2d=0
     
    
    
     
      
       R
       1
      

     
    
   
   
    
     
      2b−3d=1
     
    
    
     
      
       R
       2
      

     
    
   

  
 

Using row operations, multiply and add as follows: 
              
                (
                  
                    −2
                  
                  )
                    R
                    1
                  
                +
                  R
                  2
                
                =
                  R
                  2
                
                .
              
             Add the two equations and solve for 
              
                d.
              
            
            
             
 
  
   
    
     
      1b−2d=0
     
    
   
   
    
     
      
       
        0+1d=1
       
       
        d=1
       
      

     
    
   
   
    
     
    
   

  
 

Once more, back-substitute and solve for 
              
                b.
              
            
            
             
 
  
   
    
     
      b−2(1)=0
     
    
   
   
    
     
      b−2=0
     
    
   
   
    
     
      b=2
     
    
   

  
 

 
 
  
   A
   
    −1
   
  
  =[ 
   
    
     
      
       −3
      
     
     
      
     
     
      2
     
    
    
     
      
       −2
      
     
     
      
     
     
      1
     
    

   
   ]
 

        

    
    Finding the Multiplicative Inverse by Augmenting with the IdentityAnother way to find the multiplicative inverse is by augmenting with the identity. When matrix 
        
          A        
       is transformed into 
        
          I,        
       the augmented matrix 
        
          I        
       transforms into 
        
          
            A
            
              −1
            
          
          .
        
      
      
      For example, given
       
 
  A=[ 
   
    
     
      2
     
     
      
     
     
      1
     
    
    
     
      5
     
     
      
     
     
      3
     
    

   
   ]
 

augment 
        
          A        
       with the identity
       
 
  [ 
   
    
     
      
       2
      
      
       1
      
     
     
      
       5
      
      
       3
      
     

    
   |
    
     
      1
     
     
      0
     
    
    
     
      0
     
     
      1
     
    

   
   ]
 

Perform row operations with the goal of turning 
        
          A        
       into the identity.
     Switch row 1 and row 2.
          
 
  [ 
   
    
     
      
       5
      
      
       3
      
     
     
      
       2
      
      
       1
      
     

    
   |
    
     
      0
     
     
      1
     
    
    
     
      1
     
     
      0
     
    

   
   ]
 

      Multiply row 2 by 
 
  −2
 
 and add to row 1.
         
 
  [ 
   
    
     
      
       1
      
      
       1
      
     
     
      
       2
      
      
       1
      
     

    
   |
    
     
      
       −2
      
     
     
      1
     
    
    
     
      1
     
     
      0
     
    

   
   ]
 

      Multiply row 1 by 
 
  −2
 
 and add to row 2.
         
 
  [ 
   
    
     
      
       1
      
      
       1
      
     
     
      
       0
      
      
       
        −1
       
      
     

    
   |
    
     
      
       −2
      
     
     
      1
     
    
    
     
      5
     
     
      
       −2
      
     
    

   
   ]
 

      Add row 2 to row 1.
         
 
  [ 
   
    
     
      
       1
      
      
       0
      
     
     
      
       0
      
      
       
        −1
       
      
     

    
   |
    
     
      3
     
     
      
       −1
      
     
    
    
     
      5
     
     
      
       −2
      
     
    

   
   ]
 

       Multiply row 2 by 
         
           −1.
         
       

          
 
  [ 
   
    
     
      
       1
      
      
       0
      
     
     
      
       0
      
      
       1
      
     

    
   |
    
     
      3
     
     
      
       −1
      
     
    
    
     
      
       −5
      
     
     
      2
     
    

   
   ]
 

     The matrix we have found is 
           
               A
               
                 −1
               
             
             .
           
         

          
 
  
   A
   
    −1
   
  
  =[ 
   
    
     
      3
     
     
      
     
     
      
       −1
      
     
    
    
     
      
       −5
      
     
     
      
     
     
      2
     
    

   
   ]
 

      Finding the Multiplicative Inverse of 2×2 Matrices Using a FormulaWhen we need to find the multiplicative inverse of a 
        
          2×2        
       matrix, we can use a special formula instead of using matrix multiplication or augmenting with the identity.If 
        
          A        
       is a 
        
          2×2        
       matrix, such as
       
 
  A=[ 
   
    
     
      a
     
     
      
     
     
      b
     
    
    
     
      c
     
     
      
     
     
      d
     
    

   
   ]
 

the multiplicative inverse of 
        
          A        
       is given by the formula
       
 
  
   A
   
    −1
   
  
  =
   1
   
    ad−bc
   
  
  [ 
   
    
     
      d
     
     
      
     
     
      
       −b
      
     
    
    
     
      
       −c
      
     
     
      
     
     
      a
     
    

   
   ]
 

where 
        
          ad−bc≠0.        
       If 
        
          ad−bc=0,        
       then 
        
          A        
       has no inverse.

      
        
            Using the Formula to Find the Multiplicative Inverse of Matrix A
            Use the formula to find the multiplicative inverse of
             
              
                A=[ 
                  
                    
                      
                        1
                      
                      
                        
                          −2
                        
                      
                    
                    
                      
                        2
                      
                      
                        
                          −3
                        
                      
                    

                  
                 ]
              
            
            
          
          

          Using the formula, we have
             
 
  
   
    
     
      
       A
       
        −1
       
      
      =
       1
       
        (1)(−3)−(−2)(2)
       
      
      [ 
       
        
         
          
           −3
          
         
         
          2
         
        
        
         
          
           −2
          
         
         
          1
         
        

       
       ]
     
    
   
   
    
     
      =
       1
       
        −3+4
       
      
      [ 
       
        
         
          
           −3
          
         
         
          2
         
        
        
         
          
           −2
          
         
         
          1
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
          
           −3
          
         
         
          2
         
        
        
         
          
           −2
          
         
         
          1
         
        

       
       ]
     
    
   

  
 

          
            Analysis 

            We can check that our formula works by using one of the other methods to calculate the inverse. Let’s augment 
              
                A
              
             with the identity. 
              
                [ 
                  
                    
                      
                        1
                      
                      
                        
                          −2
                        
                      
                    
                    
                      
                        2
                      
                      
                        
                          −3
                        
                      
                    

                  |
                    
                      
                        
                          1
                        
                        
                          0
                        
                      
                      
                        
                          0
                        
                        
                          1
                        
                      

                    
                  
                 ]
              
            
            
            Perform row operations with the goal of turning 
              
                A
              
             into the identity.
            Multiply row 1 by 
              
                −2
              
             and add to row 2.
               
                
                  [ 
                    
                      
                        
                          1
                        
                        
                          
                            −2
                          
                        
                      
                      
                        
                          0
                        
                        
                          1
                        
                      

                    |
                      
                        
                          
                            1
                          
                          
                            0
                          
                        
                        
                          
                            
                              −2
                            
                          
                          
                            1
                          
                        

                      
                    
                   ]
                
              
              
          Multiply row 2 by 2 and add to row 1.
             
              
                [ 
                  
                    
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        0
                      
                      
                        1
                      
                    

                  |
                    
                      
                        
                          
                            −3
                          
                        
                        
                          2
                        
                      
                      
                        
                          
                            −2
                          
                        
                        
                          1
                        
                      

                    
                  
                 ]
              
            
            
          So, we have verified our original solution.
             
 
  
   A
   
    −1
   
  
  =[ 
   
    
     
      
       −3
      
     
     
      2
     
    
    
     
      
       −2
      
     
     
      1
     
    

   
   ]
 

        

      
        Try It
        
          Use the formula to find the inverse of matrix 
            
              A.
            
           Verify your answer by augmenting with the identity matrix.
             
              
                A=[ 
                  
                    
                      
                        1
                      
                      
                        
                          −1
                        
                      
                    
                    
                      
                        2
                      
                      
                        
                          3
                        
                      
                    

                  
                 ]
              
            
            
          
           
            
              
                A
                
                  −1
                
              
              =[ 
                
                  
                    
                      
                        
                          3
                          5
                        

                      
                    
                    
                      
                        
                          1
                          5
                        

                      
                    
                  
                  
                    
                      
                        −
                          2
                          5
                        

                      
                    
                    
                      
                        
                          1
                          5
                        

                      
                    
                  

                
               ]
            
          
          
        
      

      
        
          
            Finding the Inverse of the Matrix, If It Exists
            Find the inverse, if it exists, of the given matrix.
             
              
                A=[ 
                  
                    
                      
                        3
                      
                      
                        6
                      
                    
                    
                      
                        1
                      
                      
                        2
                      
                    

                  
                 ]
              
            
            
          
          
            

          We will use the method of augmenting with the identity.
           
            
              [ 
                
                  
                    
                      3
                    
                    
                      6
                    
                  
                  
                    
                      1
                    
                    
                      2
                    
                  

                |
                  
                    
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        0
                      
                      
                        1
                      
                    

                  
                
               ]
            
          
          Switch row 1 and row 2.
             
              
                [ 
                  
                    
                      
                        1
                      
                      
                        3
                      
                    
                    
                      
                        3
                      
                      
                        
                          2
                        
                      
                    

                  |
                    
                      
                        
                          0
                        
                        
                          1
                        
                      
                      
                        
                          1
                        
                        
                          0
                        
                      

                    
                  
                 ]
              
            
            
            Multiply row 1 by −3 and add it to row 2.
               
                
                  [ 
                    
                      
                        
                          1
                        
                        
                          2
                        
                      
                      
                        
                          0
                        
                        
                          0
                        
                      

                    |
                     
                        
                          
                            1
                          
                          
                            0
                          
                        
                        
                          
                            
                              −3
                            
                          
                          
                            1
                          
                        

                      
                    
                   ]
                
              
              
          There is nothing further we can do. The zeros in row 2 indicate that this matrix has no inverse.
          
        
      

    
    
      Finding the Multiplicative Inverse of 3×3 MatricesUnfortunately, we do not have a formula similar to the one for a 
        
          2×2        
       matrix to find the inverse of a 
        
          3×3        
       matrix. Instead, we will augment the original matrix with the identity matrix and use row operations to obtain the inverse.Given a 
        
          3×3        
      
        matrix 
        
          A=[ 
            
              
                
                  2
                
                
                  3
                
                
                  1
                
              
              
                
                  3
                
                
                  3
                
                
                  1
                
              
              
                
                  2
                
                
                  4
                
                
                  1
                
              

            
           ]
        
      
      
      augment 
        
          A        
       with the identity matrix
       
 
  A|I=[ 
   
    
     
      2
     
     
      3
     
     
      1
     
    
    
     
      3
     
     
      3
     
     
      1
     
    
    
     
      2
     
     
      4
     
     
      1
     
    

    |
     
     
      
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
 

To begin, we write the augmented matrix with the identity on the right and 
        
          A        
       on the left. Performing elementary row operations so that the identity matrix appears on the left, we will obtain the inverse matrix on the right. We will find the inverse of this matrix in the next example.

      
        How To
        Given a 
          
            3×3
          
         matrix, find the inverseWrite the original matrix augmented with the identity matrix on the right.
        Use elementary row operations so that the identity appears on the left.
        What is obtained on the right is the inverse of the original matrix.
          Use matrix multiplication to show that 
            
              A
                A
                
                  −1
                
              
              =I
            
           and 
            
              
                A
                
                  −1
                
              
              A=I.
            
          
          
        

      
        
            Finding the Inverse of a 3 × 3 Matrix
            Given the 
              
                3×3
              
             matrix 
              
                A,
              
             find the inverse. 
              
                A=[ 
                  
                    
                      
                        2
                      
                      
                        3
                      
                      
                        1
                      
                    
                    
                      
                        3
                      
                      
                        3
                      
                      
                        1
                      
                    
                    
                      
                        2
                      
                      
                        4
                      
                      
                        1
                      
                    

                  
                 ]
              
            
            
          
          
            Augment 
              
                A
              
             with the identity matrix, and then begin row operations until the identity matrix replaces 
              
                A.
              
             The matrix on the right will be the inverse of 
              
                A.
              
            
            
             
              
                [ 
                  
                    
                      
                        2
                      
                      
                        3
                      
                      
                        1
                      
                    
                    
                      
                        3
                      
                      
                        3
                      
                      
                        1
                      
                    
                    
                      
                        2
                      
                      
                        4
                      
                      
                        1
                      
                    

                  |
                    
                      
                        
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
                  →
                  
                    Interchange 
                      R
                      2
                    
                    and 
                      R
                      1
                    

                  
                
                [ 
                  
                    
                      
                        3
                      
                      
                        3
                      
                      
                        1
                      
                    
                    
                      
                        2
                      
                      
                        3
                      
                      
                        1
                      
                    
                    
                      
                        2
                      
                      
                        4
                      
                      
                        1
                      
                    

                  |
                    
                      
                        
                          0
                        
                        
                          1
                        
                        
                          0
                        
                      
                      
                        
                          1
                        
                        
                          0
                        
                        
                          0
                        
                      
                      
                        
                          
                            0
                          
                        
                        
                          0
                        
                        
                          1
                        
                      

                    
                  
                 ]
              
            
            
             
 
  −
   R
   2
  
  +
   R
   1
  
  =
   R
   1
  
  →[ 
   
    
     
      
       1
      
      
       0
      
      
       0
      
     
     
      
       2
      
      
       3
      
      
       1
      
     
     
      
       2
      
      
       4
      
      
       1
      
     

    
   |
    
     
      
       −1
      
     
     
      1
     
     
      0
     
    
    
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      1
     
    

   
   ]
 

 
 
  −
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
      
      
       0
      
      
       0
      
     
     
      
       2
      
      
       3
      
      
       1
      
     
     
      
       0
      
      
       1
      
      
       0
      
     

    
   |
    
     
      
       −1
      
     
     
      1
     
     
      0
     
    
    
     
      1
     
     
      0
     
     
      0
     
    
    
     
      
       −1
      
     
     
      0
     
     
      1
     
    

   
   ]
 

 
 
  
   R
   3
  
  ↔ 
   R
   2
  
  →[ 
   
    
     
      
       1
      
      
       0
      
      
       0
      
     
     
      
       0
      
      
       1
      
      
       0
      
     
     
      
       2
      
      
       3
      
      
       1
      
     

    
   |
    
     
      
       −1
      
     
     
      1
     
     
      0
     
    
    
     
      
       −1
      
     
     
      0
     
     
      1
     
    
    
     
      1
     
     
      0
     
     
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
      
      
       0
      
      
       0
      
     
     
      
       0
      
      
       1
      
      
       0
      
     
     
      
       0
      
      
       3
      
      
       1
      
     

    
   |
    
     
      
       −1
      
     
     
      1
     
     
      0
     
    
    
     
      
       −1
      
     
     
      0
     
     
      1
     
    
    
     
      3
     
     
      
       −2
      
     
     
      0
     
    

   
   ]
 

 
 
  −3
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
      
      
       0
      
      
       0
      
     
     
      
       0
      
      
       1
      
      
       0
      
     
     
      
       0
      
      
       0
      
      
       1
      
     

    
   |
    
     
      
       −1
      
     
     
      1
     
     
      0
     
    
    
     
      
       −1
      
     
     
      0
     
     
      1
     
    
    
     
      6
     
     
      
       −2
      
     
     
      
       −3
      
     
    

   
   ]
 

Thus,
             
 
  
   A
   
    −1
   
  
  =B=[
   
    
     
      −1
     
    
    
     
      1
     
    
    
     
      0
     
    
   
   
    
     
      −1
     
    
    
     
      0
     
    
    
     
      1
     
    
   
   
    
     
      6
     
    
    
     
      −2
     
    
    
     
      −3
     
    
   

  ]
 

          
            Analysis 
            

            To prove that 
              
                B=
                  A
                  
                    −1
                  
                
                ,
              
             let’s multiply the two matrices together to see if the product equals the identity, if 
              
                A
                  A
                  
                    −1
                  
                
                =I
              
             and 
              
                
                  A
                  
                    −1
                  
                
                A=I.
              
            
 
 
  
   
    
     
      
       
        
         
          
           
            
             
            
           
           
            
             
            
           

          
         
        
       
       
        
         
          A
           A
           
            −1
           
          
          =[ 
           
            
             
              2
             
             
              3
             
             
              1
             
            
            
             
              3
             
             
              3
             
             
              1
             
            
            
             
              2
             
             
              4
             
             
              1
             
            

           
           ]  [ 
           
            
             
              
               −1
              
             
             
              1
             
             
              0
             
            
            
             
              
               −1
              
             
             
              0
             
             
              1
             
            
            
             
              6
             
             
              
               −2
              
             
             
              
               −3
              
             
            

           
           ]
         
        
       

      
     
    
   
   
    
     
      =[ 
       
        
         
          
           2(−1)+3(−1)+1(6)
          
         
         
          
           2(1)+3(0)+1(−2)
          
         
         
          
           2(0)+3(1)+1(−3)
          
         
        
        
         
          
           3(−1)+3(−1)+1(6)
          
         
         
          
           3(1)+3(0)+1(−2)
          
         
         
          
           3(0)+3(1)+1(−3)
          
         
        
        
         
          
           2(−1)+4(−1)+1(6)
          
         
         
          
           2(1)+4(0)+1(−2)
          
         
         
          
           2(0)+4(1)+1(−3)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
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
     
    
   

  
 

 
 
  
   
    
     
      
       
        
         
          
           
            
             
            
           
           
            
             
            
           

          
         
        
       
       
        
         
          
           A
           
            −1
           
          
          A=[ 
           
            
             
              
               −1
              
             
             
              1
             
             
              0
             
            
            
             
              
               −1
              
             
             
              0
             
             
              1
             
            
            
             
              6
             
             
              
               −2
              
             
             
              
               −3
              
             
            

           
           ]  [ 
           
            
             
              2
             
             
              3
             
             
              1
             
            
            
             
              3
             
             
              3
             
             
              1
             
            
            
             
              2
             
             
              4
             
             
              1
             
            

           
           ]
         
        
       

      
     
    
   
   
    
     
      =[ 
       
        
         
          
           −1(2)+1(3)+0(2)
          
         
         
          
           −1(3)+1(3)+0(4)
          
         
         
          
           
−1(1)+1(1)+0(1)
          
         
        
        
         
          
           −1(2)+0(3)+1(2)
          
         
         
          
           −1(3)+0(3)+1(4)
          
         
         
          
           −1(1)+0(1)+1(1)
          
         
        
        
         
          
           6(2)+−2(3)+−3(2)
          
         
         
          
           6(3)+−2(3)+−3(4)
          
         
         
          
           6(1)+−2(1)+−3(1)
          
         
        

       
       ]
     
    
   
   
    
     
      =[ 
       
        
         
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
     
    
   

  
 

        

      
        Try It
        
          Find the inverse of the 
            
              3×3
            
           matrix.
             
              
                A=[ 
                  
                    
                      
                        
                          2
                        
                      
                      
                        
                          −17
                        
                      
                      
                        
                          11
                        
                      
                    
                    
                      
                        
                          −1
                        
                      
                      
                        
                          11
                        
                      
                      
                        
                          −7
                        
                      
                    
                    
                      
                        
                          0
                        
                      
                      
                        
                          3
                        
                      
                      
                        
                          −2
                        
                      
                    

                  
                 ]
              
            
            
          
           
            
              
                A
                
                  −1
                
              
              =[ 
                
                  
                    
                      1
                    
                    
                      1
                    
                    
                      
                        2
                      
                    
                  
                  
                    
                      2
                    
                    
                      4
                    
                    
                      
                        −3
                      
                    
                  
                  
                    
                      3
                    
                    
                      6
                    
                    
                      
                        −5
                      
                    
                  

                
               ]
            
          
          
        
      
          
  
  Solving a System of Linear Equations Using the Inverse of a MatrixSolving a system of linear equations using the inverse of a matrix requires the definition of two new matrices: 
      
       X
      
     is the matrix representing the variables of the system, and 
      
       B
      
     is the matrix representing the constants. Using matrix multiplication, we may define a system of equations with the same number of equations as variables as
     
      
        AX=B
      
    
    
    To solve a system of linear equations using an inverse matrix, let 
      
       A
      
     be the coefficient matrix, let 
      
       X
      
     be the variable matrix, and let 
      
       B
      
     be the constant matrix. Thus, we want to solve a system 
      
       AX=B.
      
     For example, look at the following system of equations. 
 
  
   
    
     
      
       a
       1
      
      x+
       b
       1
      
      y=
       c
       1
      

     
    
   
   
    
     
      
       a
       2
      
      x+
       b
       2
      
      y=
       c
       2
      

     
    
   

  
 

From this system, the coefficient matrix is
     
      
        A=[ 
          
            
              
                
                  
                    a
                    1
                  

                
              
              
                
                  
                    b
                    1
                  

                
              
            
            
              
                
                  
                    a
                    2
                  

                
              
              
                
                  
                    b
                    2
                  

                
              
            

          
         ]
      
    
    
    The variable matrix is
     
      
        X=[ 
          
            
              
                x
              
            
            
              
                y
              
            

          
         ]
      
    
    
    And the constant matrix is
     
      
        B=[ 
          
            
              
                
                  
                    c
                    1
                  

                
              
            
            
              
                
                  
                    c
                    2
                  

                
              
            

          
         ]
      
    
    

    Then 
      
       AX=B
      
     looks like
     
 
  [ 
   
    
     
      
       
        a
        1
       

      
     
     
      
       
        b
        1
       

      
     
    
    
     
      
       
        a
        2
       

      
     
     
      
       
        b
        2
       

      
     
    

   
   ]  [ 
   
    
     
      x
     
    
    
     
      y
     
    

   
   ]=[ 
   
    
     
      
       
        c
        1
       

      
     
    
    
     
      
       
        c
        2
       

      
     
    

   
   ]
 

Recall the discussion earlier in this section regarding multiplying a real number by its inverse, 
 
  (
   2
   
    −1
   
  
  )2=(
   
    
     1
     2
    

   
  )2=1.
 
 To solve a single linear equation 
      
       ax=b
      
     for 
      
       x,
      
     we would simply multiply both sides of the equation by the multiplicative inverse (reciprocal) of 
      
       a.
      
     Thus, 
 
  
   
    
     
       ax=b
     
    
   
   
    
     
       (
       
        
         1
         a
        

       
      )ax=(
       
        
         1
         a
        

       
      )b
     
    
   
   
    
     
      (
       a
       
        −1
       
      
        )ax=(
       a
       
        −1
       
      
      )b
     
    
   
   
    
     
      [(
       a
       
        −1
       
      
      )a]x=(
       a
       
        −1
       
      
      )b
     
    
   
   
    
     
                 1x=(
       a
       
        −1
       
      
      )b
     
    
   
   
    
     
                   x=(
       a
       
        −1
       
      
      )b
     
    
   

  
 

The only difference between a solving a linear equation and a system of equations written in matrix form is that finding the inverse of a matrix is more complicated, and matrix multiplication is a longer process. However, the goal is the same—to isolate the variable.
    We will investigate this idea in detail, but it is helpful to begin with a 
 
  2×2
 
 system and then move on to a 
 
  3×3
 
 system.

      Solving a System of Equations Using the Inverse of a Matrix
      Given a system of equations, write the coefficient matrix 
        
          A,        
       the variable matrix 
        
          X,        
       and the constant matrix 
        
          B.        
       Then
       
        
          AX=B
        
      
      
      Multiply both sides by the inverse of 
        
          A        
       to obtain the solution.
       
 
  
   
    
     
      (
       
        
         A
         
          −1
         
        

       
      )AX=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   
   
    
     
      [ 
       (
        
         
          A
          
           −1
          
         

        
       )A
       ]X=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   
   
    
     
      IX=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   
   
    
     
      X=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   

  
 

    
      Q&A
      If the coefficient matrix does not have an inverse, does that mean the system has no solution?
      No, if the coefficient matrix is not invertible, the system could be inconsistent and have no solution, or be dependent and have infinitely many solutions.
    

    
      
          Solving a 2 × 2 System Using the Inverse of a Matrix
          Solve the given system of equations using the inverse of a matrix.
           
 
  
   
    
     
      3x+8y=5
     
    
   
   
    
     
      4x+11y=7
     
    
   

  
 

        

        Write the system in terms of a coefficient matrix, a variable matrix, and a constant matrix.
           
 
  A=[
   
    
     3
    
    
     8
    
   
   
    
     4
    
    
     
      11
     
    
   

  ],X=[
   
    
     x
    
   
   
    
     y
    
   

  ],B=[
   
    
     5
    
   
   
    
     7
    
   

  ]
 

Then
           
 
  [ 
   
    
     
      3
     
     
      8
     
    
    
     
      4
     
     
      
       11
      
     
    

   
   ]  [ 
   
    
     
      x
     
    
    
     
      y
     
    

   
   ]=[ 
   
    
     
      5
     
    
    
     
      7
     
    

   
   ]
 

First, we need to calculate 
            
              
                A
                
                  −1
                
              
              .
            
           Using the formula to calculate the inverse of a 2 by 2 matrix, we have:
           
 
  
   
    
     
      
       A
       
        −1
       
      
      =
       1
       
        ad−bc
       
      
      [ 
       
        
         
          d
         
         
          
           −b
          
         
        
        
         
          
           −c
          
         
         
          a
         
        

       
       ]
     
    
   
   
    
     
           =
       1
       
        3(11)−8(4)
       
      
      [ 
       
        
         
          
           11
          
         
         
          
           −8
          
         
        
        
         
          
           −4
          
         
         
          3
         
        

       
       ]
     
    
   
   
    
     
           =
       1
       1
      
      [ 
       
        
         
          
           11
          
         
         
          
           −8
          
         
        
        
         
          
           −4
          
         
         
          3
         
        

       
       ]
     
    
   

  
 

So,
           
            
              
                A
                
                  −1
                
              
              =[ 
                
                  
                    
                      
                        11
                      
                    
                    
                      
                        −8
                      
                    
                  
                  
                    
                      
                        −4
                      
                    
                    
                      
                        ​​3
                      
                    
                  

                
               ]
            
          
          
          Now we are ready to solve. Multiply both sides of the equation by 
            
              
                A
                
                  −1
                
              
              .
            
          
          
           
 
  
   
    
     
      (
       A
       
        −1
       
      
      )AX=(
       A
       
        −1
       
      
      )B
     
    
   
   
    
     
      [ 
       
        
         
          
           11
          
         
         
          
           −8
          
         
        
        
         
          
           −4
          
         
         
          3
         
        

       
       ]  [ 
       
        
         
          3
         
         
          8
         
        
        
         
          4
         
         
          
           11
          
         
        

       
       ]  [ 
       
        
         
          x
         
        
        
         
          y
         
        

       
       ]=[ 
       
        
         
          
           11
          
         
         
          
           −8
          
         
        
        
         
          
           −4
          
         
         
          3
         
        

       
       ]  [ 
       
        
         
          5
         
        
        
         
          7
         
        

       
       ]
     
    
   
   
    
     
      [ 
       
        
         
          1
         
         
          0
         
        
        
         
          0
         
         
          1
         
        

       
       ]  [ 
       
        
         
          x
         
        
        
         
          y
         
        

       
       ]=[ 
       
        
         
          
           11(5)+(−8)7
          
         
        
        
         
          
           −4(5)+3(7)
          
         
        

       
       ]
     
    
   
   
    
     
      [ 
       
        
         
          x
         
        
        
         
          y
         
        

       
       ]=[ 
       
        
         
          
           −1
          
         
        
        
         
          1
         
        

       
       ]
     
    
   

  
 

The solution is 
            
              (
                
                  −1,1
                
                ).
            
          
          
        
      

    
      Q&A
      Can we solve for 
        
          X        
       by finding the product 
        
          B
            A
            
              −1
            
          
          ?
        
      
      
      No, recall that matrix multiplication is not commutative, so 
        
          
            A
            
              −1
            
          
          B≠B
            A
            
              −1
            
          
          .        
       Consider our steps for solving the matrix equation. 
 
  
   
    
     
      (
       
        
         A
         
          −1
         
        

       
      )AX=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   
   
    
     
      [ 
       (
        
         
          A
          
           −1
          
         

        
       )A
       ]X=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   
   
    
     
      IX=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   
   
    
     
      X=(
       
        
         A
         
          −1
         
        

       
      )B
     
    
   

  
 

Notice in the first step we multiplied both sides of the equation by 
        
          
            A
            
              −1
            
          
          ,        
       but the 
        
          
            A
            
              −1
            
          
                  
       was to the left of 
 
  A
 
 on the left side and to the left of 
 
  B
 
 on the right side. Because matrix multiplication is not commutative, order matters.

    
      
          Solving a 3 × 3 System Using the Inverse of a Matrix
          Solve the following system using the inverse of a matrix.

           
 
  
   
    
     
      5x+15y+56z=35
     
    
   
   
    
     
      −4x−11y−41z=−26
     
    
   
   
    
     
      −x−3y−11z=−7
     
    
   

  
 

        
          Write the equation 
            
              AX=B.
            
          
          

           
 
  [ 
   
    
     
      5
     
     
      
       15
      
     
     
      
       56
      
     
    
    
     
      
       −4
      
     
     
      
       −11
      
     
     
      
       −41
      
     
    
    
     
      
       −1
      
     
     
      
       −3
      
     
     
      
       −11
      
     
    

   
   ]  [ 
   
    
     
      x
     
    
    
     
      y
     
    
    
     
      z
     
    

   
   ]=[ 
   
    
     
      
       35
      
     
    
    
     
      
       −26
      
     
    
    
     
      
       −7
      
     
    

   
   ]
 

First, we will find the inverse of 
            
              A
            
           by augmenting with the identity.
           
 
  [ 
   
    
     
      
       5
      
      
       
        15
       
      
      
       
        56
       
      
     
     
      
       
        −4
       
      
      
       
        −11
       
      
      
       
        −41
       
      
     
     
      
       
        −1
       
      
      
       
        −3
       
      
      
       
        −11
       
      
     

    
   |
    
     
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
 

Multiply row 1 by 
            
              
                1
                5
              
              .
            
          
          
           
            
              [ 
                
                  
                    
                      1
                    
                    
                      3
                    
                    
                      
                        
                          
                            56
                          
                          5
                        

                      
                    
                  
                  
                    
                      
                        −4
                      
                    
                    
                      
                        −11
                      
                    
                    
                      
                        −41
                      
                    
                  
                  
                    
                      
                        −1
                      
                    
                    
                      
                        −3
                      
                    
                    
                      
                        −11
                      
                    
                  

                |
                  
                    
                      
                        
                          
                            1
                            5
                          

                        
                      
                      
                        0
                      
                      
                        0
                      
                    
                    
                      
                        0
                      
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        0
                      
                      
                        0
                      
                      
                        1
                      
                    

                  
                
               ]
            
          
          
        Multiply row 1 by 4 and add to row 2.
           
            
              [ 
                
                  
                    
                      1
                    
                    
                      3
                    
                    
                      
                        
                          
                            56
                          
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                    
                      
                        
                          
                            19
                          
                          5
                        

                      
                    
                  
                  
                    
                      
                        −1
                      
                    
                    
                      
                        −3
                      
                    
                    
                      
                        −11
                      
                    
                  

                |
                  
                    
                      
                        
                          
                            1
                            5
                          

                        
                      
                      
                        0
                      
                      
                        0
                      
                    
                    
                      
                        
                          
                            4
                            5
                          

                        
                      
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        0
                      
                      
                        0
                      
                      
                        1
                      
                    

                  
                
               ]
            
          
          
        Add row 1 to row 3.
           
            
              [ 
                
                  
                    
                      1
                    
                    
                      3
                    
                    
                      
                        
                          
                            56
                          
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                    
                      
                        
                          
                            19
                          
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      
                        
                          1
                          5
                        

                      
                    
                  

                |
                  
                    
                      
                        
                          
                            1
                            5
                          

                        
                      
                      
                        0
                      
                      
                        0
                      
                    
                    
                      
                        
                          
                            4
                            5
                          

                        
                      
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        
                          
                            1
                            5
                          

                        
                      
                      
                        0
                      
                      
                        1
                      
                    

                  
                
               ]
            
          
          
        Multiply row 2 by −3 and add to row 1.
           
            
              [ 
                
                  
                    
                      1
                    
                    
                      0
                    
                    
                      
                        −
                          1
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                    
                      
                        
                          
                            19
                          
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      
                        
                          1
                          5
                        

                      
                    
                  

                |
                  
                    
                      
                        
                          −
                            
                              11
                            
                            5
                          

                        
                      
                      
                        
                          −3
                        
                      
                      
                        0
                      
                    
                    
                      
                        
                          
                            4
                            5
                          

                        
                      
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        
                          
                            1
                            5
                          

                        
                      
                      
                        0
                      
                      
                        1
                      
                    

                  
                
               ]
            
          
          
        Multiply row 3 by 5.
           
            
              [ 
                
                  
                    
                      1
                    
                    
                      0
                    
                    
                      
                        −
                          1
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                    
                      
                        
                          
                            19
                          
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      1
                    
                  

                |
                  
                    
                      
                        
                          −
                            
                              11
                            
                            5
                          

                        
                      
                      
                        
                          −3
                        
                      
                      
                        0
                      
                    
                    
                      
                        
                          
                            4
                            5
                          

                        
                      
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        1
                      
                      
                        0
                      
                      
                        5
                      
                    

                  
                
               ]
            
          
          
          Multiply row 3 by 
            
              
                1
                5
              

            
           and add to row 1.
           
            
              [ 
                
                  
                    
                      1
                    
                    
                      0
                    
                    
                      0
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                    
                      
                        
                          
                            19
                          
                          5
                        

                      
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      1
                    
                  

                |
                  
                    
                      
                        
                          −2
                        
                      
                      
                        
                          −3
                        
                      
                      
                        1
                      
                    
                    
                      
                        
                          
                            4
                            5
                          

                        
                      
                      
                        1
                      
                      
                        0
                      
                    
                    
                      
                        1
                      
                      
                        0
                      
                      
                        5
                      
                    

                  
                
               ]
            
          
          
          Multiply row 3 by 
            
              −
                
                  19
                
                5
              

            
           and add to row 2.
           
            
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
                    
                  

                |
                  
                    
                      
                        
                          −2
                        
                      
                      
                        
                          −3
                        
                      
                      
                        1
                      
                    
                    
                      
                        
                          −3
                        
                      
                      
                        1
                      
                      
                        
                          −19
                        
                      
                    
                    
                      
                        1
                      
                      
                        0
                      
                      
                        5
                      
                    

                  
                
               ]
            
          
          
        So,
           
            
              
                A
                
                  −1
                
              
              =[ 
                
                  
                    
                      
                        −2
                      
                    
                    
                      
                        −3
                      
                    
                    
                      1
                    
                  
                  
                    
                      
                        −3
                      
                    
                    
                      1
                    
                    
                      
                        −19
                      
                    
                  
                  
                    
                      1
                    
                    
                      0
                    
                    
                      5
                    
                  

                
               ]
            
          
          Multiply both sides of the equation by 
            
              
                A
                
                  −1
                
              
              .
            
           We want 
            
              
                A
                
                  −1
                
              
              AX=
                A
                
                  −1
                
              
              B:
            
          
          
           
 
  [ 
   
    
     
      
       −2
      
     
     
      
       −3
      
     
     
      1
     
    
    
     
      
       −3
      
     
     
      1
     
     
      
       −19
      
     
    
    
     
      1
     
     
      0
     
     
      5
     
    

   
   ]  [ 
   
    
     
      5
     
     
      
       15
      
     
     
      
       56
      
     
    
    
     
      
       −4
      
     
     
      
       −11
      
     
     
      
       −41
      
     
    
    
     
      
       −1
      
     
     
      
       −3
      
     
     
      
       −11
      
     
    

   
   ]  [ 
   
    
     
      x
     
    
    
     
      y
     
    
    
     
      z
     
    

   
   ]=[ 
   
    
     
      
       −2
      
     
     
      
       −3
      
     
     
      1
     
    
    
     
      
       −3
      
     
     
      1
     
     
      
       −19
      
     
    
    
     
      1
     
     
      0
     
     
      5
     
    

   
   ]  [ 
   
    
     
      
       35
      
     
    
    
     
      
       −26
      
     
    
    
     
      
       −7
      
     
    

   
   ]
 

Thus,
           
 
  
   A
   
    −1
   
  
  B=[ 
   
    
     
      
       −70+78−7
      
     
    
    
     
      
       −105−26+133
      
     
    
    
     
      
       35+0−35
      
     
    

   
   ]=[ 
   
    
     
      1
     
    
    
     
      2
     
    
    
     
      0
     
    

   
   ]
 

The solution is 
            
              (
                
                  1,2,0
                
                ).
            
          
          
        
      

    
      Try It
      
        Solve the system using the inverse of the coefficient matrix.

         
 
  
   
    
     
       2x−17y+11z=0
     
    
   
   
    
     
       −x+11y−7z=8
     
    
   
   
    
     
                    3y−2z=−2
     
    
   

  
 

           
            
              X=[ 
                
                  
                    
                      4
                    
                  
                  
                    
                      
                        38
                      
                    
                  
                  
                    
                      
                        58
                      
                    
                  

                
               ]
            
          
          

      
    

    
      How To
      Given a system of equations, solve with matrix inverses using a calculator.
      
      Save the coefficient matrix and the constant matrix as matrix variables 
          
            [ A ]
          
         and 
          
            [ B ].
          
        
        
      Enter the multiplication into the calculator, calling up each matrix variable as needed.
      If the coefficient matrix is invertible, the calculator will present the solution matrix; if the coefficient matrix is not invertible, the calculator will present an error message.
      

    
      
        
          Using a Calculator to Solve a System of Equations with Matrix Inverses
          Solve the system of equations with matrix inverses using a calculator
           
 
  
   
    
     
      2x+3y+z=32
     
    
   
   
    
     
      3x+3y+z=−27
     
    
   
   
    
     
      2x+4y+z=−2
     
    
   

  
 

        

          On the matrix page of the calculator, enter the coefficient matrix as the matrix variable 
            
              [ A ],
            
           and enter the constant matrix as the matrix variable 
            
              [ B ].
            
          
           
            
              [A]=[ 
                
                  
                    
                      2
                    
                    
                      3
                    
                    
                      1
                    
                  
                  
                    
                      3
                    
                    
                      3
                    
                    
                      1
                    
                  
                  
                    
                      2
                    
                    
                      4
                    
                    
                      1
                    
                  

                
               ], [B]=[ 
                
                  
                    
                      
                        32
                      
                    
                  
                  
                    
                      
                        −27
                      
                    
                  
                  
                    
                      
                        −2
                      
                    
                  

                
               ]
            
          
          
          On the home screen of the calculator, type in the multiplication to solve for 
            
              X,
            
           calling up each matrix variable as needed.
           
            
              
                
                  [A]
                
                
                  −1
                
              
              ×[B]
            
          
          
        Evaluate the expression.
           
            
              [ 
                
                  
                    
                      
                        −59
                      
                    
                  
                  
                    
                      
                        −34
                      
                    
                  
                  
                    
                      
                        252
                      
                    
                  

                
               ]
            
          
          
        
      
    

    
      Media
      Access these online resources for additional instruction and practice with solving systems with inverses.
      
        The Identity Matrix
        Determining Inverse Matrices
        Using a Matrix Equation to Solve a System of Equations
      
    
  Key Equations

Identity matrix for a 
 
  2×2
 
 matrix
 
 
  
   I
   2
  
  =[ 
   
    
     
      1
     
     
      0
     
    
    
     
      0
     
     
      1
     
    

   
   ]
 
 

Identity matrix for a 
 
  3×3
 
 matrix
 
 
  
   I
   3
  
  =[ 
   
    
     
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
 
 

Multiplicative inverse of a 
 
  2×2
 
 matrix
 
 
  
   A
   
    −1
   
  
  =
   1
   
    ad−bc
   
  
  [ 
   
    
     
      d
     
     
      
       −b
      
     
    
    
     
      
       −c
      
     
     
      a
     
    

   
   ],where ad−bc≠0
 
 

    Key Concepts
      An identity matrix has the property 
      
       AI=IA=A.
      
       See .
    An invertible matrix has the property 
      
       A
          A
          
            −1
          
        
        =
          A
          
            −1
          
        
        A=I.
      
     See .
    Use matrix multiplication and the identity to find the inverse of a 
      
       2×2
      
     matrix. See .
      The multiplicative inverse can be found using a formula.  See .
      Another method of finding the inverse is by augmenting with the identity. See .
    We can augment a 
      
       3×3
      
     matrix with the identity on the right and use row operations to turn the original matrix into the identity, and the matrix on the right becomes the inverse. See .
    	Write the system of equations as 
      
       AX=B,
      
     and multiply both sides by the inverse of 
      
       A:
          A
          
            −1
          
        
        AX=
          A
          
            −1
          
        
        B.
      
     See  and .
      We can also use a calculator to solve a system of equations with matrix inverses. See .
    
      

  

    Section Exercises
      Verbal
      In a previous section, we showed that matrix multiplication is not commutative, that is, 
        
          AB≠BA        
       in most cases. Can you explain why matrix multiplication is commutative for matrix inverses, that is, 
        
          
            A
            
              −1
            
          
          A=A
            A
            
              −1
            
          
          ?
        
      
      
      
        If 
          
            
              A
              
                −1
              
            

          
         is the inverse of 
          
            A,
          
         then 
          
            A
              A
              
                −1
              
            
            =I,
          
         the identity matrix. Since 
          
            A
          
         is also the inverse of 
          
            
              A
              
                −1
              
            
            ,
              A
              
                −1
              
            
            A=I.
          
         You can also check by proving this for a 
          
            2×2
          
         matrix.

      Does every 
        
          2×2        
       matrix have an inverse? Explain why or why not. Explain what condition is necessary for an inverse to exist.
      Can you explain whether a 
        
          2×2        
       matrix with an entire row of zeros can have an inverse? 
        No, because 
          
            ad
          
         and 
          
            bc
          
         are both 0, so 
          
            ad−bc=0,
          
         which requires us to divide by 0 in the formula. 

      Can a matrix with an entire column of zeros have an inverse? Explain why or why not.
      Can a matrix with zeros on the diagonal have an inverse? If so, find an example. If not, prove why not. For simplicity, assume a 
        
          2×2        
       matrix.
      
        Yes.  Consider the matrix 
          
            [ 
              
                
                  
                    0
                  
                  
                    1
                  
                
                
                  
                    1
                  
                  
                    0
                  
                

              
             ].
          
         The inverse is found with the following calculation: 
          
            
              A
              
                −1
              
            
            =
              1
              
                0(0)−1(1)
              
            
            [ 
              
                
                  
                    0
                  
                  
                    
                      −1
                    
                  
                
                
                  
                    
                      −1
                    
                  
                  
                    0
                  
                

              
             ]=[ 
              
                
                  
                    0
                  
                  
                    1
                  
                
                
                  
                    1
                  
                  
                    0
                  
                

              
             ].
          
        
        

    
    AlgebraicIn the following exercises, show that matrix 
        
          A        
       is the inverse of matrix 
        
          B.
        
      
      
       
        
          A=[ 
            
              
                
                  1
                
                
                  0
                
              
              
                
                  
                    −1
                  
                
                
                  1
                
              

            
           ],B=[ 
            
              
                
                  1
                
                
                  0
                
              
              
                
                  1
                
                
                  1
                
              

            
           ]
        
      
      
       
        
          A=[ 
            
              
                
                  1
                
                
                  2
                
              
              
                
                  3
                
                
                  4
                
              

            
           ],B=[ 
            
              
                
                  
                    −2
                  
                
                
                  1
                
              
              
                
                  
                    
                      3
                      2
                    

                  
                
                
                  
                    −
                      1
                      2
                    

                  
                
              

            
           ]
        
      
      
      
         
          
            AB=BA=[ 
              
                
                  
                    1
                  
                  
                    0
                  
                
                
                  
                    0
                  
                  
                    1
                  
                

              
             ]=I
          
        
        

       
        
          A=[ 
            
              
                
                  4
                
                
                  5
                
              
              
                
                  7
                
                
                  0
                
              

            
           ],B=[ 
            
              
                
                  0
                
                
                  
                    
                      1
                      7
                    

                  
                
              
              
                
                  
                    
                      1
                      5
                    

                  
                
                
                  
                    −
                      4
                      
                        35
                      
                    

                  
                
              

            
           ]
        
      
      
       
        
          A=[ 
            
              
                
                  
                    −2
                  
                
                
                  
                    
                      1
                      2
                    

                  
                
              
              
                
                  3
                
                
                  
                    −1
                  
                
              

            
           ],B=[ 
            
              
                
                  
                    −2
                  
                
                
                  
                    −1
                  
                
              
              
                
                  
                    −6
                  
                
                
                  
                    −4
                  
                
              

            
           ]
        
      
      
        
           
            
              AB=BA=[ 
                
                  
                    
                      1
                    
                    
                      0
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                  

                
               ]=I
            
          
          
        
       
        
          A=[ 
            
              
                
                  1
                
                
                  0
                
                
                  1
                
              
              
                
                  0
                
                
                  1
                
                
                  
                    −1
                  
                
              
              
                
                  0
                
                
                  1
                
                
                  1
                
              

            
           ],B=
            1
            2
          
          [ 
            
              
                
                  2
                
                
                  1
                
                
                  
                    −1
                  
                
              
              
                
                  0
                
                
                  1
                
                
                  1
                
              
              
                
                  0
                
                
                  
                    −1
                  
                
                
                  1
                
              

            
           ]
        
      
      
       
        
          A=[ 
            
              
                
                  1
                
                
                  2
                
                
                  3
                
              
              
                
                  4
                
                
                  0
                
                
                  2
                
              
              
                
                  1
                
                
                  6
                
                
                  9
                
              

            
           ],B=
            1
            4
          
          [ 
            
              
                
                  6
                
                
                  0
                
                
                  
                    −2
                  
                
              
              
                
                  
                    17
                  
                
                
                  
                    −3
                  
                
                
                  
                    −5
                  
                
              
              
                
                  
                    −12
                  
                
                
                  2
                
                
                  4
                
              

            
           ]
        
      
      
        
           
            
              AB=BA=[ 
                
                  
                    
                      1
                    
                    
                      0
                    
                    
                      0
                    
                  
                  
                    
                      0
                    
                    
                      1
                    
                    
                      0
                    
                  
                  
                    
                      0
                    
                    
                      0
                    
                    
                      1
                    
                  

                
               ]=I
            
          
          
        
       
        
          A=[ 
            
              
                
                  3
                
                
                  8
                
                
                  2
                
              
              
                
                  1
                
                
                  1
                
                
                  1
                
              
              
                
                  5
                
                
                  6
                
                
                  
                    12
                  
                
              

            
           ],B=
            1
            
              36
            
          
          [ 
            
              
                
                  
                    −6
                  
                
                
                  
                    84
                  
                
                
                  
                    −6
                  
                
              
              
                
                  7
                
                
                  
                    −26
                  
                
                
                  1
                
              
              
                
                  
                    −1
                  
                
                
                  
                    −22
                  
                
                
                  5
                
              

            
           ]
        
      
      

      For the following exercises, find the multiplicative inverse of each matrix, if it exists.

       
        
          [ 
            
              
                
                  3
                
                
                  
                    −2
                  
                
              
              
                
                  1
                
                
                  9
                
              

            
           ]
        
      
      
        
           
            
              
                1
                
                  29
                
              
              [ 
                
                  
                    
                      9
                    
                    
                      2
                    
                  
                  
                    
                      
                        −1
                      
                    
                    
                      3
                    
                  

                
               ]
            
          
          
        
       
        
          [ 
            
              
                
                  
                    −2
                  
                
                
                  2
                
              
              
                
                  3
                
                
                  1
                
              

            
           ]
        
      
      
       
        
          [ 
            
              
                
                  
                    −3
                  
                
                
                  7
                
              
              
                
                  9
                
                
                  2
                
              

            
           ]
        
      
      
        
           
            
              
                1
                
                  69
                
              
              [ 
                
                  
                    
                      
                        −2
                      
                    
                    
                      7
                    
                  
                  
                    
                      9
                    
                    
                      3
                    
                  

                
               ]
            
          
          
        
       
        
          [ 
            
              
                
                  
                    −4
                  
                
                
                  
                    −3
                  
                
              
              
                
                  
                    −5
                  
                
                
                  8
                
              

            
           ]
        
      
      
       
        
          [ 
            
              
                
                  1
                
                
                  1
                
              
              
                
                  2
                
                
                  2
                
              

            
           ]
        
      
      
        
          There is no inverse
        
       
        
          [ 
            
              
                
                  0
                
                
                  1
                
              
              
                
                  1
                
                
                  0
                
              

            
           ]
        
      
      
       
        
          [ 
            
              
                
                  
                    0.5
                  
                
                
                  
                    1.5
                  
                
              
              
                
                  1
                
                
                  
                    −0.5
                  
                
              

            
           ]
        
      
      
        
           
            
              
                4
                7
              
              [ 
                
                  
                    
                      
                        0.5
                      
                    
                    
                      
                        1.5
                      
                    
                  
                  
                    
                      1
                    
                    
                      
                        −0.5
                      
                    
                  

                
               ]
            
          
          
        
       
        
          [ 
            
              
                
                  1
                
                
                  0
                
                
                  6
                
              
              
                
                  
                    −2
                  
                
                
                  1
                
                
                  7
                
              
              
                
                  3
                
                
                  0
                
                
                  2
                
              

            
           ]
        
      
      
       
        
          [ 
            
              
                
                  0
                
                
                  1
                
                
                  
                    −3
                  
                
              
              
                
                  4
                
                
                  1
                
                
                  0
                
              
              
                
                  1
                
                
                  0
                
                
                  5
                
              

            
           ]
        
      
      
        
           
            
              
                1
                
                  17
                
              
              [ 
                
                  
                    
                      
                        −5
                      
                    
                    
                      5
                    
                    
                      
                        −3
                      
                    
                  
                  
                    
                      
                        20
                      
                    
                    
                      
                        −3
                      
                    
                    
                      
                        12
                      
                    
                  
                  
                    
                      1
                    
                    
                      
                        −1
                      
                    
                    
                      4
                    
                  

                
               ]
            
          
          
        
       
        
          [ 
            
              
                
                  1
                
                
                  2
                
                
                  
                    −1
                  
                
              
              
                
                  
                    −3
                  
                
                
                  4
                
                
                  1
                
              
              
                
                  
                    −2
                  
                
                
                  
                    −4
                  
                
                
                  
                    −5
                  
                
              

            
           ]
        
      
      
       
        
          [ 
            
              
                
                  1
                
                
                  9
                
                
                  
                    −3
                  
                
              
              
                
                  2
                
                
                  5
                
                
                  6
                
              
              
                
                  4
                
                
                  
                    −2
                  
                
                
                  7
                
              

            
           ]
        
      
      
        
           
            
              
                1
                
                  209
                
              
              [ 
                
                  
                    
                      
                        47
                      
                    
                    
                      
                        −57
                      
                    
                    
                      
                        69
                      
                    
                  
                  
                    
                      
                        10
                      
                    
                    
                      
                        19
                      
                    
                    
                      
                        −12
                      
                    
                  
                  
                    
                      
                        −24
                      
                    
                    
                      
                        38
                      
                    
                    
                      
                        −13
                      
                    
                  

                
               ]
            
          
          
        
       
        
          [ 
            
              
                
                  1
                
                
                  
                    −2
                  
                
                
                  3
                
              
              
                
                  
                    −4
                  
                
                
                  8
                
                
                  
                    −12
                  
                
              
              
                
                  1
                
                
                  4
                
                
                  2
                
              

            
           ]
        
      
      
       
        
          [ 
            
              
                
                  
                    
                      1
                      2
                    

                  
                
                
                  
                    
                      1
                      2
                    

                  
                
                
                  
                    
                      1
                      2
                    

                  
                
              
              
                
                  
                    
                      1
                      3
                    

                  
                
                
                  
                    
                      1
                      4
                    

                  
                
                
                  
                    
                      1
                      5
                    

                  
                
              
              
                
                  
                    
                      1
                      6
                    

                  
                
                
                  
                    
                      1
                      7
                    

                  
                
                
                  
                    
                      1
                      8
                    

                  
                
              

            
           ]
        
      
      
        
           
            
              [ 
                
                  
                    
                      
                        18
                      
                    
                    
                      
                        60
                      
                    
                    
                      
                        −168
                      
                    
                  
                  
                    
                      
                        −56
                      
                    
                    
                      
                        −140
                      
                    
                    
                      
                        448
                      
                    
                  
                  
                    
                      
                        40
                      
                    
                    
                      
                        80
                      
                    
                    
                      
                        −280
                      
                    
                  

                
               ]
            
          
          
        
       
        
          [ 
            
              
                
                  1
                
                
                  2
                
                
                  3
                
              
              
                
                  4
                
                
                  5
                
                
                  6
                
              
              
                
                  7
                
                
                  8
                
                
                  9
                
              

            
           ]
        
      
      

      For the following exercises, solve the system using the inverse of a 
 
  2×2
 
 matrix.
 
  
   
    
     5x−6y=−61
     
    
   
   
    
     
      4x+3y=−2
     
    
   

  
 

        
           
            
              (
                
                  −5,6
                
                )
            
          
          
        
       
        
          
            
              8x+4y=−100
            
          
          
            
              3x−4y=1
            
          
        

      
      
      
 
  
   
    
     3x−2y=6
     
    
   
   
    
     
      −x+5y=−2
     
    
   

  
 

        
           
            
              (
                
                  2,0
                
                )
            
          
          
        
      
 
  
   
    
     
      5x−4y=−5
     
    
   
   
    
     4x+y=2.3
     
    
   

  
 

      
 
  
   
    
     
      −3x−4y=9
     
    
   
   
    
     12x+4y=−6
     
    
   

  
 

        
           
            
              (
                
                  
                    1
                    3
                  
                  ,−
                    5
                    2
                  

                
                )
            
          
          
        
      
 
  
   
    
     
      −2x+3y=
       3
       
        10
       
      

     
    
   
   
    
     −x+5y=
       1
       2
      

     
    
   

  
 

      
 
  
   
    
     
       8
       5
      
      x−
       4
       5
      
      y=
       2
       5
      

     
    
   
   
    
     
      −
       8
       5
      
      x+
       1
       5
      
      y=
       7
       
        10
       
      

     
    
   

  
 

        
           
            
              (
                
                  −
                    2
                    3
                  
                  ,−
                    
                      11
                    
                    6
                  

                
                )
            
          
          
        
       
        
          
            
              
                1
                2
              
              x+
                1
                5
              
              y=−
                1
                4
              

            
          
          
            
              
                1
                2
              
              x−
                3
                5
              
              y=−
                9
                4
              

            
          
        

      
      

      For the following exercises, solve a system using the inverse of a 
        
          3×3        
      
        matrix.
 
  
   
    
     
      3x−2y+5z=21
     
    
   
   
    
     5x+4y=37
     
    
   
   
    
     x−2y−5z=5
     
    
   

  
 

        
           
            
              (
                
                  7,
                    1
                    2
                  
                  ,
                    1
                    5
                  

                
                )
            
          
          
        
      
 
  
   
    
     4x+4y+4z=40
     
    
   
   
    
     2x−3y+4z=−12
     
    
   
   
    
     −x+3y+4z=9
     
    
   

  
 

      
 
  
   
    
     6x−5y−z=31
     
    
   
   
    
     −x+2y+z=−6
     
    
   
   
    
     3x+3y+2z=13
     
    
   

  
 

        
           
            
              (
                
                  5,0,−1
                
                )
            
          
          
        
      
 
  
   
    
     
      6x−5y+2z=−4
     
    
   
   
    
     2x+5y−z=12
     
    
   
   
    
     2x+5y+z=12
     
    
   

  
 

      
 
  
   
    
     
      4x−2y+3z=−12
     
    
   
   
    
     
      2x+2y−9z=33
     
    
   
   
    
     6y−4z=1
     
    
   

  
 

        
           
            
              
                1
                
                  34
                
              
              (
                
                  −35,−97,−154
                
                )
            
          
          
        
       
        
          
            
              
                1
                
                  10
                
              
              x−
                1
                5
              
              y+4z=
                
                  −41
                
                2
              

            
          
          
            
              
                1
                5
              
              x−20y+
                2
                5
              
              z=−101
            
          
          
            
              
                3
                
                  10
                
              
              x+4y−
                3
                
                  10
                
              
              z=23
            
          
        

      
      
      
 
  
   
    
     
       1
       2
      
      x−
       1
       5
      
      y+
       1
       5
      
      z=
       
        31
       
       
        100
       
      

     
    
   
   
    
     
      −
       3
       4
      
      x−
       1
       4
      
      y+
       1
       2
      
      z=
       7
       
        40
       
      

     
    
   
   
    
     
      −
       4
       5
      
      x−
       1
       2
      
      y+
       3
       2
      
      z=
       1
       4
      

     
    
   

  
 

        
           
            
              
                1
                
                  690
                
              
              (
                
                  65,−1136,−229
                
                )
            
          
          
        
      
 
  
   
    
     
      0.1x+0.2y+0.3z=−1.4
     
    
   
   
    
     
      0.1x−0.2y+0.3z=0.6
     
    
   
   
    
     0.4y+0.9z=−2
     
    
   

  
 

    TechnologyFor the following exercises, use a calculator to solve the system of equations with matrix inverses.

      
 
  
   
    
     2x−y=−3
     
    
   
   
    
     
      −x+2y=2.3
     
    
   

  
 

        
           
            
              (
                
                  −
                    
                      37
                    
                    
                      30
                    
                  
                  ,
                    8
                    
                      15
                    
                  

                
                )
            
          
          
        
       
 
  
   
    
     
      −
       1
       2
      
      x−
       3
       2
      
      y=−
       
        43
       
       
        20
       
      

     
    
   
   
    
     
       5
       2
      
      x+
       
        11
       
       5
      
      y=
       
        31
       
       4
      

     
    
   

  
 

       
 
  
   
    
     
      12.3x−2y−2.5z=2
     
    
   
   
    
     
      36.9x+7y−7.5z=−7
     
    
   
   
    
     8y−5z=−10
     
    
   

  
 

        
           
            
              (
                
                  
                    
                      10
                    
                    
                      123
                    
                  
                  ,−1,
                    2
                    5
                  

                
                )
            
          
          
        
       
 
  
   
    
     
      0.5x−3y+6z=−0.8
     
    
   
   
    
     0.7x−2y=−0.06
     
    
   
   
    
     
      0.5x+4y+5z=0
     
    
   

  
 

    
      Extensions
        For the following exercises, find the inverse of the given matrix.

       
        
          [ 
            
              
                
                  1
                
                
                  0
                
                
                  1
                
                
                  0
                
              
              
                
                  0
                
                
                  1
                
                
                  0
                
                
                  1
                
              
              
                
                  0
                
                
                  1
                
                
                  1
                
                
                  0
                
              
              
                
                  0
                
                
                  0
                
                
                  1
                
                
                  1
                
              

            
           ]
        
      
      
        
           
 
  
   1
   2
  
  [ 
   
    
     
      2
     
     
      1
     
     
      
       −1
      
     
     
      
       −1
      
     
    
    
     
      0
     
     
      1
     
     
      1
     
     
      
       −1
      
     
    
    
     
      0
     
     
      
       −1
      
     
     
      1
     
     
      1
     
    
    
     
      0
     
     
      1
     
     
      
       −1
      
     
     
      1
     
    

   
   ]
 

       
 
  [ 
   
    
     
      
       −1
      
     
     
      0
     
     
      2
     
     
      5
     
    
    
     
      0
     
     
      0
     
     
      0
     
     
      2
     
    
    
     
      0
     
     
      2
     
     
      
       −1
      
     
     
      0
     
    
    
     
      1
     
     
      
       −3
      
     
     
      0
     
     
      1
     
    

   
   ]
 

       
 
  [ 
   
    
     
      1
     
     
      
       −2
      
     
     
      3
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      0
     
     
      2
     
    
    
     
      1
     
     
      4
     
     
      
       −2
      
     
     
      3
     
    
    
     
      
       −5
      
     
     
      0
     
     
      1
     
     
      1
     
    

   
   ]
 

        
           
 
  
   1
   
    39
   
  
  [ 
   
    
     
      3
     
     
      2
     
     
      1
     
     
      
       −7
      
     
    
    
     
      
       18
      
     
     
      
       −53
      
     
     
      
       32
      
     
     
      
       10
      
     
    
    
     
      
       24
      
     
     
      
       −36
      
     
     
      
       21
      
     
     
      9
     
    
    
     
      
       −9
      
     
     
      
       46
      
     
     
      
       −16
      
     
     
      
       −5
      
     
    

   
   ]
 

       
 
  [ 
   
    
     
      1
     
     
      2
     
     
      0
     
     
      2
     
     
      3
     
    
    
     
      0
     
     
      2
     
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      3
     
     
      0
     
     
      1
     
    
    
     
      0
     
     
      2
     
     
      0
     
     
      0
     
     
      1
     
    
    
     
      0
     
     
      0
     
     
      1
     
     
      2
     
     
      0
     
    

   
   ]
 

       
 
  [ 
   
    
     
      1
     
     
      0
     
     
      0
     
     
      0
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      0
     
     
      0
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      1
     
     
      0
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      0
     
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      0
     
     
      0
     
     
      1
     
     
      0
     
    
    
     
      1
     
     
      1
     
     
      1
     
     
      1
     
     
      1
     
     
      1
     
    

   
   ]
 

        
           
 
  [ 
   
    
     
      1
     
     
      0
     
     
      0
     
     
      0
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      1
     
     
      0
     
     
      0
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      1
     
     
      0
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      0
     
     
      1
     
     
      0
     
     
      0
     
    
    
     
      0
     
     
      0
     
     
      0
     
     
      0
     
     
      1
     
     
      0
     
    
    
     
      
       −1
      
     
     
      
       −1
      
     
     
      
       −1
      
     
     
      
       −1
      
     
     
      
       −1
      
     
     
      1
     
    

   
   ]
 

    
    
      Real-World Applications

      For the following exercises, write a system of equations that represents the situation. Then, solve the system using the inverse of a matrix.
      2,400 tickets were sold for a basketball game. If the prices for floor 1 and floor 2 were different, and the total amount of money brought in is $64,000, how much was the price of each ticket?
      In the previous exercise, if you were told there were 400 more tickets sold for floor 2 than floor 1, how much was the price of each ticket?
      
Infinite solutions. 

      	A food drive collected two different types of canned goods, green beans and kidney beans. The total number of collected cans was 350 and the total weight of all donated food was 348 lb, 12 oz. If the green bean cans weigh 2 oz less than the kidney bean cans, how many of each can was donated?
      	Students were asked to bring their favorite fruit to class. 95% of the fruits consisted of banana, apple, and oranges. If oranges were twice as popular as bananas, and apples were 5% less popular than bananas, what are the percentages of each individual fruit?
      
50% oranges, 25% bananas, 20% apples

      The nursing club held a bake sale to raise money and sold brownies and chocolate chip cookies. They priced the brownies at $1 and the chocolate chip cookies at $0.75. They raised $700 and sold 850 items. How many brownies and how many cookies were sold?
      A clothing store needs to order new inventory. It has three different types of hats for sale: straw hats, beanies, and cowboy hats. The straw hat is priced at $13.99, the beanie at $7.99, and the cowboy hat at $14.49. If 100 hats were sold this past quarter, $1,119 was taken in by sales, and the amount of beanies sold was 10 more than cowboy hats, how many of each should the clothing store order to replace those already sold?
      
10 straw hats, 50 beanies, 40 cowboy hats 

      Anna, Percy, and Morgan weigh a combined 370 lb. If Morgan weighs 20 lb more than Percy, and Anna weighs 1.5 times as much as Percy, how much does each person weigh?
      Three roommates shared a package of 12 ice cream bars, but no one remembers who ate how many. If Micah ate twice as many ice cream bars as Joe, and Albert ate three less than Micah, how many ice cream bars did each roommate eat?
      
Micah ate 6, Joe ate 3, and Albert ate 3.

      A farmer constructed a chicken coop out of chicken wire, wood, and plywood. The chicken wire cost $2 per square foot, the wood $10 per square foot, and the plywood $5 per square foot. The farmer spent a total of $51, and the total amount of materials used was 
        
          14
            
              ft
            
            2
          
          .        
       He used 
        
          
            
              3 ft
            
            2
          
                  
       more chicken wire than plywood. How much of each material in did the farmer use?
      Jay has lemon, orange, and pomegranate trees in his backyard. An orange weighs 8 oz, a lemon 5 oz, and a pomegranate 11 oz. Jay picked 142 pieces of fruit weighing a total of 70 lb, 10 oz. He picked 15.5 times more oranges than pomegranates. How many of each fruit did Jay pick?
      
 124 oranges, 10 lemons, 8 pomegranates 

    
  

  
    
      identity matrix a square matrix containing ones down the main diagonal and zeros everywhere else; it acts as a 1 in matrix algebra
    
      multiplicative inverse of a matrix a matrix that, when multiplied by the original, equals the identity matrix
