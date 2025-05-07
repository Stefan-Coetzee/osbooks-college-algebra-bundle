Logarithmic Functions

  m49363
  Logarithmic Functions
  In this section, you will:
Convert from logarithmic to exponential form.
Convert from exponential to logarithmic form.
Evaluate logarithms.
Use common logarithms.
Use natural logarithms.

  746b4be7-5dfd-4d01-8293-06ef750e0365

Learning Objectives Convert between exponential and logarithmic form. (IA 10.3.1)
Evaluate logarithmic functions. (IA 10.3.2)Objective 1: Convert between exponential and logarithmic form. (IA 10.3.1)Practice Makes Perfect
  Graph the exponential function f(x)=2x by making a table.
  

 
x
 
 y=f(x) 

  

  

  

  

  

Is it one-to-one?
Domain?
Range?
Graph the inverse of f(x)=2x on the grid above by interchanging x and y coordinates in the table.
 

 
x
 
 y=f(x) 

  

  

  

  

  

Is the inverse one-to-one function?
Domain? 
Range?

  
Find the inverse of f(x)=2x 

  
    

  
    Rewrite with y=f(x) 
     y=2x 
  
  
    Interchange the variables x and y .
     x=2y 
  
  
    Solve for y .
    Oops! We have no way to solve for y .
  

We give y a new notation:
y=logx2 
" y=logx2 " read "the logarithm, base 2 of x", means "the power to which we raise 2 to get x".
The function y=logax  is equivalent to  ay=x

is the logarithmic function with base a, where a>0,  x>0
Since the equations y=logax and x=ay are equivalent, we can go back and forth between them. This will often be the method to solve some exponential and logarithmic equations. To help with converting back and forth, let’s take a close look at the equations. Notice the positions of the exponent and base.

If we remember the logarithm is the exponent, it makes the conversion easier. You may want to repeat, “base to the exponent gives us the number.”
Convert between exponential and logarithmic form.
  ⓐ Convert to logarithmic form: 23=8 

  Identify the base and the exponent: the base is 2 and the exponent is 3. 
Then we have 3=log28 .

  
ⓑ Convert to exponential form: logbm=a 

  Identify the base and the exponent: the base is b and the exponent is a.

Then we have ba=m .

Practice Makes Perfect
Convert between exponential and logarithmic form.Remember these logarithmic notations to help complete the following:
 Common Logarithm logx=logx10

 Natural Logarithm lnx=logxe 
  
Convert to logarithmic form.

          ⓐ 8=2x
     
     
          ⓑ 10-2=0.01
     
     
          ⓒ ex=40
     

  
Convert to exponential form.

          ⓐ log813=4 
     
          ⓑ ln 1=0
     
     
          ⓒ log10000=4
     

Objective 2: Evaluate logarithmic functions (IA 10.3.2).
We can solve and evaluate logarithmic equations by using the technique of converting the equation to its equivalent exponential form.

Find the value of x: ⓐ logx36=2, ⓑ log4x=3, and ⓒ log1218=x. 

ⓐ

 logx36=2 

Convert to exponential form.
 x2=36 

Solve the quadratic.
 x=6,x=−6 

The base of a logarithmic function must be positive, so we eliminate x=−6 .
 x=6Therefore,log636=2. 

ⓑ

 log4x=3 

Convert to exponential form.
 43=x 

Simplify.
 x=64Therefore,log464=3. 

ⓒ

 log1218=x 

Convert to exponential form.
 (12)x=18 

Rewrite 18 as (12)3 .
 (12)x=(12)3 

With the same base, the exponents must be equal.
 x=3Therefore,log1218=3 

Practice Makes Perfect
  Evaluate logarithmic functions.Find the value of x .

          ⓐ log25x=2 
     
          ⓑ logx4=2
     
     
          ⓒ logx13=2
     

  Evaluate each of the following.

          ⓐ log10010 
     
          ⓑ log0.1
     
     
          ⓒ log24
     
     
          ⓓ log120
     
     
          ⓔ log44 
     
          ⓕ log193 
     
          ⓖ log22 
     
          ⓗ ln e-5 

Devastation of March 11, 2011 earthquake in Honshu, Japan. (credit: Daniel Pierce) In 2010, a major earthquake struck Haiti, destroying or damaging over 285,000 homeshttp://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us2010rja6/#summary. Accessed 3/4/2013.. One year later, another, stronger earthquake devastated Honshu, Japan, destroying or damaging over 332,000 buildings,http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc0001xgp/#summary. Accessed 3/4/2013. like those shown in . Even though both caused substantial damage, the earthquake in 2011 was 100 times stronger than the earthquake in Haiti. How do we know? The magnitudes of earthquakes are measured on a scale known as the Richter Scale. The Haitian earthquake registered a 7.0 on the Richter Scalehttp://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us2010rja6/. Accessed 3/4/2013. whereas the Japanese earthquake registered a 9.0.http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc0001xgp/#details. Accessed 3/4/2013.

The Richter Scale is a base-ten logarithmic scale. In other words, an earthquake of magnitude 8 is not twice as great as an earthquake of magnitude 4. It is 

10

8−4

=

10

4

=10,000

 times as great! In this lesson, we will investigate the nature of the Richter Scale and the base-ten function upon which it depends.Converting from Logarithmic to Exponential FormIn order to analyze the magnitude of earthquakes or compare the magnitudes of two different earthquakes, we need to be able to convert between logarithmic and exponential form. For example, suppose the amount of energy released from one earthquake were 500 times greater than the amount of energy released from another. We want to calculate the difference in magnitude. The equation that represents this problem is 

10

x

=500,

 where 
x

 represents the difference in magnitudes on the Richter Scale. How would we solve for 
x?

 We have not yet learned a method for solving exponential equations. None of the algebraic tools discussed so far is sufficient to solve 

10

x

=500.

 We know that 

10

2

=100

 and 

10

3

=1000,

 so it is clear that 
x

 must be some value between 2 and 3, since 
y=

10

x

 is increasing. We can examine a graph, as in , to better estimate the solution.

Estimating from a graph, however, is imprecise. To find an algebraic solution, we must introduce a new function. Observe that the graph in  passes the horizontal line test. The exponential function 
y=
b
x

 is one-to-one, so its inverse, 
x=
b
y

 is also a function. As is the case with all inverse functions, we simply interchange 
x

 and 
y

 and solve for 
y

 to find the inverse function. To represent 
y

 as a function of 
x,

 we use a logarithmic function of the form 
y=

log

b

(
x
).

 The base 
b

 logarithm of a number is the exponent by which we must raise 
b

 to get that number.We read a logarithmic expression as, “The logarithm with base 
b

 of 
x

 is equal to 
y,

 ” or, simplified, “log base 
b

 of 
x

 is 
y.

 ” We can also say, “ 

b

 raised to the power of 
y

 is 
x,

 ” because logs are exponents. For example, the base 2 logarithm of 32 is 5, because 5 is the exponent we must apply to 2 to get 32. Since 

2
5

=32,

 we can write 

log

2

32=5.

 We read this as “log base 2 of 32 is 5.”We can express the relationship between logarithmic form and its corresponding exponential form as follows:

 

log

b

(
x
)=y⇔
b
y

=x,	b>0,b≠1

 Note that the base 
b

 is always positive.

Because logarithm is a function, it is most correctly written as 

log

b

(x),

 using parentheses to denote function evaluation, just as we would with 
f(x).

 However, when the input is a single variable or number, it is common to see the parentheses dropped and the expression written without parentheses, as 

log

b

x.

 Note that many calculators require parentheses around the 
x.

 We can illustrate the notation of logarithms as follows:

Notice that, comparing the logarithm function and the exponential function, the input and the output are switched.  This means 
y=

log

b

(
x
)

 and 
y=
b
x

 are inverse functions.

Definition of the Logarithmic Function

A logarithm base 
b

 of a positive number 
x

 satisfies the following definition.

For 
x>0,b>0,b≠1,

 

 

y=

log

b

(
x
)is equivalent to 
b
y

=x

where,we read 

log

b

(
x
)

 as, “the logarithm with base 
b

 of 
x

 ” or the “log base 
b

 of 
x."

 
the logarithm 
y

 is the exponent to which 
b

 must be raised to get 
x.

 
Also, since the logarithmic and exponential functions switch the 
x

 and 
y

 values, the domain and range of the exponential function are interchanged for the logarithmic function. Therefore,

the domain of the logarithm function with base 
b is (0,∞).

 
the range of the logarithm function with base 
b is (−∞,∞).

 

Q&A
Can we take the logarithm of a negative number?

No. Because the base of an exponential function is always positive, no power of that base can ever be negative. We can never take the logarithm of a negative number. Also, we cannot take the logarithm of zero. Calculators may output a log of a negative number when in complex mode, but the log of a negative number is not a real number.

How To
Given an equation in logarithmic form 

log

b

(
x
)=y,

  convert it to exponential form.Examine the equation 
y=

log

b

(x)

 and identify 
b,y,andx.

 
Rewrite 

log

b

(x)=y

 as 

b
y

=x.

 

Converting from Logarithmic Form to Exponential Form
Write the following logarithmic equations in exponential form.
 ⓐ 

log

6

(

6

)=
1
2

 
 ⓑ 

log

3

(
9
)=2

 

First, identify the values of 
b,y,and x.

 Then, write the equation in the form 

b
y

=x.

  ⓐ 

log

6

(

6

)=
1
2

Here, 
b=6,y=
1
2

,and x=

6.

 Therefore, the equation 

log

6

(

6

)=
1
2

 is equivalent to 

6

1
2

=
6

.

 ⓑ 

log

3

(
9
)=2

Here, 
b=3,y=2,and x=9.

 Therefore, the equation 

log

3

(
9
)=2

 is equivalent to 

3
2

=9.

 

Try It

Write the following logarithmic equations in exponential form. 
ⓐ

log

10

(

1,000,000

)=6

 
ⓑ

log

5

(

25

)=2

 

ⓐ

log

10

(

1,000,000

)=6

 is equivalent to 

10

6

=1,000,000

 
ⓑ

log

5

(

25

)=2

 is equivalent to 

5
2

=25

 

Converting from Exponential to Logarithmic Form

To convert from exponents to logarithms, we follow the same steps in reverse. We identify the base 
b,

 exponent 
x,

 and output 
y.

 Then we write 
x=

log

b

(
y
).

 

Converting from Exponential Form to Logarithmic Form
Write the following exponential equations in logarithmic form.
 

2
3

=8

 
 

5
2

=25

 
 

10

−4

=
1

10,000

 

First, identify the values of 
b,y,andx.

 Then, write the equation in the form 
x=

log

b

(
y
).

  

2
3

=8

Here, 
b=2,

 
x=3,

 and 
y=8.

 Therefore, the equation 

2
3

=8

 is equivalent to 

log

2

(8)=3.

 
 

5
2

=25

Here, 
b=5,

 
x=2,

 and 
y=25.

 Therefore, the equation 

5
2

=25

 is equivalent to 

log

5

(25)=2.

 
 

10

−4

=
1

10,000

Here, 
b=10,

 
x=−4,

 and 
y=
1

10,000

.

 Therefore, the equation 

10

−4

=
1

10,000

 is equivalent to 

log

10

(
1

10,000

)=−4.

 

Try It

Write the following exponential equations in logarithmic form.

  ⓐ 

3
2

=9

 
 ⓑ 

5
3

=125

 
 ⓒ 

2

−1

=
1
2

 

 ⓐ 

3
2

=9

 is equivalent to 

log

3

(9)=2

 
 ⓑ 

5
3

=125

 is equivalent to 

log

5

(125)=3

 
 ⓒ 

2

−1

=
1
2

 is equivalent to 

log

2

(
1
2

)=−1

 

Evaluating Logarithms

Knowing the squares, cubes, and roots of numbers allows us to evaluate many logarithms mentally. For example, consider 

log

2

8.

 We ask, “To what exponent must 
2

 be raised in order to get 8?” Because we already know 

2
3

=8,

 it follows that 

log

2

8=3.

 Now consider solving 

log

7

49

 and 

log

3

27

 mentally.We ask, “To what exponent must 7 be raised in order to get 49?” We know 

7
2

=49.

 Therefore, 

log
7

49=2

We ask, “To what exponent must 3 be raised in order to get 27?” We know 

3
3

=27.

 Therefore, 

log
3

27=3

Even some seemingly more complicated logarithms can be evaluated without a calculator. For example, let’s evaluate 

log

2
3

4
9

 mentally.

We ask, “To what exponent must 

2
3

 be raised in order to get 

4
9

?

 ” We know 

2
2

=4

 and 

3
2

=9,

 so 

(

2
3

)

2

=
4
9

.

 Therefore, 

log

2
3

(

4
9

)=2.

How To
Given a logarithm of the form 
y=

log

b

(
x
),

 evaluate it mentally.Rewrite the argument 
x

 as a power of 
b:

 

b
y

=x.

 
Use previous knowledge of powers of 
b

 identify 
y

 by asking, “To what exponent should 
b

 be raised in order to get 
x?

 ”

Solving Logarithms Mentally
Solve 
y=

log

4

(

64

)

 without using a calculator.

First we rewrite the logarithm in exponential form: 

4
y

=64.

 Next, we ask, “To what exponent must 4 be raised in order to get 64?” 
We know
 

4
3

=64

 
Therefore,
 

log

(

64

)

4

=3

 

Try It

Solve 
y=

log

121

(

11

)

 without using a calculator.

 

log

121

(

11

)=
1
2

 (recalling that 

121

=

(121)

1
2

=11

 )

Evaluating the Logarithm of a Reciprocal
Evaluate 
y=

log

3

(

1

27

)

 without using a calculator.

First we rewrite the logarithm in exponential form: 

3
y

=
1

27

.

 Next, we ask, “To what exponent must 3 be raised in order to get 

1

27

?

 ”
We know 

3
3

=27,

 but what must we do to get the reciprocal, 

1

27

?

 Recall from working with exponents that 

b

−a

=
1

b
a

.

 We use this information to write
 

3

−3

=
1

3
3

=
1

27

Therefore, 

log

3

(

1

27

)=−3.

 

Try It

Evaluate 
y=

log

2

(

1

32

)

 without using a calculator.

 

log

2

(

1

32

)=−5

 

Using Common Logarithms
Sometimes you may see a logarithm written without a base. When you see one written this way, you need to look at the expression before evaluating it. It may be that the base you use doesn't matter. If you find it in computer science, it often means 
log2(
x
)

. However, in mathematics it almost always means the common logarithm of 10. In other words, the expression 
  log(
  x
  )
  
   often means 

log

10

(
x
).

Definition of the Common Logarithm

A common logarithm is a logarithm with base 
10.

 We can also write 

log

10

(
x
)

 simply as 
log(
x
).

 The common logarithm of a positive number 
x

 satisfies the following definition.
For 
x>0,

 

 

y=log(
x
)is equivalent to 

10

y

=x

 We read 
log(
x
)

 as, “the logarithm with base 
10

 of 
x

 ” or “log base 10 of 
x.

 ”

The logarithm 
y

 is the exponent to which 
10

 must be raised to get 
x.

 

  Currently, we use 
  
    

log

b

(
x
)
,

  lg
  (x)

   as the common logarithm, 
  
    
      lb(x)
    
   as the binary logarithm, and 
  
    
      ln(x)
    
   as the natural logarithm. Writing 
    
      lg(x)
    
   without specifying a base is now considered bad form, despite being frequently found in older materials.

How To
Given a common logarithm of the form 
y=log(
x
),

 evaluate it mentally.
Rewrite the argument 
x

 as a power of 
10:

 

10

y

=x.

 
Use previous knowledge of powers of 
10

 to identify 
y

 by asking, “To what exponent must 
10

 be raised in order to get 
x?

 ”

Finding the Value of a Common Logarithm Mentally
Evaluate 
y=log(1000)

 without using a calculator.

First we rewrite the logarithm in exponential form: 

10

y

=1000.

 Next, we ask, “To what exponent must 
10

 be raised in order to get 1000?” We know 
 

10

3

=1000

 Therefore, 
log(

1000

)=3.

 

Try It

Evaluate 
y=log(1,000,000).

 

 

log(1,000,000)=6

 

How To
Given a common logarithm with the form 
y=log(
x
),

 evaluate it using a calculator.
Press [LOG].
Enter the value given for 
x,

 followed by [ ) ].
Press [ENTER].

Finding the Value of a Common Logarithm Using a Calculator
Evaluate 
y=log(

321

)

 to four decimal places using a calculator.

Press [LOG].
Enter 321, followed by [ ) ].
Press [ENTER].

Rounding to four decimal places, 
log(

321

)≈2.5065.

 

Analysis 
Note that 

10

2

=100

 and that 

10

3

=1000.

 Since 321 is between 100 and 1000, we know that 
log(

321

)

 must be between 
log(

100

)

 and 
log(

1000

).

 This gives us the following:
 

100

<

321

<

1000

2

<

2.5065

<

3

 

Try It

Evaluate 
y=log(

123

)

 to four decimal places using a calculator.

 

log(

123

)≈2.0899

 

Rewriting and Solving a Real-World Exponential Model
The amount of energy released from one earthquake was 500 times greater than the amount of energy released from another. The equation 

10

x

=500

 represents this situation, where 
x

 is the difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference in magnitudes?

We begin by rewriting the exponential equation in logarithmic form.
 

10

x

=500

log(

500

)

=x

Use the definition of the common log.

Next we evaluate the logarithm using a calculator:
Press [LOG].
Enter 
500,

 followed by [ ) ].
Press [ENTER].
To the nearest thousandth, 
log(

500

)≈2.699.

 
The difference in magnitudes was about 
2.699.

 

Try It

The amount of energy released from one earthquake was 
8,500

 times greater than the amount of energy released from another. The equation 

10

x

=8500

 represents this situation, where 
x

 is the difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference in magnitudes?

The difference in magnitudes was about 
3.929.

Using Natural Logarithms
The most frequently used base for logarithms is 
e,

  the value of which is approximately 2.71828. Base 
e

 logarithms are important in calculus and some scientific applications; they are called natural logarithms. The base 
e

 logarithm, 

log

e

(
x
),

 has its own notation, 
ln(x).

 Most values of 
ln(
x
)

 can be found only using a calculator. The major exception is that, because the logarithm of 1 is always 0 in any base, 
ln1=0.

 For other natural logarithms, we can use the 
ln

 key that can be found on most scientific calculators. We can also find the natural logarithm of any power of 
e

 using the inverse property of logarithms.

Definition of the Natural Logarithm

A natural logarithm is a logarithm with base 
e.

 We write 

log

e

(
x
)

 simply as 

ln(
x
).

 The natural logarithm of a positive number 

x

 satisfies the following definition.
For 
x>0,

  

y=ln(
x
)is equivalent to 
e
y

=x

 We read 
ln(
x
)

 as, “the logarithm with base 
e

 of 
x

” or “the natural logarithm of 
x.

”The logarithm 
y

 is the exponent to which 
e

 must be raised to get 
x.

 

Since the functions 
y=e
x

 and 
y=ln(
x
)

 are inverse functions, 
ln(

e
x

)=x

 for all 
x

 and 
e
=

ln(x)

x

 for 
x>0.

 
How To
Given a natural logarithm with the form 
y=ln(
x
),

 evaluate it using a calculator.Press [LN].
Enter the value given for 
x,

 followed by [ ) ].
Press [ENTER].

Evaluating a Natural Logarithm Using a Calculator
Evaluate 
y=ln(

500

)

 to four decimal places using a calculator.

Press [LN].
Enter 
500,

 followed by [ ) ].
Press [ENTER].

Rounding to four decimal places, 
ln(500)≈6.2146

 

Try It

Evaluate 
ln(−500).

 

It is not possible to take the logarithm of a negative number in the set of real numbers.

Media
Access this online resource for additional instruction and practice with logarithms.

Introduction to Logarithms

Key Equations

Definition of the logarithmic function
For 
 
  x>0,b>0,b≠1,
 
  
 
  y=
   
    log
   
   b
  
  (
   x
  )
 
 if and only if 
 
 
   b
   y
  
  =x.
 
 

Definition of the common logarithm
For 
 
 x>0,
 
 
 
  y=log(
   x
  )
 
 if and only if 
 
 
   
    10
   
   y
  
  =x.
 
 

Definition of the natural logarithm
For 
 
 x>0,
 
 
 
  y=ln(
   x
  )
 
 if and only if 
 
 
   e
   y
  
  =x.
 
 

Key Concepts

The inverse of an exponential function is a logarithmic function, and the inverse of a logarithmic function is an exponential function.
Logarithmic equations can be written in an equivalent exponential form, using the definition of a logarithm. See .
Exponential equations can be written in their equivalent logarithmic form using the definition of a logarithm See .
Logarithmic functions with base 
b

 can be evaluated mentally using previous knowledge of powers of 
b.

 See  and .
Common logarithms can be evaluated mentally using previous knowledge of powers of 
10.

 See .
When common logarithms cannot be evaluated mentally, a calculator can be used. See .
Real-world exponential problems with base 
10

 can be rewritten as a common logarithm and then evaluated using a calculator. See .
Natural logarithms can be evaluated using a calculator .

Section Exercises
Verbal

What is a base 
b

 logarithm? Discuss the meaning by interpreting each part of the equivalent equations 

b
y

=x

 and 

log

b

x=y

 for 
b>0,b≠1.

 

A logarithm is an exponent. Specifically, it is the exponent to which a base 
b

 is raised to produce a given value. In the expressions given, the base 
b

 has the same value. The exponent, 
y,

 in the expression 

b
y

 can also be written as the logarithm, 

log

b

x,

 and the value of 
x

 is the result of raising 
b

 to the power of 
y.

 

How is the logarithmic function 
f(x)=

log

b

x

 related to the exponential function 
g(x)=
b
x

?

 What is the result of composing these two functions?

How can the logarithmic equation 

log

b

x=y

 be solved for 
x

 using the properties of exponents?

Since the equation of a logarithm is equivalent to an exponential equation, the logarithm can be converted to the exponential equation 

b
y

=x,

 and then properties of exponents can be applied to solve for 
x.

 

Discuss the meaning of the common logarithm. What is its relationship to a logarithm with base 
b,

 and how does the notation differ?

Discuss the meaning of the natural logarithm. What is its relationship to a logarithm with base 
b,

 and how does the notation differ?

The natural logarithm is a special case of the logarithm with base 
b

 in that the natural log always has base 
e.

 Rather than notating the natural logarithm as 

log

e

(
x
),

 the notation used is 
ln(
x
).

 

Algebraic 
For the following exercises, rewrite each equation in exponential form.

 

log

4

(q)=m

 

log

a

(b)=c

 

a
c

=b

 

 

log

16

(
y
)=x

 

 

log

x

(

64

)=y

 

 

x
y

=64

 

 

log

y

(
x
)=−11

 

 

log

15

(
a
)=b

 

 

15

b

=a

 

log

y

(

137

)=x

 

 

log

13

(

142

)=a

 

 

13

a

=142

 

 

log(v)=t

 

ln(w)=n

 

e
n

=w

 

For the following exercises, rewrite each equation in logarithmic form.

 

4
x

=y

 

 

c
d

=k

 

 

log

c

(k)=d

 

m

−7

=n

 

 

19

x

=y

 

 

log

19

y=x

 

 

x

−

10

13

=y

 

 

n
4

=103

 

 

log

n

(

103

)=4

 

 

(

7
5

)

m

=n

 

 

y
x

=

39

100

 

 

log

y

(

39

100

)=x

 

 

10

a

=b

 

 

e
k

=h

 

 

ln(h)=k

For the following exercises, solve for 
x

 by converting the logarithmic equation to exponential form.

 

log

3

(x)=2

 

log

2

(x)=−3

 

x=
2

−3

=
1
8

 

 

log

5

(x)=2

 

log

3

(
x
)=3

 

 

x=
3
3

=27

 

 

log

2

(x)=6

 

log

9

(x)=
1
2

 

x=
9

1
2

=3

 

 

log

18

(x)=2

 

log

6

(
x
)=−3

 

 

x=
6

−3

=
1

216

 

 

log(x)=3

 

ln(x)=2

 

x=
e
2

 

For the following exercises, use the definition of common and natural logarithms to simplify.

 

log(

100

8

)

 

10

log(32)

 

32

 

 

2log(.0001)

 

 

e

ln(

1.06

)

 

 

1.06

 

 

ln(

e

−5.03

)

 

 

e

ln(

10.125

)

+4

 

 

14.125

 

Numeric 

For the following exercises, evaluate the base 
b

 logarithmic expression without using a calculator.

 
 
  
   
    log
   
   3
  
  (
   
    
     1
     
      27
     
    

   
  )
 

 

log

6

(
6

)

 

1
2

 

 
 
  
   
    log
   
   2
  
  (
   
    
     1
     8
    

   
  )+4
 

 

6

log

8

(4)

 
4
 

For the following exercises, evaluate the common logarithmic expression without using a calculator.

 

log(10,000)

 

log(0.001)

 

−3

 

 

log(1)+7

 

2log(

100

−3

)

 

−12

 

For the following exercises, evaluate the natural logarithmic expression without using a calculator.

 

ln(
e

1
3

)

 

ln(1)

 
0
 

 

ln(
e

−0.225

)−3

 

25ln(
e

2
5

)

 

10

 

Technology

For the following exercises, evaluate each expression using a calculator. Round to the nearest thousandth.

 

log(0.04)

 

ln(15)

 

2.708

 

 
 
  ln(
   
    
     4
     5
    

   
  )
 

 

log(
2

)

 

0.151

 

 

ln(
2

)

Extensions 

Is 
x=0

 in the domain of the function 
f(x)=log(x)?

 If so, what is the value of the function when 
x=0?

 Verify the result.

No, the function has no defined value for 
x=0.

 To verify, suppose 
x=0

 is in the domain of the function 
f(x)=log(x).

 Then there is some number 
n

 such that 
n=log(0).

 Rewriting as an exponential equation gives: 

10

n

=0,

 which is impossible since no such real number 
n

 exists. Therefore, 
x=0

 is not the domain of the function 
f(x)=log(x).

 

Is 
f(x)=0

 in the range of the function 
f(x)=log(x)?

 If so, for what value of 
x?

 Verify the result.

Is there a number 
x

 such that 
lnx=2?

 If so, what is that number? Verify the result.

Yes. Suppose there exists a real number 
x

 such that 
lnx=2.

 Rewriting as an exponential equation gives 
x=
e
2

,

 which is a real number. To verify, let 
x=
e
2

.

 Then, by definition, 
ln(
x
)=ln(

e
2

)=2.

 

Is the following true: 

log

3

(27)

log

4

(

1

64

)

=−1?

 Verify the result.

Is the following true: 

ln(

e

1.725

)

ln(
1
)

=1.725?

 Verify the result.

No; 
ln(
1
)=0,

 so 

ln(

e

1.725

)

ln(
1
)

 is undefined.

Real-World Applications 

The exposure index 
EI

 for a camera is a measurement of the amount of light that hits the image receptor. It is determined by the equation 
EI=

log

2

(

f
2

t

),

 where 
f

 is the “f-stop” setting on the camera, and 

t

 is the exposure time in seconds. Suppose the f-stop setting is 
8

 and the desired exposure time is 
2

 seconds. What will the resulting exposure index be?

Refer to the previous exercise. Suppose the light meter on a camera indicates an 
EI

 of 
−2,

 and the desired exposure time is 16 seconds. What should the f-stop setting be?

 
2
 

The intensity levels I of two earthquakes measured on a seismograph can be compared by the formula 
log

I
1

I
2

=
M
1

−
M
2

 where 
M

 is the magnitude given by the Richter Scale. In August 2009, an earthquake of magnitude 6.1 hit Honshu, Japan. In March 2011, that same region experienced yet another, more devastating earthquake, this time with a magnitude of 9.0.http://earthquake.usgs.gov/earthquakes/world/historical.php. Accessed 3/4/2014. How many times greater was the intensity of the 2011 earthquake? Round to the nearest whole number.

common logarithm
the exponent to which 10 must be raised to get 
x;

 

log

10

(
x
)

 is written simply as 
log(
x
).

 

logarithm
the exponent to which 
b

 must be raised to get 
x;

 written 
y=

log

b

(
x
)

 

natural logarithm
the exponent to which  the number 
e

 must be raised to get 
x;

 

log

e

(
x
)

 is written as 
ln(
x
).
