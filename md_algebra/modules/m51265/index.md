Composition of Functions

  m51265
  Composition of Functions
  In this section, you will:
Combine functions using algebraic operations.
Create a new function by composition of functions.
Evaluate composite functions.
Find the domain of a composite function.
Decompose a composite function into its component functions.

  8a4fc477-43da-4fc4-9ff0-19a7fae5a19d

Learning ObjectivesFind the value of a function (IA 3.5.3), (CA 3.1.2)
Objective 1: Find the value of a function (IA 3.5.3), (CA 3.1.2)A function is a relation that assigns to each element in its domain exactly one element in the range. For each ordered pair in the relation, each x -value is matched with only one y -value.
The notation y=f(x)  defines a function named f .  This is read as “ y  is a function of x .” The letter x  represents the input value, or independent variable. The letter y, or f(x) , represents the output value, or dependent variable.

Function Notation
For the function
 

y
=
f
(
x
)

 f is the name of the function. 
 x is the input value, the collection of possible input values make up the domain.
 f(x) is the output value, the collection of possible output values make up the range.

We read
 

f
(
x
)

as
f
of
x
or the value of
f
at
x
.

Evaluating and Solving a Function Represented in Table Form

     
          ⓐ Evaluate g(3)
     
     
          ⓑ Solve g(n)=6
     

n
1
2
3
4
5

g(n)
8
6
7
6
8

          ⓐ Evaluating g(3) means determining the output value of the function g for the input value of n=3. The table output value corresponding to n=3 is 7, so g(3)=7.
     
     
          ⓑ Solving g(n)=6 means identifying the input values, n, that produce an output value of 6. The table shows two values where g(n) = 6 at x=2 and 4.
     

Practice Makes Perfect
Find the value of a function.

  
Given the function k(t)=2t-1:
  

     
          ⓐ Evaluate k(2)
     
     
          ⓑ Solve k(t)=7
     

  Given the function f(x)=x+2 :
  
     
          ⓐ Evaluate f(7)
     
     
          ⓑ Solve f(x)=4
     

  For the function f(x)=2x2+3x+1 , find
  
          ⓐ f(3)
     
     
          ⓑ f(–2)
     
     
          ⓒ f(t)
     
     
          ⓓ The value(s) of x that make f(x)=1
     

  
Use the table below to help answer the following:
  

x
1
2
3
4
5

g(x)
5
12
21
32
45

     
          ⓐ Evaluate g(4)
     
     
          ⓑ Solve g(x)=32
     

A composite function is a two-step function and can have numerical or variable inputs.
 x→g→g(x)→f→f(g(x)) (f∘g)(x)=f(g(x))  is read as “f of g of x”To evaluate a composite function, we always start evaluating the inner function and then evaluate the outer function in terms of the inner function.
Let’s use a table to help us organize our work in evaluating a two-step (composition) function in terms of some numerical inputs.First evaluate g in terms of x, the f in terms of g(x).
Given that: g(x)=3x-1 , and f(x)=x2+1 , complete the table below. Remember the output of g(x) becomes the input of f(x)!

  
    x
     g(x)=3x-1 
     f(g(x))=(g(x))2+1 
  
  
    –1
    
    
  
  
    –3
    
    
  
  
    0
    
    
  
  
    4
    
    
  
  
    10
    
    
  

Practice Makes Perfect
  
Use the table below showing values of f(x) and g(x) to find each of the following. Remember when working with composition functions we always evaluate the inner function first.
  

  
    x
    –3
    –2
    –1
    0
    1
    2
    3
  
  
    f(x)
   11
    9
    7
    5
    3
    1
    –1
  
  
    g(x)
   –8
    –3
    0
    1
    0
    –3
    –8
  

          ⓐ f(1)=
     
     
          ⓑ g(f(1))=
     
     
          ⓒ g(0)=
     
     
          ⓓ f(g(0))=
     
     
          ⓔ f(g(2))=
     
     
          ⓕ f(f(3))=
     

Suppose we want to calculate how much it costs to heat a house on a particular day of the year. The cost to heat a house will depend on the average daily temperature, and in turn, the average daily temperature depends on the particular day of the year. Notice how we have just defined two relationships: The cost depends on the temperature, and the temperature depends on the day.
Using descriptive variables, we can notate these two functions. The function 

C(
T
)
 gives the cost 

C
 of heating a house for a given average daily temperature in 

T
 degrees Celsius. The function 

T(
d
)
 gives the average daily temperature on day 

d
 of the year. For any given day, 

Cost=C(

T(
d
)
)
 means that the cost depends on the temperature, which in turns depends on the day of the year. Thus, we can evaluate the cost function at the temperature 

T(
d
).
 For example, we could evaluate 

T(
5
)
 to determine the average daily temperature on the 5th day of the year. Then, we could evaluate the cost function at that temperature. We would write 

C(

T(
5
)
).

By combining these two relationships into one function, we have performed function composition, which is the focus of this section.

Combining Functions Using Algebraic Operations
Function composition is only one way to combine existing functions. Another way is to carry out the usual algebraic operations on functions, such as addition, subtraction, multiplication and division. We do this by performing the operations with the function outputs, defining the result as the output of our new function.
Suppose we need to add two columns of numbers that represent a husband and wife’s separate annual incomes over a period of years, with the result being their total household income. We want to do this for every year, adding only that year’s incomes and then collecting all the data in a new column. If 

w(y)
 is the wife’s income and 

h(y)
 is the husband’s income in year 

y,
 and we want 

T
 to represent the total income, then we can define a new function.
 

T(
y
)=h(
y
)+w(
y
)

If this holds true for every year, then we can focus on the relation between the functions without reference to a year and write

 

T=h+w

Just as for this sum of two functions, we can define difference, product, and ratio functions for any pair of functions that have the same kinds of inputs (not necessarily numbers) and also the same kinds of outputs (which do have to be numbers so that the usual operations of algebra can apply to them, and which also must have the same units or no units when we add and subtract). In this way, we can think of adding, subtracting, multiplying, and dividing functions.
For two functions 

f(
x
)
 and 

g(
x
)
 with real number outputs, we define new functions 

f+g,f−g,fg,
 and 

f
g

 by the relations

 
 
  
   
    
     
      (f+g)(x)
     
    
    
     =
    
    
     
      f(x)+g(x)
     
    
    
   
   
    
     
      (f−g)(x)
     
    
    
     =
    
    
     
      f(x)−g(x)
     
    
    
   
   
    
     
       (fg)(x)
     
    
    
     =
    
    
     
      f(x)g(x)
     
    
    
   
   
    
     
      (
       
        
         f
         g
        

       
      )(x)
     
    
    
     =
    
    
     
      
       
        f(x)
       
       
        g(x)
       
      

     
    
    
     
      whereg(x)≠0
     
    
   

  
 

Performing Algebraic Operations on Functions
Find and simplify the functions 

(

g−f
)(
x
)
 and 

(

g
f

)(
x
),
 given 

f(
x
)=x−1
 and 

g(
x
)=
x
2

−1.
 Are they the same function?

Begin by writing the general form, and then substitute the given functions.

  
 
  
   
    
     
      (g−f)(x)
     
    
    
     =
    
    
     
      g(x)−f(x)
     
    
    
   
   
    
     
      (g−f)(x)
     
    
    
     =
    
    
     
      
       x
       2
      
      −1−(x−1)
     
    
    
   
   
    
     
      (g−f)(x)
     
    
    
     =
    
    
     
      
       x
       2
      
      −x
     
    
    
   
   

     
      (g−f)(x)
     
        
     =
    
    
     
      x(x−1)
     
    
    
   
   
    
    
    
    
   
   
    
    
    
    
   
   
    
     
       (
       
        
         g
         f
        

       
      )(x)
     
    
    
     =
    
    
     
      
       
        g(x)
       
       
        f(x)
       
      

     
    
    
   
   
    
     
      (
       
        
         g
         f
        

       
      )(x)
     
    
    
     =
    
    
     
      
       
        
         x
         2
        
        −1
       
       
        x−1
       
      

     
    
    
   
   

     
       (
       
        
         g
         f
        

       
      )(x)
     
        
     =
    
    
     
      
       
        (x+1)(x−1)
       
       
        x−1
       
      

     
    
    
     
      where x≠1
     
    
   
   

     
       (
       
        
         g
         f
        

       
      )(x)
     
        
     =
    
    
     
      x+1
     
    
    
   

  
 

No, the functions are not the same.
Note: For 

(

g
f

)(
x
),
 the condition 

x≠1
 is necessary because when 

x=1,
 the denominator is equal to 0, which makes the function undefined.

Try It

Find and simplify the functions 

(

fg
)(
x
)
 and 

(

f−g
)(
x
).

 

f(
x
)=x−1   and    g(
x
)=
x
2

−1

Are they the same function?

 

(

fg
)(
x
)=f(
x
)g(
x
)=(

x−1
)(

x
2

−1
)=
x
3

−
x
2

−x+1

(

f−g
)(
x
)=f(
x
)−g(
x
)=(

x−1
)−(

x
2

−1
)=x−
x
2

No, the functions are not the same.

Create a Function by Composition of FunctionsPerforming algebraic operations on functions combines them into a new function, but we can also create functions by composing functions. When we wanted to compute a heating cost from a day of the year, we created a new function that takes a day as input and yields a cost as output. The process of combining functions so that the output of one function becomes the input of another is known as a composition of functions. The resulting function is known as a composite function. We represent this combination by the following notation:
 

(

f∘g
)(
x
)=f(

g(
x
)
)

We read the left-hand side as 
 
  “f
 
 composed with 

g
 at 
 
  x,”
 
 and the right-hand side as 
 
  “f
 
 of 

g
 of 
 
  x.”
 
 The two sides of the equation have the same mathematical meaning and are equal. The open circle symbol 

∘
 is called the composition operator. We use this operator mainly when we wish to emphasize the relationship between the functions themselves without referring to any particular input value. Composition is a binary operation that takes two functions and forms a new function, much as addition or multiplication takes two numbers and gives a new number. However, it is important not to confuse function composition with multiplication because, as we learned above, in most cases 
 
  f(g(x))≠f(x)g(x).
 

It is also important to understand the order of operations in evaluating a composite function. We follow the usual convention with parentheses by starting with the innermost parentheses first, and then working to the outside. In the equation above, the function 

g
 takes the input 

x
 first and yields an output 

g(
x
).
 Then the function 

f
 takes 

g(
x
)
 as an input and yields an output 

f(

g(
x
)
).

In general, 

f∘g
 and 

g∘f
 are different functions. In other words, in many cases 

f(

g(
x
)
)≠g(

f(
x
)
)
 for all 

x.
 We will also see that sometimes two functions can be composed only in one specific order.
For example, if 

f(
x
)=
x
2

 and 

g(
x
)=x+2,
 then

 
  
   
    
     
      
       f(g(x))
      
     
     
      =
     
     
      
       f(x+2)
      
     
    
    
     
     
      =
     
     
      
       
        
         (x+2)
        
        2
       

      
     
    
    
     
     
      =
     
     
      
       
        x
        2
       
       +4x+4
      
     
    

   
  
 

but
 
 
  
   
    
     
      g(f(x))
     
    
    
     =
    
    
     
      g(
       x
       2
      
      )
     
    
   
   
    
    
     =
    
    
     
      
       x
       2
      
      +2
     
    
   

  
 

These expressions are not equal for all values of 

x,
 so the two functions are not equal. It is irrelevant that the expressions happen to be equal for the single input value 

x=−
1
2

.

Note that the range of the inside function (the first function to be evaluated) needs to be within the domain of the outside function. Less formally, the composition has to make sense in terms of inputs and outputs.

Composition of Functions
When the output of one function is used as the input of another, we call the entire operation a composition of functions. For any input 

x
 and functions 

f
 and 

g,
 this action defines a composite function, which we write as 

f∘g
 such that
 

(

f∘g
)(
x
)=f(

g(
x
)
)

The domain of the composite function 

f∘g
 is all 

x
 such that 

x
 is in the domain of 

g
 and 

g(
x
)
 is in the domain of 

f.

It is important to realize that the product of functions 

fg
 is not the same as the function composition 

f(

g(
x
)
),
 because, in general, 

f(
x
)g(
x
)≠f(

g(
x
)
).

Determining whether Composition of Functions is Commutative
Using the functions provided, find 

f(

g(
x
)
)
 and 

g(

f(
x
)
).
 Determine whether the composition of the functions is commutative.
 

f(x)=2x+1g(x)=3−x

Let’s begin by substituting 

g(
x
)
 into 

f(
x
).

  
  
   
    
     
      
       f(g(x))
      
     
     
      =
     
     
      
       2(3−x)+1
      
     
    
    
     
     
      =
     
     
      
       6−2x+1
      
     
    
    
     
     
      =
     
     
      
       7−2x
      
     
    

   
  
 

Now we can substitute 

f(
x
)
 into 

g(
x
).

  
  
   
    
     
      
       g(f(x))
      
     
     
      =
     
     
      
       3−(2x+1)
      
     
    
    
     
     
      =
     
     
      
       3−2x−1
      
     
    
    
     
     
      =
     
     
      
       −2x+2
      
     
    

   
  
 

We find that 
 
  g(f(x))≠f(g(x)),
 
 so the operation of function composition is not commutative.

Interpreting Composite Functions
The function 

c(s)
 gives the number of calories burned completing 

s
 sit-ups, and 

s(t)
 gives the number of sit-ups a person can complete in 

t
 minutes. Interpret 

c(s(3)).

The inside expression in the composition is 

s(3).
 Because the input to the s-function is time, 

t=3
 represents 3 minutes, and 

s(3)
 is the number of sit-ups completed in 3 minutes. Using 

s(3)
 as the input to the function 

c(s)
 gives us the number of calories burned during the number of sit-ups that can be completed in 3 minutes, or simply the number of calories burned in 3 minutes (by doing sit-ups).

Investigating the Order of Function Composition
Suppose 

f(x)
 gives miles that can be driven in 

x
 hours and 

g(y)
 gives the gallons of gas used in driving 

y
 miles. Which of these expressions is meaningful: 

f(

g(y)
)
 or 

g(

f(x)
)?

The function 

y=f(
x
)
 is a function whose output is the number of miles driven corresponding to the number of hours driven. 
 

number of miles =f(number of hours)

The function 

g(
y
)
 is a function whose output is the number of gallons used corresponding to the number of miles driven. This means:
 

number of gallons =g(number of miles)

The expression 

g(y)
 takes miles as the input and a number of gallons as the output. The function 

f(x)
 requires a number of hours as the input. Trying to input a number of gallons does not make sense. The expression 

f(

g(y)
)
 is meaningless.
The expression 

f(x)
 takes hours as input and a number of miles driven as the output. The function 

g(y)
 requires a number of miles as the input. Using 

f(x)
 (miles driven) as an input value for 

g(y),
 where gallons of gas depends on miles driven, does make sense. The expression 

g(

f(x)
)
 makes sense, and will yield the number of gallons of gas used, 

g,
 driving a certain number of miles, 

f(x),
 in 

x
 hours.

Q&A
Are there any situations where      f(g(y))  and      g(f(x))  would both be meaningful or useful expressions?

Yes. For many pure mathematical functions, both compositions make sense, even though they usually produce different new functions. In real-world problems, functions whose inputs and outputs have the same units also may give compositions that are meaningful in either order.

Try It

The gravitational force on a planet a distance r from the sun is given by the function 

G(r).
 The acceleration of a planet subjected to any force 

F
 is given by the function 

a(F).
 Form a meaningful composition of these two functions, and explain what it means.
A gravitational force is still a force, so 

a(

G(r)
)
 makes sense as the acceleration of a planet at a distance r from the Sun (due to gravity), but 

G(

a(F)
)
 does not make sense.

Evaluating Composite Functions
Once we compose a new function from two existing functions, we need to be able to evaluate it for any input in its domain. We will do this with specific numerical inputs for functions expressed as tables, graphs, and formulas and with variables as inputs to functions expressed as formulas. In each case, we evaluate the inner function using the starting input and then use the inner function’s output as the input for the outer function.

Evaluating Composite Functions Using Tables
When working with functions given as tables, we read input and output values from the table entries and always work from the inside to the outside. We evaluate the inside function first and then use the output of the inside function as the input to the outside function.

Using a Table to Evaluate a Composite Function
Using , evaluate 

f(g(3))
 and 

g(f(3)).

 
x

 
f(x)

 

g(x)

1
6
3

2
8
5

3
3
2

4
1
7

To evaluate 

f(g(3)),
 we start from the inside with the input value 3. We then evaluate the inside expression 

g(3)
 using the table that defines the function 

g:
 

g(3)=2.
 We can then use that result as the input to the function 

f,
 so 

g(3)
 is replaced by 2 and we get 

f(2).
 Then, using the table that defines the function 

f,
 we find that 

f(2)=8.

  
  
   
    
     
      
       g(3)
      
     
     
      =
     
     
      2
     
    
    
     
      
       f(g(3))
      
     
     
      =
     
     
      
       f(2)=8
      
     
    

   
  
 
 To evaluate 

g(f(3)),
 we first evaluate the inside expression 

f(3)
 using the first table: 

f(3)=3.
 Then, using the table for 
 
  g, 
 
 we can evaluate

 

g(f(3))=g(3)=2

 shows the composite functions 

f∘g
 and 

g∘f
 as tables.

 
x

 

g(
x
)

 

f(

g(
x
)
)

 

f(
x
)

 

g(

f(
x
)
)

3
2
8
3
2

Try It

Using , evaluate 

f(g(1))
 and 

g(f(4)).

 

f(g(1))=f(3)=3
 and 

g(f(4))=g(1)=3

Evaluating Composite Functions Using Graphs
When we are given individual functions as graphs, the procedure for evaluating composite functions is similar to the process we use for evaluating tables. We read the input and output values, but this time, from the 

x-
 and 

y-
 axes of the graphs.

How To
Given a composite function and graphs of its individual functions, evaluate it using the information provided by the graphs.

Locate the given input to the inner function on the 

x-
 axis of its graph.
Read off the output of the inner function from the 

y-
 axis of its graph.
Locate the inner function output on the 

x-
 axis of the graph of the outer function.
Read the output of the outer function from the 

y-
 axis of its graph. This is the output of the composite function.

Using a Graph to Evaluate a Composite Function
Using , evaluate 

f(g(1)).

To evaluate 

f(g(1)),
 we start with the inside evaluation. See .

We evaluate 

g(1)
 using the graph of 

g(x),
 finding the input of 1 on the 

x-
 axis and finding the output value of the graph at that input. Here, 

g(1)=3.
 We use this value as the input to the function 

f.

 

f(g(1))=f(3)

We can then evaluate the composite function by looking to the graph of 

f(x),
 finding the input of 3 on the 
 
  x-
 
 axis and reading the output value of the graph at this input. Here, 

f(3)=6,
 so 

f(g(1))=6.

Analysis 
 shows how we can mark the graphs with arrows to trace the path from the input value to the output value.

Try It

Using , evaluate 

g(f(2)).

 

g(f(2))=g(5)=3

Evaluating Composite Functions Using Formulas
When evaluating a composite function where we have either created or been given formulas, the rule of working from the inside out remains the same. The input value to the outer function will be the output of the inner function, which may be a numerical value, a variable name, or a more complicated expression.
While we can compose the functions for each individual input value, it is sometimes helpful to find a single formula that will calculate the result of a composition 

f(

g(
x
)
).
 To do this, we will extend our idea of function evaluation. Recall that, when we evaluate a function like 

f(t)=
t
2

−t,
 we substitute the value inside the parentheses into the formula wherever we see the input variable.

How To
Given a formula for a composite function, evaluate the function.

Evaluate the inside function using the input value or variable provided.
Use the resulting output as the input to the outside function.

Evaluating a Composition of Functions Expressed as Formulas with a Numerical Input
Given 

f(t)=
t
2

−t
 and 

h(x)=3x+2,
 evaluate 

f(h(1)).

Because the inside expression is 

h(1),
 we start by evaluating 

h(x)
 at 1.
  
  
   
    
     
      
       h(1)
      
     
     
      =
     
     
      
       3(1)+2
      
     
    
    
     
      
       h(1)
      
     
     
      =
     
     
      5
     
    

   
  
 

Then 

f(h(1))=f(5),
 so we evaluate 

f(t)
 at an input of 5.

  
  
   
    
     
      
       f(h(1))
      
     
     
      =
     
     
      
       f(5)
      
     
    
    
     
      
       f(h(1))
      
     
     
      =
     
     
      
       
        5
        2
       
       −5
      
     
    
    
     
      
       f(h(1))
      
     
     
      =
     
     
      
       20
      
     
    

   
  
 

Analysis 
It makes no difference what the input variables 

t
 and 

x
 were called in this problem because we evaluated for specific numerical values.

Try It

Given 

f(t)=
t
2

−t
 and 

h(x)=3x+2,
 evaluate 
ⓐ 

h(f(2))

ⓑ 

h(f(−2))

ⓐ 8 ⓑ 20

Finding the Domain of a Composite Function
As we discussed previously, the domain of a composite function such as 

f∘g
 is dependent on the domain of 

g
 and the domain of 

f.
 It is important to know when we can apply a composite function and when we cannot, that is, to know the domain of a function such as 

f∘g.
 Let us assume we know the domains of the functions 

f
 and 

g
 separately. If we write the composite function for an input 

x
 as 

f(

g(
x
)
),
 we can see right away that 

x
 must be a member of the domain of 

g
 in order for the expression to be meaningful, because otherwise we cannot complete the inner function evaluation. However, we also see that 

g(
x
)
 must be a member of the domain of 

f,
 otherwise the second function evaluation in 

f(

g(
x
)
)
 cannot be completed, and the expression is still undefined. Thus the domain of 

f∘g
 consists of only those inputs in the domain of 

g
 that produce outputs from 

g
 belonging to the domain of 

f.
 Note that the domain of 

f
 composed with 

g
 is the set of all 

x
 such that 

x
 is in the domain of 

g
 and 

g(
x
)
 is in the domain of 

f.

Domain of a Composite Function
The domain of a composite function 

f(

g(
x
)
)
 is the set of those inputs 

x
 in the domain of 

g
 for which 

g(
x
)
 is in the domain of 

f.

How To
Given a function composition 
 
  f(g(x)),
 
 determine its domain.Find the domain of 

g.
 
Find the domain of 

f.

Find those inputs 

x
 in the domain of 

g
 for which 

g(
x
)
 is in the domain of 

f.
 That is, exclude those inputs 

x
 from the domain of 

g
 for which 

g(
x
)
 is not in the domain of 

f.
 The resulting set is the domain of 

f∘g.

Finding the Domain of a Composite Function
Find the domain of
 

(

f∘g
)(x)wheref(x)=
5

x−1

andg(x)=
4

3x−2

The domain of 

g(
x
)
 consists of all real numbers except 

x=
2
3

,
 since that input value would cause us to divide by 0. Likewise, the domain of 

f
 consists of all real numbers except 1. So we need to exclude from the domain of 

g(
x
)
 that value of 

x
 for which 

g(
x
)=1.

  
  
   
    
     
      
       
        4
        
         3x−2
        
       

      
     
     
      =
     
     
      1
     
    
    
     
      4
     
     
      =
     
     
      
       3x−2
      
     
    
    
     
      6
     
     
      =
     
     
      
       3x
      
     
    
    
     
      x
     
     
      =
     
     
      2
     
    

   
  
 

So the domain of 

f∘g
 is the set of all real numbers except 

2
3

 and 

2.
 This means that

 

x≠
2
3

orx≠2

We can write this in interval notation as
 

(

−∞,
2
3

)∪(

2
3

,2
)∪(

2,∞
)

Finding the Domain of a Composite Function Involving Radicals
Find the domain of
 

(

f∘g
)(x) wheref(x)=

x+2

 and  g(x)=

3−x

Because we cannot take the square root of a negative number, the domain of 

g
 is 

( 
−∞,3 ].
 Now we check the domain of the composite function

 
(

f∘g
)(x)=

3−x+2

For 
(

f∘g
)(x)=

3−x+2
,

3−x+2
≥0,

since the radicand of a square root must be positive. Since square roots are positive, 

3−x
≥0
,

 or, 

3−x
≥0,

 which gives a domain of 
(-∞,3]
 .

Analysis 
This example shows that knowledge of the range of functions (specifically the inner function) can also be helpful in finding the domain of a composite function. It also shows that the domain of 

f∘g
 can contain values that are not in the domain of 

f,
 though they must be in the domain of 

g.

Try It

Find the domain of
 

(

f∘g
)(x) wheref(x)=
1

x−2

 and  g(x)=

x+4

 

 

[ 
−4,0 )∪(

0,∞
)

Decomposing a Composite Function into its Component FunctionsIn some cases, it is necessary to decompose a complicated function. In other words, we can write it as a composition of two simpler functions. There may be more than one way to decompose a composite function, so we may choose the decomposition that appears to be most expedient.

Decomposing a Function
Write 

f(x)=

5−
x
2

 as the composition of two functions.

We are looking for two functions, 

g
 and 

h,
 so 

f(x)=g(h(x)).
 To do this, we look for a function inside a function in the formula for 

f(x).
 As one possibility, we might notice that the expression 

5−
x
2

 is the inside of the square root. We could then decompose the function as

 

h(x)=5−
x
2

and g(x)=
x

We can check our answer by recomposing the functions.
 

g(h(x))=g(

5−
x
2

)=

5−
x
2

Try It

Write 

f(x)=
4

3−

4+
x
2

 as the composition of two functions.

Possible answer: 

g(
x
)=

4+
x
2

h(
x
)=
4

3−x

f=h∘g

Media
Access these online resources for additional instruction and practice with composite functions.

Composite Functions
Composite Function Notation Application
Composite Functions Using Graphs
Decompose Functions
Composite Function Values

Key Equation

Composite function
 
 
  (
   
    f∘g
   
  )(
   x
  )=f(
   
    g(
     x
    )
   
  )
 

Key Concepts
We can perform algebraic operations on functions. See .
When functions are composed, the output of the first (inner) function becomes the input of the second (outer) function.
The function produced by composing two functions is a composite function. See  and .
The order of function composition must be considered when interpreting the meaning of composite functions. See .
A composite function can be evaluated by evaluating the inner function using the given input value and then evaluating the outer function taking as its input the output of the inner function.
A composite function can be evaluated from a table. See .
A composite function can be evaluated from a graph. See .
A composite function can be evaluated from a formula. See .
The domain of a composite function consists of those inputs in the domain of the inner function that correspond to outputs of the inner function that are in the domain of the outer function. See  and .
Just as functions can be combined to form a composite function, composite functions can be decomposed into simpler functions.
Functions can often be decomposed in more than one way. See .

Section Exercises

Verbal

How does one find the domain of the quotient of two functions, 

f
g

?

Find the numbers that make the function in the denominator 

g
 equal to zero, and check for any other domain restrictions on 

f
 and 

g,
 such as an even-indexed root or zeros in the denominator.

What is the composition of two functions, 

f∘g?

If the order is reversed when composing two functions, can the result ever be the same as the answer in the original order of the composition? If yes, give an example. If no, explain why not.

Yes. Sample answer: Let 

f(x)=x+1and g(x)=x−1.
 Then 

f(g(x))=f(x−1)=(x−1)+1=x
 and 

g(f(x))=g(x+1)=(x+1)−1=x.
 So 

f∘g=g∘f.

How do you find the domain for the composition of two functions, 

f∘g?

AlgebraicFor the following exercises, determine the domain for each function in interval notation.

Given 
 
  f(x)=
   x
   2
  
  +2x
 
 and 
 
   g(x)=6−
   x
   2
  
  ,
 
 find 
 
  f+g,f−g,fg,
 
 and 
 
  
   f
   g
  
  .
 
 

 

(f+g)(
x
)=2x+6,
 domain: 

(−∞,∞)
 

 

(f−g)(
x
)=2
x
2

+2x−6,
 domain: 

(−∞,∞)

 

(fg)(
x
)=−
x
4

−2
x
3

+6
x
2

+12x,
 domain: 

(−∞,∞)

 

(

f
g

)(
x
)=

x
2

+2x

6−
x
2

,
 domain: 

(−∞,−
6

)∪(−
6

,
6

)∪(
6

,∞)

Given 
 
  f(x)=−3
   x
   2
  
  +x
 
 and 
 
  g(x)=5,
 
 find 
 
  f+g,f−g,fg,
 
 and 
 
  
   f
   g
  
  .
 
 

Given 
 
  f(x)=2
   x
   2
  
  +4x
 
 and 
 
  g(x)=
   1
   
    2x
   
  
  ,
 
 find 
 
  f+g,f−g,fg,
 
 and 
 
  
   f
   g
  
  .
 
 

 

(f+g)(
x
)=

4
x
3

+8
x
2

+1

2x

,
 domain: 

(−∞,0)∪(0,∞)
 
 

(f−g)(
x
)=

4
x
3

+8
x
2

−1

2x

,
 domain: 

(−∞,0)∪(0,∞)

 

(fg)(
x
)=x+2,
 domain: 

(−∞,0)∪(0,∞)

 

(

f
g

)(
x
)=4
x
3

+8
x
2

,
 domain: 

(−∞,0)∪(0,∞)

Given 

f(x)=
1

x−4

 and 

g(x)=
1

6−x

,
 find 
 
  f+g,f−g,fg,
 
 and 
 
  
   f
   g
  
  .
 
 

Given 

f(x)=3
x
2

 and 

g(x)=

x−5

,
 find 
 
  f+g,f−g,fg,
 
 and 
 
  
   f
   g
  
  .
 
 

 

(f+g)(x)=3
x
2

+

x−5

,
 domain: 

[5,∞)

 

(f−g)(x)=3
x
2

−

x−5

,
 domain: 

[5,∞)

 

(fg)(x)=3
x
2

x−5

,
 domain: 

[5,∞)

 

(

f
g

)(x)=

3
x
2

x−5

,
 domain: 

(5,∞)

Given 

f(x)=
x

 and 

g(x)=|x−3|,
 find 

g
f

.
 

For the following exercise, find the indicated function given 

f(x)=2
x
2

+1
 and 

g(x)=3x−5.
 
ⓐ 

f(g(2))

ⓑ 

f(g(x))

ⓒ 

g(f(x))

 ⓓ 

(

g∘g
)(
x
)

ⓔ 

(

f∘f
)(

−2
)

      
          ⓐ 3
       ⓑ 

f(

g(
x
)
)=2

(

3x−5
)
2

+1
 ⓒ 

f(

g(
x
)
)=6
x
2

−2
ⓓ

(

g∘g
)(x)=3(3x−5)−5=9x−20
ⓔ 

(

f∘f
)(

−2
)=163

For the following exercises, use each pair of functions to find 

f(

g(
x
)
)
 and 

g(

f(
x
)
).
 Simplify your answers.

 

f(x)=
x
2

+1,g(x)=

x+2

 

f(x)=
x

+2,g(x)=
x
2

+3

 

f(g(x))=

x
2

+3

+2,g(f(x))=x+4
x

+7

 

f(x)=| x |,g(x)=5x+1

 

f(x)=
x
3

,g(x)=

x+1

x
3

 

f(g(x))=

x+1

x
3

3

=

x+1
3

x

,g(f(x))=

x
3

+1
x

 

f(x)=
1

x−6

,g(x)=
7
x

+6

 

f(x)=
1

x−4

,g(x)=
2
x

+4

 

(

f∘g
)(x)=
1

2
x

+4−4

=
x
2

,(

g∘f
)(x)=2x−4

For the following exercises, use each set of functions to find 

f(

g(

h(x)
)
).
 Simplify your answers.

 

f(x)=
x
4

+6,
 

g(x)=x−6,
 and 

h(x)=
x

 

f(x)=
x
2

+1,
 

g(x)=
1
x

,
 and 

h(x)=x+3

 

f(g(h(x)))=

(

1

x+3

)
2

+1

Given 

f(x)=
1
x

 and 

g(x)=x−3,
 find the following:

ⓐ 

(f∘g)(x)

ⓑthe domain of 

(f∘g)(x)
 in interval notation
ⓒ 

(g∘f)(x)

 ⓓthe domain of 

(g∘f)(x)

ⓔ 

(

f
g

)(x)

Given 

f(x)=

2−4x

 and 

g(x)=−
3
x

,
 find the following:
ⓐ 

(g∘f)(x)

ⓑ the domain of 

(g∘f)(x)
 in interval notation

ⓐ 

(g∘f)(x)=−
3

2−4x

ⓑ

(

−∞,
1
2

)

Given the functions 
 
  f(x)=
   
    1−x
   
   x
  
  andg(x)=
   1
   
    1+
     x
     2
    

   
  
  ,
 
 find the following:ⓐ 

(g∘f)(x)

ⓑ 
 
  (g∘f)(2)
 

Given functions 

p(x)=
1

x

 and 

m(x)=
x
2

−4,
 state the domain of each of the following functions using interval notation:
ⓐ 

p(x)

m(x)

ⓑ 

p(m(x))

ⓒ 

m(p(x))

 ⓐ 

(0,2)∪(2,∞);
 ⓑ

(−∞,−2)∪(2,∞);
 ⓒ 

(0,∞)

Given functions 

q(x)=
1

x

 and 

h(x)=
x
2

−9,
 state the domain of each of the following functions using interval notation.
ⓐ 

q(x)

h(x)

ⓑ 

q(

h(x)
)

ⓒ 

h(

q(x)
)

For 

f(x)=
1
x

 and 

g(x)=

x−1

,
 write the domain of 

(f∘g)(x)
 in interval notation.

 

(1,∞)

For the following exercises, find functions 

f(x)
 and 

g(x)
 so the given function can be expressed as 

h(x)=f(

g(x)
).

 

h(x)=

(x+2)
2

 

h(x)=

(x−5)
3

sample: 

f(x)=
x
3

g(x)=x−5

 

h(x)=
3

x−5

 

h(x)=
4

(x+2)
2

sample: 
 
  
   
    
     
      f(x)=
       4
       x
      
      
    
   
   
    
     
      g(x)=
       
        (x+2)
       2
      
      
    
   

  

 

h(x)=4+
x
3

 

h(x)=

1

2x−3

3

sample: 

f(x)=
x
3

g(x)=
1

2x−3

 

h(x)=
1

(3
x
2

−4)

−3

 

h(x)=

3x−2

x+5

4

sample: 

f(x)=
x
4

g(x)=

3x−2

x+5

 

h(x)=

(

8+
x
3

8−
x
3

)
4

 

h(x)=

2x+6

sample: 

f(x)=
x

g(x)=2x+6

 

h(x)=

(5x−1)
3

 

h(x)=

x−1
3

sample: 

f(x)=
x
3

g(x)=(x−1)

 

h(x)=| 

x
2

+7 |

 

h(x)=
1

(x−2)
3

sample: 

f(x)=
x
3

g(x)=
1

x−2

 

h(x)=

(

1

2x−3

)
2

 

h(x)=

2x−1

3x+4

sample: 

f(x)=
x

g(x)=

2x−1

3x+4

Graphical
For the following exercises, use the graphs of 

f,
 shown in , and 

g,
 shown in , to evaluate the expressions.

 

f(

g(3)
)

 

f(

g(1)
)

2

 

g(

f(1)
)

 

g(

f(0)
)

5

 

f(

f(5)
)

 

f(

f(4)
)

4

 

g(

g(2)
)

 

g(

g(0)
)

0

For the following exercises, use graphs of 

f(x),
 shown in , 

g(x),
 shown in , and 

h(x),
 shown in , to evaluate the expressions.

 

g(

f(
1
)
)

 

g(

f(
2
)
)

2

 

f(

g(
4
)
)

 

f(

g(
1
)
)

1

 

f(

h(
2
)
)

 

h(

f(
2
)
)

4

 

f(

g(

h(
4
)
)
)

 

f(

g(

f(

−2
)
)
)

4

NumericFor the following exercises, use the function values for 

fand g
 shown in  to evaluate each expression.

 
 x
 

 
  f(x)
 

 
  g(x)
 

079

165

256

382

441

508

627

713

894

930

 

f(

g(
8
)
)

 

f(

g(
5
)
)

9

 

g(

f(
5
)
)

 

g(

f(
3
)
)

4

 

f(

f(
4
)
)

 

f(

f(
1
)
)

2

 

g(

g(
2
)
)

 

g(

g(
6
)
)

3

For the following exercises, use the function values for 

fand g
 shown in  to evaluate the expressions.

 
x

 

f(x)
 

 

g(x)
 

 
 
  −3
 
 
11
 
 
  −8
 
 

 
 
  −2
 
 
9
 
 
  −3
 
 

 
 
  −1
 
 
7
0

0
5
1

1
3
0

2
1
 
 
  −3
 
 

3
 
 
  −1
 
 
 
 
  −8
 
 

 

(f∘g)(1)

 

(f∘g)(2)

11

 

(g∘f)(2)

 

(g∘f)(3)

0

 

(g∘g)(1)

 

(f∘f)(3)

7

For the following exercises, use each pair of functions to find 

f(

g(
0
)
)
 and 

g(

f(0)
).

 

f(x)=4x+8,g(x)=7−
x
2

 

f(x)=5x+7,g(x)=4−2
x
2

 

f(g(0))=27,g(

f(0)
)=−94

 

f(x)=

x+4

,g(x)=12−
x
3

 

f(x)=
1

x+2

,g(x)=4x+3

 

f(g(0))=
1
5

,g(f(0))=5

For the following exercises, use the functions 

f(x)=2
x
2

+1
 and 

g(x)=3x+5

to evaluate or find the composite function as indicated.

 

f(

g(2)
)

 

f(

g(x)
)

 

18
x
2

+60x+51

 

g(

f(−3)
)

 

(g∘g)(x)

 

g∘g(x)=9x+20

Extensions
For the following exercises, use 

f(x)=
x
3

+1
 and 

g(x)=

x−1
3

.

Find 

(f∘g)(x)
 and 

(g∘f)(x).
 Compare the two answers.

Find 

(f∘g)(2)
 and 

(g∘f)(2).

2

What is the domain of 

(g∘f)(x)?

What is the domain of 

(f∘g)(x)?

 

(−∞,∞)

Let 

f(x)=
1
x

.

  ⓐFind 

(f∘f)(x).

ⓑIs 

(f∘f)(x)
 for any function 

f
 the same result as the answer to part (a) for any function? Explain.

For the following exercises, let 

F(x)=

(x+1)
5

,
 

f(x)=
x
5

,
 and 

g(x)=x+1.

True or False: 

(g∘f)(x)=F(x).

False

True or False: 

(f∘g)(x)=F(x).

For the following exercises, find the composition when 

f(x)=
x
2

+2
 for all 

x≥0
 and 

g(x)=

x−2

.

 

(f∘g)(6);(g∘f)(6)

 

(f∘g)(6)=6
 ; 

(g∘f)(6)=6

 

(g∘f)(a);(f∘g)(a)

 

(f∘g)(11);(g∘f)(11)

 

(f∘g)(11)=11,(g∘f)(11)=11

Real-World Applications

The function 

D(p)
 gives the number of items that will be demanded when the price is 

p.
 The production cost 

C(x)
 is the cost of producing 

x
 items. To determine the cost of production when the price is $6, you would do which of the following?
ⓐEvaluate 

D(

C(6)
).

ⓑEvaluate 

C(

D(6)
).

ⓒSolve 

D(

C(x)
)=6.

 ⓓSolve 

C(

D(p)
)=6.

The function 

A(d)
 gives the pain level on a scale of 0 to 10 experienced by a patient with 

d
 milligrams of a pain-reducing drug in her system. The milligrams of the drug in the patient’s system after 

t
 minutes is modeled by 

m(t).
 Which of the following would you do in order to determine when the patient will be at a pain level of 4?
ⓐEvaluate 

A(

m(4)
).

ⓑEvaluate 

m(

A(4)
).

ⓒSolve 

A(

m(t)
)=4.

 ⓓSolve 

m(

A(d)
)=4.

c

A store offers customers a 30% discount on the price 

x
 of selected items. Then, the store takes off an additional 15% at the cash register. Write a price function 

P(x)
 that computes the final price of the item in terms of the original price 

x.
 (Hint: Use function composition to find your answer.)

A rain drop hitting a lake makes a circular ripple. If the radius, in inches, grows as a function of time in minutes according to 

r(t)=25

t+2

,
 find the area of the ripple as a function of time. Find the area of the ripple at 

t=2.

 

A(t)=π

(

25

t+2

)
2

 and 

A(2)=π

(

25
4

)
2

=2500π
 square inches

A forest fire leaves behind an area of grass burned in an expanding circular pattern. If the radius of the circle of burning grass is increasing with time according to the formula 

r(t)=2t+1,
 express the area burned as a function of time, 

t
 (minutes).

Use the function you found in the previous exercise to find the total area burned after 5 minutes.

 

A(5)=π

(

2(5)+1
)
2

=121π
 square units

The radius 

r,
 in inches, of a spherical balloon is related to the volume, 
V,
 by 

r(V)=

3V

4π

3

.
 Air is pumped into the balloon, so the volume after 

t
 seconds is given by 

V(t)=10+20t.
 

ⓐFind the composite function 

r(

V(t)
).

ⓑFind the exact time when the radius reaches 10 inches.

The number of bacteria in a refrigerated food product is given by 

N(T)=23
T
2

−56T+1,
 

3<T<33,
 where 

T
 is the temperature of the food. When the food is removed from the refrigerator, the temperature is given by 

T(t)=5t+1.5,
 where 

t
 is the time in hours.
ⓐFind the composite function 

N(

T(t)
).

ⓑFind the time (round to two decimal places) when the bacteria count reaches 6752.

       
          ⓐ 
     
     N(T(t))=23
     
     (5t+1.5)
     2
     
     −56(5t+1.5)+1
     
     
     
     ⓑ 3.38 hours

composite function
the new function formed by function composition, when the output of one function is used as the input of another
