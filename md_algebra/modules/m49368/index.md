**Fitting Exponential Models to Data**

  m49368
  

**Fitting Exponential Models to Data**

  In this section, you will:

Build an exponential model from data.
Build a logarithmic model from data.
Build a logistic model from data.

  aa3a6479-56b9-4e74-9b72-5817cfe5bf5a

## Learning Objectives

Draw and interpret scatter diagrams (linear, exponential, logarithmic). (CA 4.3.1)
Fit a regression equation to a set of data and use the linear (or exponential) model to make predictions. (CA 4.3.4)

## Objective 1: Draw and interpret scatter diagrams (linear, exponential, logarithmic). (CA 4.3.1)

>
>
> **Vocabulary and Concept Check**
>
> Draw and interpret scatter diagrams (linear, exponential, logarithmic).
> Fill in the blanks and match the description with the graphs a, b, or c
> A ________ function has equation $f\left(x\right)=mx+b$ and has a basic shape ________.
>
> A ________ function has equation $f\left(x\right)={a}^{x},\ a>0,\ a\ne 1$ and has a basic shape ________.
>
> A ________ function has equation $f\left(x\right)={\mathrm{log}}_{a}x,\ a>0,\ x>0$ and has a basic shape ________.
>
>
>
> ![graph](../../media/CNX_Coreq_Figure_06_08_001.jpg)
>

A **Scatter Plot** is a graph of plotted points that may show a relationship between the variables in a set of data.

<hr/>

Draw and interpret scatter diagrams (linear, exponential, logarithmic).

1. **Using a Scatter Plot to Investigate Cricket Chirps**    The table below shows the number of cricket chirps in 15 seconds, for several different air temperatures, in degrees Fahrenheit Selected data from http://classic.globe.gov/fsl/scientistsblog/2007/10/. Retrieved Aug 3, 2010 . Plot this data, and determine whether the data appears to be linearly related.     | *Chirps* | 44 | 35 | 20.4 | 33 | 31 | 35 | 18.5 | 37 | 26 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | *Temperature* | 80.5 | 70.5 | 57 | 66 | 68 | 72 | 52 | 73.5 | 53 |

<details>
<summary>Solution</summary>

Plotting this data, as depicted below, suggests that there may be a trend. We can see from the trend in the data that the number of chirps increases as the temperature increases. The trend appears to be roughly linear, though certainly not perfectly so.

![Image](../../media/CNX_Precalc_Figure_02_04_002-0bd8.jpg)
</details>

### Practice Makes Perfect
Draw and interpret scatter diagrams ( linear, exponential, logarithmic).
2. Make a scatter plot for the table below. Does it look linear? Exponential? Logarithmic?      | x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | y | 0 | 1.5 | 2.2 | 2.8 | 3.5 | 3.6 | 3.9 | 4.3 | 4.4 |     ![blank plot](../../media/blankplot6.8.1.png)

3. Make a scatter plot for the table below. Does it look linear? Exponential? Logarithmic?      | x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | y | 3.3 | 5.6 | 9.1 | 15.1 | 24.4 | 40.2 | 66.2 | 108.4 | 180.1 |    ![ex2](../../media/blankplot6.8.2.png)

4. Make a scatter plot for the table below. Does it look linear? Exponential? Logarithmic?      | x | 1 | 2 | 3 | 4 | 5 | 6 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | y | 3 | 5.5 | 7 | 10 | 12.1 | 14.9 |    ![ex3](../../media/blankplot6.8.3.png)

## Objective 2: Fit a regression equation to a set of data and use the linear (or exponential) model to make predictions. (CA 4.3.4)

We can find a linear function that fits the data in the previous problem by “eyeballing” a line that seems to fit. But while estimating a line works relatively well, technology can help us find a line that fits the data as perfect as possible.

This line is called the Least Squares Regression Line or **Linear Regression Model**.
A regression line is a line that is closest to the data in the scatter plot, which means that such a line is a **best fit** for the data.
Fit a regression equation to a set of data and use the linear (or exponential) model to make predictions.

>
> How To
>
> *Given data of input and corresponding outputs from a linear function, find the best fit line using linear regression.*
>
>
>
> Enter the input in List 1 (L1).
> Enter the output in List 2 (L2).
> On a graphing utility, select Linear Regression (LinReg).
>

<hr/>

5. **Fit a regression equation to a set of data and use the linear (or exponential) model to make predictions.**      Find the linear regression line using the cricket-chirp data in the example earlier in this section, and find the temperature if there are 30 chirps in 15 seconds.

<details>
<summary>Solution</summary>

Enter the input (chirps) in List 1.

  
Enter the output (temperature) in List 2.

| L1 | 44 | 35 | 20.4 | 33 | 31 | 35 | 18.5 | 37 | 26 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| L2 | 80.5 | 70.5 | 57 | 66 | 68 | 72 | 52 | 73.5 | 53 |

On a graphing utility, select Linear Regression (LinReg). Using the cricket chirp data, with technology we obtain the equation:  T(c)=30.281+1.143c

To find the temperature for 30 chirps in 15 seconds we substitute 30 for x and find T:
 $T\left(30\right)=30.281+1.143\left(30\right)\ =64.571\approx 64.6\phantom{\rule{0.5em}{0ex}}degrees$

The graph of the scatter plot with the regression line of best fit is shown.
</details>

### Practice Makes Perfect
Fit a regression equation to a set of data and use the linear (or exponential) model to make predictions.
6. Gasoline consumption in the United States has been steadily increasing from 1994 to 2004.       | Year | 94 | 95 | 96 | 97 | 98 | 99 | 00 | 01 | 02 | 03 | 04 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | Consumption(billions of gallons) | 113 | 116 | 118 | 119 | 123 | 125 | 126 | 128 | 131 | 133 | 136 |   ⓐ  Determine whether the trend is linear, and if so, use your graphing utility to find a model for the data. ⓑ Use the model to predict the consumption in 2008.

7. We determined in the second practice problem,  earlier in this section, that the data below has an exponential trend. Use your graphing utility to find an exponential model that fits the data the best and write your exponential model below (Hint: instead of choosing Linear Regression, choose Exponential Regression).      | x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | y | 3.3 | 5.6 | 9.1 | 15.1 | 24.4 | 40.2 | 66.2 | 108.4 | 180.1 |

In previous sections of this chapter, we were either given a function explicitly to graph or evaluate, or we were given a set of points that were guaranteed to lie on the curve. Then we used algebra to find the equation that fit the points exactly. In this section, we use a modeling technique called *regression analysis* to find a curve that models data collected from real-world observations. With **regression analysis**, we don’t expect all the points to lie perfectly on the curve. The idea is to find a model that best fits the data. Then we use the model to make predictions about future events.
Do not be confused by the word *model*. In mathematics, we often use the terms *function*, *equation*, and *model* interchangeably, even though they each have their own formal definition. The term *model* is typically used to indicate that the equation or function approximates a real-world situation.

We will concentrate on three types of regression models in this section: exponential, logarithmic, and logistic. Having already worked with each of these functions gives us an advantage. Knowing their formal definitions, the behavior of their graphs, and some of their real-world applications gives us the opportunity to deepen our understanding. As each regression model is presented, key features and definitions of its associated function are included for review. Take a moment to rethink each of these functions, reflect on the work we’ve done so far, and then explore the ways regression is used to model real-world phenomena.

# Building an Exponential Model from Data
As we’ve learned, there are a multitude of situations that can be modeled by exponential functions, such as investment growth, radioactive decay, atmospheric pressure changes, and temperatures of a cooling object. What do these phenomena have in common? For one thing, all the models either increase or decrease as time moves forward. But that’s not the whole story. It’s the *way* data increase or decrease that helps us determine whether it is best modeled by an exponential equation. Knowing the behavior of exponential functions in general allows us to recognize when to use exponential regression, so let’s review exponential growth and decay.
Recall that exponential functions have the form $y=a{b}^{x}$ or $y={A}_{0}{e}^{kx}.$ When performing regression analysis, we use the form most commonly used on graphing utilities, $y=a{b}^{x}.$ Take a moment to reflect on the characteristics we’ve already learned about the exponential function $y=a{b}^{x}$ (assume $a>0):$ 

 $b$ must be greater than zero and not equal to one.
The initial value of the model is $y=a.$
If $b>1,$ the function models exponential growth. As $x$ increases, the outputs of the model increase slowly at first, but then increase more and more rapidly, without bound.
If $0<b<1,$ the function models **exponential decay**. As $x$ increases, the outputs for the model decrease rapidly at first and then level off to become asymptotic to the *x*-axis. In other words, the outputs never become equal to or less than zero.

As part of the results, your calculator will display a number known as the *correlation coefficient*, labeled by the variable $r,$ or ${r}^{2}.$ (You may have to change the calculator’s settings for these to be shown.) The values are an indication of the “goodness of fit” of the regression equation to the data. We more commonly use the value of ${r}^{2}$ instead of $r,$ but the closer either value is to 1, the better the regression equation approximates the data.

>
>
>
>
> **Exponential Regression**
>
>
> *Exponential regression* is used to model situations in which growth begins slowly and then accelerates rapidly without bound, or where decay begins rapidly and then slows down to get closer and closer to zero. We use the command “*ExpReg*” on a graphing utility to fit an exponential function to a set of data points. This returns an equation of the form, $$
> y=a{b}^{x}
> $$ 
> Note that:
>
>  $b$ must be non-negative.
> when $b>1,$ we have an exponential growth model.
> when $0<b<1,$ we have an exponential decay model.

>
> How To
> *Given a set of data, perform exponential regression using a graphing utility.*
>
> Use the *STAT* then *EDIT* menu to enter given data.
>
> Clear any existing data from the lists.
> List the input values in the L1 column.
> List the output values in the L2 column.
>
>
> Graph and observe a scatter plot of the data using the *STATPLOT* feature.
>
> Use *ZOOM* [*9*] to adjust axes to fit the data.
> Verify the data follow an exponential pattern.
>
>
> Find the equation that models the data.
>
> Select “*ExpReg*” from the *STAT* then *CALC* menu.
> Use the values returned for *a* and *b* to record the model, $y=a{b}^{x}.$ 
>
>
> Graph the model in the same window as the scatterplot to verify it is a good fit for the data.

<hr/>

8. **Using Exponential Regression to Fit a Model to Data**    In 2007, a university study was published investigating the crash risk of alcohol impaired driving. Data from 2,871 crashes were used to measure the association of a person’s blood alcohol level (BAC) with the risk of being in an accident.  shows results from the study Source: *Indiana University Center for Studies of Law in Action, 2007*. The *relative risk* is a measure of how many times more likely a person is to crash. So, for example, a person with a BAC of 0.09 is 3.54 times as likely to crash as a person who has not been drinking alcohol.   | *BAC* | 0 | 0.01 | 0.03 | 0.05 | 0.07 | 0.09 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | *Relative Risk of Crashing* | 1 | 1.03 | 1.06 | 1.38 | 2.09 | 3.54 | | *BAC* | 0.11 | 0.13 | 0.15 | 0.17 | 0.19 | 0.21 | | *Relative Risk of Crashing* | 6.41 | 12.6 | 22.1 | 39.05 | 65.32 | 99.78 |   Let $x$ represent the BAC level, and let $y$ represent the corresponding relative risk. Use exponential regression to fit a model to these data. After 6 drinks, a person weighing 160 pounds will have a BAC of about $\mathrm{0.16.}$ How many times more likely is a person with this weight to crash if they drive after having a 6-pack of beer? Round to the nearest hundredth.

<details>
<summary>Solution</summary>

Using the *STAT* then *EDIT* menu on a graphing utility, list the *BAC* values in L1 and the relative risk values in L2. Then use the *STATPLOT* feature to verify that the scatterplot follows the exponential pattern shown in :

![Image](../../media/CNX_Precalc_Figure_04_08_001.jpg)

Use the “*ExpReg*” command from the *STAT* then *CALC* menu to obtain the exponential model,
 $$
y=0.58304829{\left(2.20720213\text{E}10\right)}^{x}
$$ Converting from scientific notation, we have:
 $$
y=0.58304829{\left(\text{22,072,021,300}\right)}^{x}
$$ Notice that ${r}^{2}\approx 0.97$ which indicates the model is a good fit to the data. To see this, graph the model in the same window as the scatterplot to verify it is a good fit as shown in :

![Image](../../media/CNX_Precalc_Figure_04_08_002.jpg)

Use the model to estimate the risk associated with a BAC of $\mathrm{0.16.}$ Substitute $0.16$ for $x$ in the model and solve for $y.$ 

 $\begin{array}{lll}y  & =0.58304829{\left(\text{22,072,021,300}\right)}^{x}  & \text{Use\ the\ regression\ model\ found\ in\ part\ (a)}\text{.}  \\   & =0.58304829{\left(\text{22,072,021,300}\right)}^{0.16}  & \text{Substitute\ 0}\text{.16\ for\}x\text{.}  \\   & \approx \text{26}\text{.35}  & \text{Round\ to\ the\ nearest\ hundredth}\text{.}  \end{array}$ 

If a 160-pound person drives after having 6 drinks, they are about 26.35 times more likely to crash than if driving while sober.
</details>

>
> Try It
> 9. shows a recent graduate’s credit card balance each month after graduation.    | *Month* | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | *Debt ($)* | 620.00 | 761.88 | 899.80 | 1039.93 | 1270.63 | 1589.04 | 1851.31 | 2154.92 |  ⓐ Use exponential regression to fit a model to these data. ⓑ If spending continues at this rate, what will the graduate’s credit card debt be one year after graduating?
>
> <details>
> <summary>Solution</summary>
>
> ⓐ The exponential regression model that fits these data is $y=522.88585984{\left(1.19645256\right)}^{x}.$ 
> ⓑ If spending continues at this rate, the graduate’s credit card debt will be $4,499.38 after one year.
> </details>
>
>

> Q&A
> *Is it reasonable to assume that an exponential regression model will represent a situation indefinitely?*
>
> *No. Remember that models are formed by real-world data gathered for regression. It is usually reasonable to make estimates within the interval of original observation (interpolation). However, when a model is used to make predictions, it is important to use reasoning skills to determine whether the model makes sense for inputs far beyond the original observation interval (extrapolation).*
>

# Building a Logarithmic Model from Data
Just as with exponential functions, there are many real-world applications for logarithmic functions: intensity of sound, pH levels of solutions, yields of chemical reactions, production of goods, and growth of infants. As with exponential models, data modeled by logarithmic functions are either always increasing or always decreasing as time moves forward. Again, it is the *way* they increase or decrease that helps us determine whether a **logarithmic model** is best.
Recall that logarithmic functions increase or decrease rapidly at first, but then steadily slow as time moves on. By reflecting on the characteristics we’ve already learned about this function, we can better analyze real world situations that reflect this type of growth or decay. When performing logarithmic **regression analysis**, we use the form of the logarithmic function most commonly used on graphing utilities, $y=a+b\mathrm{ln}\left(x\right).$ For this function

All input values, $x,$ must be greater than zero.
The point $\left(1,a\right)$ is on the graph of the model.
If $b>0,$ the model is increasing. Growth increases rapidly at first and then steadily slows over time.
If $b<0,$ the model is decreasing. Decay occurs rapidly at first and then steadily slows over time.

>
>
>
>
> **Logarithmic Regression**
>
>
> *Logarithmic regression* is used to model situations where growth or decay accelerates rapidly at first and then slows over time. We use the command “LnReg” on a graphing utility to fit a logarithmic function to a set of data points. This returns an equation of the form,
>  $$
> y=a+b\mathrm{ln}\left(x\right)
> $$ Note that
>
>
> all input values, $x,$ must be non-negative.
> when $b>0,$ the model is increasing.
> when $b<0,$ the model is decreasing.
>

>
> How To
> *Given a set of data, perform logarithmic regression using a graphing utility.*
>
> Use the *STAT* then *EDIT* menu to enter given data.
>
> Clear any existing data from the lists.
> List the input values in the L1 column.
> List the output values in the L2 column.
>
>
> Graph and observe a scatter plot of the data using the *STATPLOT* feature.
>
> Use *ZOOM* [*9*] to adjust axes to fit the data.
> Verify the data follow a logarithmic pattern.
>
>
> Find the equation that models the data.
>
> Select “*LnReg*” from the *STAT* then *CALC* menu.
> Use the values returned for *a* and *b* to record the model, $y=a+b\mathrm{ln}\left(x\right).$ 
>
>
> Graph the model in the same window as the scatterplot to verify it is a good fit for the data.

<hr/>

10. **Using Logarithmic Regression to Fit a Model to Data**    Due to advances in medicine and higher standards of living, life expectancy has been increasing in most developed countries since the beginning of the 20th century.     shows the average life expectancies, in years, of Americans from 1900–2010Source: *Center for Disease Control and Prevention, 2013*.     | *Year* | 1900 | 1910 | 1920 | 1930 | 1940 | 1950 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | *Life Expectancy(Years)* | 47.3 | 50.0 | 54.1 | 59.7 | 62.9 | 68.2 | | *Year* | 1960 | 1970 | 1980 | 1990 | 2000 | 2010 | | *Life Expectancy(Years)* | 69.7 | 70.8 | 73.7 | 75.4 | 76.8 | 78.7 |   ⓐ Let $x$ represent time in decades starting with $x=1$ for the year 1900, $x=2$ for the year 1910, and so on. Let $y$ represent the corresponding life expectancy. Use logarithmic regression to fit a model to these data. ⓑ Use the model to predict the average American life expectancy for the year 2030.

<details>
<summary>Solution</summary>

ⓐ Using the *STAT* then *EDIT* menu on a graphing utility, list the years using values 1–12 in L1 and the corresponding life expectancy in L2. Then use the *STATPLOT* feature to verify that the scatterplot follows a logarithmic pattern as shown in :

![Image](../../media/CNX_Precalc_Figure_04_08_003.jpg)

Use the “*LnReg*” command from the *STAT* then *CALC* menu to obtain the logarithmic model,
 $$
y=42.52722583+13.85752327\mathrm{ln}(x)
$$ 
Next, graph the model in the same window as the scatterplot to verify it is a good fit as shown in :

![Image](../../media/CNX_Precalc_Figure_04_08_004.jpg)

ⓑ To predict the life expectancy of an American in the year 2030, substitute $x=14$ for the in the model and solve for $y:$
 $\begin{array}{lll}y  & =42.52722583+13.85752327\mathrm{ln}(x)  & \text{Use\ the\ regression\ model\ found\ in\ part\ (a)}\text{.}  \\   & =42.52722583+13.85752327\mathrm{ln}(14)  & \text{Substitute\ 14\ for\}x\text{.}  \\   & \approx \text{79}\text{.1}  & \text{Round\ to\ the\ nearest\ tenth.}  \end{array}$ If life expectancy continues to increase at this pace, the average life expectancy of an American will be 79.1 by the year 2030.
</details>

> Try It
> 11. Sales of a video game released in the year 2000 took off at first, but then steadily slowed as time moved on.  shows the number of games sold, in thousands, from the years 2000–2010.     | *Year* | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | | :--- | :--- | :--- | :--- | :--- | :--- | :--- | | *Number Sold (thousands)* | 142 | 149 | 154 | 155 | 159 | 161 | | *Year* | 2006 | 2007 | 2008 | 2009 | 2010 | - | | *Number Sold (thousands)* | 163 | 164 | 164 | 166 | 167 | - |  ⓐ Let $x$ represent time in years starting with $x=1$ for the year 2000. Let $y$ represent the number of games sold in thousands. Use logarithmic regression to fit a model to these data. ⓑ If games continue to sell at this rate, how many games will sell in 2015? Round to the nearest thousand.
>
> <details>
> <summary>Solution</summary>
>
> ⓐ The logarithmic regression model that fits these data is $y=141.91242949+10.45366573\mathrm{ln}(x)$
>
> ⓑ If sales continue at this rate, about 171,000 games will be sold in the year 2015.
> </details>
>
>

# Building a Logistic Model from Data
Like exponential and logarithmic growth, logistic growth increases over time. One of the most notable differences with logistic growth models is that, at a certain point, growth steadily slows and the function approaches an upper bound, or *limiting value*. Because of this, logistic regression is best for modeling phenomena where there are limits in expansion, such as availability of living space or nutrients.
It is worth pointing out that logistic functions actually model resource-limited exponential growth. There are many examples of this type of growth in real-world situations, including population growth and spread of disease, rumors, and even stains in fabric. When performing logistic **regression analysis**, we use the form most commonly used on graphing utilities:
 $$
y=\frac{c}{1+a{e}^{-bx}}
$$ Recall that:
 $\frac{c}{1+a}$ is the initial value of the model.
when $b>0,$ the model increases rapidly at first until it reaches its point of maximum growth rate, $\left(\frac{\mathrm{ln}\left(a\right)}{b},\frac{c}{2}\right).$ At that point, growth steadily slows and the function becomes asymptotic to the upper bound $y=c.$ 
 $c$
is the limiting value, sometimes called the *carrying capacity*, of the model.

>
>
>
>
> **Logistic Regression**
>
>
> *Logistic regression* is used to model situations where growth accelerates rapidly at first and then steadily slows to an upper limit. We use the command “Logistic” on a graphing utility to fit a logistic function to a set of data points. This returns an equation of the form
>  $$
> y=\frac{c}{1+a{e}^{-bx}}
> $$ Note that
>
>
> The initial value of the model is $\frac{c}{1+a}.$ 
> Output values for the model grow closer and closer to $y=c$ as time increases.
>

>
> How To
> *Given a set of data, perform logistic regression using a graphing utility.*
>
> Use the *STAT* then *EDIT* menu to enter given data.
>
> Clear any existing data from the lists.
> List the input values in the L1 column.
> List the output values in the L2 column.
>
>
> Graph and observe a scatter plot of the data using the *STATPLOT* feature.
>
> Use *ZOOM* [*9*] to adjust axes to fit the data.
> Verify the data follow a logistic pattern.
>
>
> Find the equation that models the data.
> Select “*Logistic*” from the *STAT* then *CALC* menu.
> Use the values returned for $a,$ $b,$ and $c$ to record the model, $y=\frac{c}{1+a{e}^{-bx}}.$ 
>
> Graph the model in the same window as the scatterplot to verify it is a good fit for the data.

<hr/>

12. **Using Logistic Regression to Fit a Model to Data**    Mobile telephone service has increased rapidly in America since the mid 1990s. Today, almost all residents have cellular service.  shows the percentage of Americans with cellular service between the years 1995 and 2012 Source: *The World Bank, 2013*.   | Year | Americans with Cellular Service (%) | Year | Americans with Cellular Service (%) | | :--- | :--- | :--- | :--- | | 1995 | 12.69 | 2004 | 62.852 | | 1996 | 16.35 | 2005 | 68.63 | | 1997 | 20.29 | 2006 | 76.64 | | 1998 | 25.08 | 2007 | 82.47 | | 1999 | 30.81 | 2008 | 85.68 | | 2000 | 38.75 | 2009 | 89.14 | | 2001 | 45.00 | 2010 | 91.86 | | 2002 | 49.16 | 2011 | 95.28 | | 2003 | 55.15 | 2012 | 98.17 |    ⓐ Let $x$ represent time in years starting with $x=0$ for the year 1995. Let $y$ represent the corresponding percentage of residents with cellular service. Use logistic regression to fit a model to these data. ⓑ Use the model to calculate the percentage of Americans with cell service in the year 2013. Round to the nearest tenth of a percent. ⓒ Discuss the value returned for the upper limit, $c.$ What does this tell you about the model? What would the limiting value be if the model were exact?

<details>
<summary>Solution</summary>

ⓐ
 Using the *STAT* then *EDIT* menu on a graphing utility, list the years using values 0–15 in L1 and the corresponding percentage in L2. Then use the *STATPLOT* feature to verify that the scatterplot follows a logistic pattern as shown in :

	

![Image](../../media/CNX_Precalc_Figure_04_08_005.jpg)

Use the “*Logistic*” command from the *STAT* then *CALC* menu to obtain the logistic model,
 $$
y=\frac{105.7379526}{1+6.88328979{e}^{-0.2595440013x}}
$$ Next, graph the model in the same window as shown in  the scatterplot to verify it is a good fit:

![Image](../../media/CNX_Precalc_Figure_04_08_006.jpg)

ⓑ
 To approximate the percentage of Americans with cellular service in the year 2013, substitute $x=18$ for the in the model and solve for $y:$

 $\begin{array}{lll}y  & =\frac{105.7379526}{1+6.88328979{e}^{-0.2595440013x}}  & \text{Use\ the\ regression\ model\ found\ in\ part\ (a)}.  \\   & =\frac{105.7379526}{1+6.88328979{e}^{-0.2595440013(18)}}  & \text{Substitute\ 18\ for\}x.  \\   & \approx \text{99}\text{.3\}  & \text{Round\ to\ the\ nearest\ tenth}  \end{array}$
According to the model, about 99.3% of Americans had cellular service in 2013.

ⓒ
The model gives a limiting value of about 105. This means that the maximum possible percentage of Americans with cellular service would be 105%, which is impossible. (How could over 100% of a population have cellular service?) If the model were exact, the limiting value would be $c=100$ and the model’s outputs would get very close to, but never actually reach 100%. After all, there will always be someone out there without cellular service!
</details>

>
> Try It
> 13. shows the population, in thousands, of harbor seals in the Wadden Sea over the years 1997 to 2012.     | Year | Seal Population (Thousands) | Year | Seal Population (Thousands) | | :--- | :--- | :--- | :--- | | 1997 | 3.493 | 2005 | 19.590 | | 1998 | 5.282 | 2006 | 21.955 | | 1999 | 6.357 | 2007 | 22.862 | | 2000 | 9.201 | 2008 | 23.869 | | 2001 | 11.224 | 2009 | 24.243 | | 2002 | 12.964 | 2010 | 24.344 | | 2003 | 16.226 | 2011 | 24.919 | | 2004 | 18.137 | 2012 | 25.108 |  ⓐ Let $x$ represent time in years starting with $x=0$ for the year 1997. Let $y$ represent the number of seals in thousands. Use logistic regression to fit a model to these data. ⓑ Use the model to predict the seal population for the year 2020. ⓒ To the nearest whole number, what is the limiting value of this model?
>
> <details>
> <summary>Solution</summary>
>
> ⓐ The logistic regression model that fits these data is $y=\frac{25.65665979}{1+6.113686306{e}^{-0.3852149008x}}.$ 
> ⓑ If the population continues to grow at this rate, there will be about $\text{25,634}$ seals in 2020.
> ⓒ To the nearest whole number, the carrying capacity is 25,657.
> </details>
>
>

>
> Media
> Access this online resource for additional instruction and practice with exponential function models.
>
> Exponential Regression on a Calculator

# Key Concepts

Exponential regression is used to model situations where growth begins slowly and then accelerates rapidly without bound, or where decay begins rapidly and then slows down to get closer and closer to zero.
We use the command “ExpReg” on a graphing utility to fit function of the form $y=a{b}^{x}$ to a set of data points. See .
Logarithmic regression is used to model situations where growth or decay accelerates rapidly at first and then slows over time.
We use the command “LnReg” on a graphing utility to fit a function of the form $y=a+b\mathrm{ln}\left(x\right)$ to a set of data points. See .
Logistic regression is used to model situations where growth accelerates rapidly at first and then steadily slows as the function approaches an upper limit.
We use the command “Logistic” on a graphing utility to fit a function of the form $y=\frac{c}{1+a{e}^{-bx}}$ to a set of data points. See .

# Section Exercises

## Verbal
1. What situations are best modeled by a logistic equation? Give an example, and state a case for why the example is a good fit.

<details>
<summary>Solution</summary>

Logistic models are best used for situations that have limited values. For example, populations cannot grow indefinitely since resources such as food, water, and space are limited, so a logistic model best describes populations.
</details>

2. What is a carrying capacity? What kind of model has a carrying capacity built into its formula? Why does this make sense?

3. What is regression analysis? Describe the process of performing regression analysis on a graphing utility.

<details>
<summary>Solution</summary>

Regression analysis is the process of finding an equation that best fits a given set of data points. To perform a regression analysis on a graphing utility, first list the given points using the STAT then EDIT menu. Next graph the scatter plot using the STAT PLOT feature. The shape of the data points on the scatter graph can help determine which regression feature to use. Once this is determined, select the appropriate regression analysis command from the STAT then CALC menu.
</details>

4. What might a scatterplot of data points look like if it were best described by a logarithmic model?

5. What does the *y*-intercept on the graph of a logistic equation correspond to for a population modeled by that equation?

<details>
<summary>Solution</summary>

The *y*-intercept on the graph of a logistic equation corresponds to the initial population for the population model.
</details>

## Graphical
For the following exercises, match the given function of best fit with the appropriate scatterplot in  through . Answer using the letter beneath the matching graph.

![Image](../../media/CNX_PreCalc_Figure_04_08_201.jpg)

![Image](../../media/CNX_PreCalc_Figure_04_08_202.jpg)

![Image](../../media/CNX_PreCalc_Figure_04_08_203.jpg)

![Image](../../media/CNX_PreCalc_Figure_04_08_204.jpg)

![Image](../../media/CNX_PreCalc_Figure_04_08_205.jpg)

6. $y=10.209{e}^{-0.294x}$

7. $y=5.598-1.912\mathrm{ln}(x)$

<details>
<summary>Solution</summary>

C
</details>

8. $y=2.104{\left(1.479\right)}^{x}$

9. $y=4.607+2.733\mathrm{ln}(x)$

<details>
<summary>Solution</summary>

B
</details>

10. $y=\frac{14.005}{1+2.79{e}^{-0.812x}}$

## Numeric
11. To the nearest whole number, what is the initial value of a population modeled by the logistic equation $P(t)=\frac{175}{1+6.995{e}^{-0.68t}}?$ What is the carrying capacity?

<details>
<summary>Solution</summary>

$P(0)=22$ ; 175
</details>

12. Rewrite the exponential model $A(t)=1550{\left(1.085\right)}^{x}$ as an equivalent model with base $e.$ Express the exponent to four significant digits.

13. A logarithmic model is given by the equation $h(p)=67.682-5.792\mathrm{ln}\left(p\right).$ To the nearest hundredth, for what value of $p$ does $h(p)=62?$

<details>
<summary>Solution</summary>

$p\approx 2.67$
</details>

14. A logistic model is given by the equation $P(t)=\frac{90}{1+5{e}^{-0.42t}}.$ To the nearest hundredth, for what value of *t* does $P(t)=45?$

15. What is the *y*-intercept on the graph of the logistic model given in the previous exercise?

<details>
<summary>Solution</summary>

*y*-intercept: $\left(0,15\right)$
</details>

## Technology
For the following exercises, use this scenario: The population $P$ of a koi pond over $x$ months is modeled by the function $P(x)=\frac{68}{1+16{e}^{-0.28x}}.$ 
16. Graph the population model to show the population over a span of $3$ years.

17. What was the initial population of koi?

<details>
<summary>Solution</summary>

$4$ koi
</details>

18. How many koi will the pond have after one and a half years?

19. How many months will it take before there are $20$ koi in the pond?

<details>
<summary>Solution</summary>

about $6.8$ months.
</details>

20. Use the intersect feature to approximate the number of months it will take before the population of the pond reaches half its carrying capacity.

For the following exercises, use this scenario: The population $P$ of an endangered species habitat for wolves is modeled by the function $P(x)=\frac{558}{1+54.8{e}^{-0.462x}},$ where $x$ is given in years.
21. Graph the population model to show the population over a span of $10$ years.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_221.jpg)
</details>

22. What was the initial population of wolves transported to the habitat?

23. How many wolves will the habitat have after $3$ years?

<details>
<summary>Solution</summary>

About 38 wolves
</details>

24. How many years will it take before there are $100$ wolves in the habitat?

25. Use the intersect feature to approximate the number of years it will take before the population of the habitat reaches half its carrying capacity.

<details>
<summary>Solution</summary>

About 8.7 years
</details>

For the following exercises, refer to .

| **x** | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **f(x)** | 1125 | 1495 | 2310 | 3294 | 4650 | 6361 |

26. Use a graphing calculator to create a scatter diagram of the data.

27. Use the regression feature to find an exponential function that best fits the data in the table.

<details>
<summary>Solution</summary>

$f\left(x\right)=776.682{\left(1.426\right)}^{x}$
</details>

28. Write the exponential function as an exponential equation with base $e.$

29. Graph the exponential equation on the scatter diagram.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_229.jpg)
</details>

30. Use the intersect feature to find the value of $x$ for which $f(x)=4000.$

For the following exercises, refer to .

| **x** | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **f(x)** | 555 | 383 | 307 | 210 | 158 | 122 |

31. Use a graphing calculator to create a scatter diagram of the data.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_231.jpg)
</details>

32. Use the regression feature to find an exponential function that best fits the data in the table.

33. Write the exponential function as an exponential equation with base $e.$

<details>
<summary>Solution</summary>

$f\left(x\right)={731.92e}^{-0.3038x}$
</details>

34. Graph the exponential equation on the scatter diagram.

35. Use the intersect feature to find the value of $x$ for which $f(x)=250.$

<details>
<summary>Solution</summary>

When
 $f\left(x\right)=250,x\approx 3.6$
</details>

For the following exercises, refer to .

| **x** | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **f(x)** | 5.1 | 6.3 | 7.3 | 7.7 | 8.1 | 8.6 |

36. Use a graphing calculator to create a scatter diagram of the data.

37. Use the LOGarithm option of the REGression feature to find a logarithmic function of the form $y=a+b\mathrm{ln}\left(x\right)$ that best fits the data in the table.

<details>
<summary>Solution</summary>

$y=5.063+1.934\text{log}\left(x\right)$
</details>

38. Use the logarithmic function to find the value of the function when $x=10.$

39. Graph the logarithmic equation on the scatter diagram.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_239.jpg)
</details>

40. Use the intersect feature to find the value of $x$ for which $f(x)=7.$

For the following exercises, refer to .

| **x** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **f(x)** | 7.5 | 6 | 5.2 | 4.3 | 3.9 | 3.4 | 3.1 | 2.9 |

41. Use a graphing calculator to create a scatter diagram of the data.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_241.jpg)
</details>

42. Use the *LOG*arithm option of the *REG*ression feature to find a logarithmic function of the form $y=a+b\mathrm{ln}\left(x\right)$ that best fits the data in the table.

43. Use the logarithmic function to find the value of the function when $x=10.$

<details>
<summary>Solution</summary>

When
 $f\left(10\right)\approx 2.3$
</details>

44. Graph the logarithmic equation on the scatter diagram.

45. Use the intersect feature to find the value of $x$ for which $f(x)=8.$

<details>
<summary>Solution</summary>

When
 $f\left(x\right)=8,x\approx 0.82$
</details>

For the following exercises, refer to .

| **x** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **f(x)** | 8.7 | 12.3 | 15.4 | 18.5 | 20.7 | 22.5 | 23.3 | 24 | 24.6 | 24.8 |

46. Use a graphing calculator to create a scatter diagram of the data.

47. Use the LOGISTIC regression option to find a logistic growth model of the form $y=\frac{c}{1+a{e}^{-bx}}$ that best fits the data in the table.

<details>
<summary>Solution</summary>

$f(x)=\frac{25.081}{1+3.182{e}^{-0.545x}}$
</details>

48. Graph the logistic equation on the scatter diagram.

49. To the nearest whole number, what is the predicted carrying capacity of the model?

<details>
<summary>Solution</summary>

About 25
</details>

50. Use the intersect feature to find the value of $x$ for which the model reaches half its carrying capacity.

For the following exercises, refer to .

| $x$ | 0 | 2 | 4 | 5 | 7 | 8 | 10 | 11 | 15 | 17 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f\left(x\right)$ | 12 | 28.6 | 52.8 | 70.3 | 99.9 | 112.5 | 125.8 | 127.9 | 135.1 | 135.9 |

51. Use a graphing calculator to create a scatter diagram of the data.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_251.jpg)
</details>

52. Use the LOGISTIC regression option to find a logistic growth model of the form $y=\frac{c}{1+a{e}^{-bx}}$ that best fits the data in the table.

53. Graph the logistic equation on the scatter diagram.

<details>
<summary>Solution</summary>

![Image](../../media/CNX_Precalc_Figure_06_08_253.jpg)
</details>

54. To the nearest whole number, what is the predicted carrying capacity of the model?

55. Use the intersect feature to find the value of $x$ for which the model reaches half its carrying capacity.

<details>
<summary>Solution</summary>

When
 $f\left(x\right)=68,x\approx 4.9$
</details>

## Extensions
56. Recall that the general form of a logistic equation for a population is given by $P(t)=\frac{c}{1+a{e}^{-bt}},$ such that the initial population at time $t=0$ is $P(0)={P}_{0}.$ Show algebraically that $\frac{c-P(t)}{P(t)}=\frac{c-{P}_{0}}{{P}_{0}}{e}^{-bt}.$

57. Use a graphing utility to find an exponential regression formula $f(x)$ and a logarithmic regression formula $g(x)$ for the points $\left(1.5,1.5\right)$ and $\left(8.5,\phantom{\rule{0.5em}{0ex}}\text{8.5}\right).$ Round all numbers to 6 decimal places. Graph the points and both formulas along with the line $y=x$ on the same axis. Make a conjecture about the relationship of the regression formulas.

<details>
<summary>Solution</summary>

$f\left(x\right)=1.034341{\left(1.281204\right)}^{x}$
; $g\left(x\right)=4.035510$
; the regression curves are symmetrical about $y=x$
, so it appears that they are inverse functions.
</details>

58. Verify the conjecture made in the previous exercise. Round all numbers to six decimal places when necessary.

59. Find the inverse function ${f}^{-1}\left(x\right)$ for the logistic function $f(x)=\frac{c}{1+a{e}^{-bx}}.$ Show all steps.

<details>
<summary>Solution</summary>

${f}^{-1}\left(x\right)=\frac{\text{ln}(a)-\text{ln}(\frac{c}{x}-1)}{b}$
</details>

60. Use the result from the previous exercise to graph the logistic model $P(t)=\frac{20}{1+4{e}^{-0.5t}}$ along with its inverse on the same axis. What are the intercepts and asymptotes of each function?

# Chapter Review Exercises

## Exponential Functions
14. Determine whether the function $y=156{\left(0.825\right)}^{t}$ represents exponential growth, exponential decay, or neither. Explain

<details>
<summary>Solution</summary>

exponential decay; The growth factor, $0.825,$ is between $0$ and $1.$
</details>

15. The population of a herd of deer is represented by the function $A(t)=205{(1.13)}^{t},$ where $t$ is given in years. To the nearest whole number, what will the herd population be after $6$ years?

16. Find an exponential equation that passes through the points $\text{(2,\ 2}\text{.25)}$ and $(5,60.75).$

<details>
<summary>Solution</summary>

$y=0.25{\left(3\right)}^{x}$
</details>

17. Determine whether  could represent a function that is linear, exponential, or neither. If it appears to be exponential, find a function that passes through the points.     | **x** | 1 | 2 | 3 | 4 | | :--- | :--- | :--- | :--- | :--- | | **f(x)** | 3 | 0.9 | 0.27 | 0.081 |

18. A retirement account is opened with an initial deposit of $8,500 and earns $8.12\%$ interest compounded monthly. What will the account be worth in $20$ years?

<details>
<summary>Solution</summary>

$\mathrm{$}42,888.18$
</details>

19. Hsu-Mei wants to save $5,000 for a down payment on a car. To the nearest dollar, how much will she need to invest in an account now with $7.5\%$ APR, compounded daily, in order to reach her goal in $3$ years?

20. Does the equation $y=2.294{e}^{-0.654t}$ represent continuous growth, continuous decay, or neither? Explain.

<details>
<summary>Solution</summary>

continuous decay; the growth rate is negative.
</details>

21. Suppose an investment account is opened with an initial deposit of $\text{$10,500}$ earning $6.25\%$ interest, compounded continuously. How much will the account be worth after $25$ years?

## Graphs of Exponential Functions
22. Graph the function $f(x)=3.5{\left(2\right)}^{x}.$ State the domain and range and give the *y*-intercept.

<details>
<summary>Solution</summary>

domain: all real numbers; range: all real numbers strictly greater than zero; *y*-intercept: (0, 3.5);

![Graph of f(x)=3.5(2^x)](../../media/CNX_PreCalc_Figure_04_08_229.jpg)
</details>

23. Graph the function $f(x)=4{\left(\frac{1}{8}\right)}^{x}$ and its reflection about the *y*-axis on the same axes, and give the *y*-intercept.

24. The graph of $f(x)={6.5}^{x}$ is reflected about the *y*-axis and stretched vertically by a factor of $7.$ What is the equation of the new function, $g(x)?$ State its *y*-intercept, domain, and range.

<details>
<summary>Solution</summary>

$g(x)=7{\left(6.5\right)}^{-x};$ *y*-intercept: $(0,\phantom{\rule{0.5em}{0ex}}\text{7});$ Domain: all real numbers; Range: all real numbers greater than $0.$
</details>

25. The graph below shows transformations of the graph of $f(x)={2}^{x}.$ What is the equation for the transformation?     ![Image](../../media/CNX_PreCalc_Figure_04_08_231.jpg)

## Logarithmic Functions
26. Rewrite ${\mathrm{log}}_{17}\left(4913\right)=x$ as an equivalent exponential equation.

<details>
<summary>Solution</summary>

${17}^{x}=4913$
</details>

27. Rewrite $\mathrm{ln}\left(s\right)=t$ as an equivalent exponential equation.

28. Rewrite ${a}^{-\phantom{\rule{0.5em}{0ex}}\frac{2}{5}}=b$ as an equivalent logarithmic equation.

<details>
<summary>Solution</summary>

${\mathrm{log}}_{a}b=-\frac{2}{5}$
</details>

29. Rewrite ${e}^{-3.5}=h$ as an equivalent logarithmic equation.

30. Solve for *x* if ${\mathrm{log}}_{64}(x)=\frac{1}{3}$ by converting the logarithmic equation ${\mathrm{log}}_{64}(x)=\frac{1}{3}$ to exponential form.

<details>
<summary>Solution</summary>

$x={64}^{\frac{1}{3}}=4$
</details>

31. Evaluate ${\mathrm{log}}_{5}\left(\frac{1}{125}\right)$ without using a calculator.

32. Evaluate $\mathrm{log}\left(0.000001\right)$ without using a calculator.

<details>
<summary>Solution</summary>

$\mathrm{log}\left(\text{0}\text{.000001}\right)=-6$
</details>

33. Evaluate $\mathrm{log}(4.005)$ using a calculator. Round to the nearest thousandth.

34. Evaluate $\mathrm{ln}\left({e}^{-0.8648}\right)$ without using a calculator.

<details>
<summary>Solution</summary>

$\mathrm{ln}\left({e}^{-0.8648}\right)=-0.8648$
</details>

35. Evaluate $\mathrm{ln}\left(\sqrt[3]{18}\right)$ using a calculator. Round to the nearest thousandth.

## Graphs of Logarithmic Functions
36. Graph the function $g(x)=\mathrm{log}\left(7x+21\right)-4.$

<details>
<summary>Solution</summary>

![Graph of g(x)=log(7x+21)-4.](../../media/CNX_PreCalc_Figure_04_08_232.jpg)
</details>

37. Graph the function $h(x)=2\mathrm{ln}\left(9-3x\right)+1.$

38. State the domain, vertical asymptote, and end behavior of the function $g(x)=\mathrm{ln}\left(4x+20\right)-17.$

<details>
<summary>Solution</summary>

Domain: $x>-5;$ Vertical asymptote: $x=-5;$ End behavior: as $x\to -{5}^{+},f(x)\to -\infty$ and as $x\to \infty ,f(x)\to \infty .$
</details>

## Logarithmic Properties
39. Rewrite $\mathrm{ln}\left(7r\cdot 11st\right)$ in expanded form.

40. Rewrite ${\mathrm{log}}_{8}\left(x\right)+{\mathrm{log}}_{8}\left(5\right)+{\mathrm{log}}_{8}\left(y\right)+{\mathrm{log}}_{8}\left(13\right)$ in compact form.

<details>
<summary>Solution</summary>

${\text{log}}_{8}\left(65xy\right)$
</details>

41. Rewrite ${\mathrm{log}}_{m}\left(\frac{67}{83}\right)$ in expanded form.

42. Rewrite $\mathrm{ln}\left(z\right)-\mathrm{ln}\left(x\right)-\mathrm{ln}\left(y\right)$ in compact form.

<details>
<summary>Solution</summary>

$\mathrm{ln}\left(\frac{z}{xy}\right)$
</details>

43. Rewrite $\mathrm{ln}\left(\frac{1}{{x}^{5}}\right)$ as a product.

44. Rewrite $-{\mathrm{log}}_{y}\left(\frac{1}{12}\right)$ as a single logarithm.

<details>
<summary>Solution</summary>

${\text{log}}_{y}\left(12\right)$
</details>

45. Use properties of logarithms to expand $\mathrm{log}\left(\frac{{r}^{2}{s}^{11}}{{t}^{14}}\right).$

46. Use properties of logarithms to expand $\mathrm{ln}\left(2b\sqrt{\frac{b+1}{b-1}}\right).$

<details>
<summary>Solution</summary>

$\mathrm{ln}\left(2\right)+\mathrm{ln}\left(b\right)+\frac{\mathrm{ln}\left(b+1\right)-\mathrm{ln}\left(b-1\right)}{2}$
</details>

47. Condense the expression $5\mathrm{ln}\left(b\right)+\mathrm{ln}\left(c\right)+\frac{\mathrm{ln}\left(4-a\right)}{2}$ to a single logarithm.

48. Condense the expression $3{\mathrm{log}}_{7}v+6{\mathrm{log}}_{7}w-\frac{{\mathrm{log}}_{7}u}{3}$ to a single logarithm.

<details>
<summary>Solution</summary>

${\mathrm{log}}_{7}\left(\frac{{v}^{3}{w}^{6}}{\sqrt[3]{u}}\right)$
</details>

49. Rewrite ${\mathrm{log}}_{3}\left(12.75\right)$ to base $e.$

50. Rewrite ${5}^{12x-17}=125$ as a logarithm. Then apply the change of base formula to solve for $x$ using the common log. Round to the nearest thousandth.

<details>
<summary>Solution</summary>

$x=\frac{\frac{\mathrm{log}\left(125\right)}{\mathrm{log}\left(5\right)}+17}{12}=\frac{5}{3}$
</details>

## Exponential and Logarithmic Equations
51. Solve ${216}^{3x}\cdot {216}^{x}={36}^{3x+2}$ by rewriting each side with a common base.

52. Solve $\frac{125}{{\left(\frac{1}{625}\right)}^{-x-3}}={5}^{3}$ by rewriting each side with a common base.

<details>
<summary>Solution</summary>

$x=-3$
</details>

53. Use logarithms to find the exact solution for $7\cdot {17}^{-9x}-7=49.$ If there is no solution, write *no solution*.

54. Use logarithms to find the exact solution for $3{e}^{6n-2}+1=-60.$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

no solution
</details>

55. Find the exact solution for $5{e}^{3x}-4=6$ . If there is no solution, write *no solution*.

56. Find the exact solution for $2{e}^{5x-2}-9=-56.$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

no solution
</details>

57. Find the exact solution for ${5}^{2x-3}={7}^{x+1}.$ If there is no solution, write *no solution*.

58. Find the exact solution for ${e}^{2x}-{e}^{x}-110=0.$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

$x=\mathrm{ln}\left(11\right)$
</details>

59. Use the definition of a logarithm to solve. $-5{\mathrm{log}}_{7}\left(10n\right)=5.$

60. Use the definition of a logarithm to find the exact solution for $9+6\mathrm{ln}\left(a+3\right)=33.$

<details>
<summary>Solution</summary>

$a={e}^{4}-3$
</details>

61. Use the one-to-one property of logarithms to find an exact solution for ${\mathrm{log}}_{8}\left(7\right)+{\mathrm{log}}_{8}\left(-4x\right)={\mathrm{log}}_{8}\left(5\right).$ If there is no solution, write *no solution*.

62. Use the one-to-one property of logarithms to find an exact solution for $\mathrm{ln}\left(5\right)+\mathrm{ln}\left(5{x}^{2}-5\right)=\mathrm{ln}\left(56\right).$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

$x=\pm \frac{9}{5}$
</details>

63. The formula for measuring sound intensity in decibels $D$ is defined by the equation $D=10\mathrm{log}\left(\frac{I}{{I}_{0}}\right),$ where $I$ is the intensity of the sound in watts per square meter and ${I}_{0}={10}^{-12}$ is the lowest level of sound that the average person can hear. How many decibels are emitted from a large orchestra with a sound intensity of $6.3\cdot {10}^{-3}$ watts per square meter?

64. The population of a city is modeled by the equation $P(t)=256,114{e}^{0.25t}$ where $t$ is measured in years. If the city continues to grow at this rate, how many years will it take for the population to reach one million?

<details>
<summary>Solution</summary>

about $5.45$ years
</details>

65. Find the inverse function ${f}^{-1}$ for the exponential function $f\left(x\right)=2\cdot {e}^{x+1}-5.$

66. Find the inverse function ${f}^{-1}$ for the logarithmic function $f\left(x\right)=0.25\cdot {\mathrm{log}}_{2}\left({x}^{3}+1\right).$

<details>
<summary>Solution</summary>

${f}^{-1}\left(x\right)=\sqrt[3]{{2}^{4x}-1}$
</details>

## Exponential and Logarithmic Models
For the following exercises, use this scenario: A doctor prescribes $300$ milligrams of a therapeutic drug that decays by about $17\%$ each hour.
67. To the nearest minute, what is the half-life of the drug?

68. Write an exponential model representing the amount of the drug remaining in the patient’s system after $t$ hours. Then use the formula to find the amount of the drug that would remain in the patient’s system after $24$ hours. Round to the nearest hundredth of a gram.

<details>
<summary>Solution</summary>

$f(t)=300{\left(0.83\right)}^{t};$$f(24)\approx 3.43\text{\hspace{0.05em}}\text{\hspace{0.05em}}g$
</details>

For the following exercises, use this scenario: A soup with an internal temperature of $\text{350\xb0}$ Fahrenheit was taken off the stove to cool in a $\text{71\xb0F}$ room. After fifteen minutes, the internal temperature of the soup was $\text{175\xb0F}\text{.}$ 
69. Use Newton’s Law of Cooling to write a formula that models this situation.

70. How many minutes will it take the soup to cool to $\text{85\xb0F?}$

<details>
<summary>Solution</summary>

about $45$ minutes
</details>

For the following exercises, use this scenario: The equation $N\left(t\right)=\frac{1200}{1+199{e}^{-0.625t}}$ models the number of people in a school who have heard a rumor after $t$ days.
71. How many people started the rumor?

72. To the nearest tenth, how many days will it be before the rumor spreads to half the carrying capacity?

<details>
<summary>Solution</summary>

about $8.5$ days
</details>

73. What is the carrying capacity?

For the following exercises, enter the data from each table into a graphing calculator and graph the resulting scatter plots. Determine whether the data from the table would likely represent a function that is linear, exponential, or logarithmic.
74. | **x** | **f(x)** | | :--- | :--- | | 1 | 3.05 | | 2 | 4.42 | | 3 | 6.4 | | 4 | 9.28 | | 5 | 13.46 | | 6 | 19.52 | | 7 | 28.3 | | 8 | 41.04 | | 9 | 59.5 | | 10 | 86.28 |

<details>
<summary>Solution</summary>

exponential

![Graph of the table’s values.](../../media/CNX_PreCalc_Figure_04_08_234.jpg)
</details>

75. | **x** | **f(x)** | | :--- | :--- | | 0.5 | 18.05 | | 1 | 17 | | 3 | 15.33 | | 5 | 14.55 | | 7 | 14.04 | | 10 | 13.5 | | 12 | 13.22 | | 13 | 13.1 | | 15 | 12.88 | | 17 | 12.69 | | 20 | 12.45 |

76. Find a formula for an exponential equation that goes through the points $\left(-2,100\right)$ and $\left(0,4\right).$ Then express the formula as an equivalent equation with base *e.*

<details>
<summary>Solution</summary>

$y=4{\left(0.2\right)}^{x};$ $y=4{e}^{\text{-1.609438}x}$
</details>

## Fitting Exponential Models to Data
77. What is the carrying capacity for a population modeled by the logistic equation $P(t)=\frac{250,000}{1+499{e}^{-0.45t}}?$ What is the initial population for the model?

78. The population of a culture of bacteria is modeled by the logistic equation $\phantom{\rule{0.5em}{0ex}}P(t)=\frac{14,250}{1+29{e}^{-0.62t}},$ where $t$ is in days. To the nearest tenth, how many days will it take the culture to reach $75\%$ of its carrying capacity?

<details>
<summary>Solution</summary>

about $7.2$ days
</details>

For the following exercises, use a graphing utility to create a scatter diagram of the data given in the table. Observe the shape of the scatter diagram to determine whether the data is best described by an exponential, logarithmic, or logistic model. Then use the appropriate regression feature to find an equation that models the data. When necessary, round values to five decimal places.
79. | **x** | **f(x)** | | :--- | :--- | | 1 | 409.4 | | 2 | 260.7 | | 3 | 170.4 | | 4 | 110.6 | | 5 | 74 | | 6 | 44.7 | | 7 | 32.4 | | 8 | 19.5 | | 9 | 12.7 | | 10 | 8.1 |

80. | **x** | **f(x)** | | :--- | :--- | | 0.15 | 36.21 | | 0.25 | 28.88 | | 0.5 | 24.39 | | 0.75 | 18.28 | | 1 | 16.5 | | 1.5 | 12.99 | | 2 | 9.91 | | 2.25 | 8.57 | | 2.75 | 7.23 | | 3 | 5.99 | | 3.5 | 4.81 |

<details>
<summary>Solution</summary>

logarithmic; $y=16.68718-9.71860\mathrm{ln}(x)$ 

![Graph of the table’s values.](../../media/CNX_PreCalc_Figure_04_08_237.jpg)
</details>

81. | **x** | **f(x)** | | :--- | :--- | | 0 | 9 | | 2 | 22.6 | | 4 | 44.2 | | 5 | 62.1 | | 7 | 96.9 | | 8 | 113.4 | | 10 | 133.4 | | 11 | 137.6 | | 15 | 148.4 | | 17 | 149.3 |

# Practice Test
82. The population of a pod of bottlenose dolphins is modeled by the function $A(t)=8{(1.17)}^{t},$ where $t$ is given in years. To the nearest whole number, what will the pod population be after $3$ years?

<details>
<summary>Solution</summary>

About 13 dolphins.
</details>

83. Find an exponential equation that passes through the points $\text{(0, 4)}$ and $\text{(2, 9)}\text{.}$

84. Drew wants to save $2,500 to go to the next World Cup. To the nearest dollar, how much will he need to invest in an account now with $6.25\%$ APR, compounding daily, in order to reach his goal in $4$ years?

<details>
<summary>Solution</summary>

$\mathrm{$}\mathrm{1,947}$
</details>

85. An investment account was opened with an initial deposit of $9,600 and earns $7.4\%$ interest, compounded continuously. How much will the account be worth after $15$ years?

86. Graph the function $f(x)=5{\left(0.5\right)}^{-x}$ and its reflection across the *y*-axis on the same axes, and give the *y*-intercept.

<details>
<summary>Solution</summary>

*y*-intercept: $(0,\phantom{\rule{0.5em}{0ex}}\text{5})$ 

![Graph of f(-x)=5(0.5)^-x in blue and f(x)=5(0.5)^x in orange.](../../media/CNX_PreCalc_Figure_04_08_239.jpg)
</details>

87. The graph shows transformations of the graph of $f(x)={\left(\frac{1}{2}\right)}^{x}.$ What is the equation for the transformation?   ![Graph of f(x)= (1/2)^x.](../../media/CNX_PreCalc_Figure_04_08_240.jpg)

88. Rewrite ${\mathrm{log}}_{8.5}\left(614.125\right)=a$ as an equivalent exponential equation.

<details>
<summary>Solution</summary>

${8.5}^{a}=614.125$
</details>

89. Rewrite ${e}^{\frac{1}{2}}=m$ as an equivalent logarithmic equation.

90. Solve for $x$ by converting the logarithmic equation $lo{g}_{\frac{1}{7}}(x)=2$ to exponential form.

<details>
<summary>Solution</summary>

$x={\left(\frac{1}{7}\right)}^{2}=\frac{1}{49}$
</details>

91. Evaluate $\mathrm{log}(\mathrm{10,000,000})$ without using a calculator.

92. Evaluate $\mathrm{ln}\left(0.716\right)$ using a calculator. Round to the nearest thousandth.

<details>
<summary>Solution</summary>

$\mathrm{ln}\left(0.716\right)\approx -0.334$
</details>

93. Graph the function $g(x)=\mathrm{log}\left(12-6x\right)+3.$

94. State the domain, vertical asymptote, and end behavior of the function $f(x)={\mathrm{log}}_{5}\left(39-13x\right)+7.$

<details>
<summary>Solution</summary>

Domain: $x<3;$ Vertical asymptote: $x=3;$ End behavior: $x\to {3}^{-},f(x)\to -\infty$ and $x\to -\infty ,f(x)\to \infty$
</details>

95. Rewrite $\mathrm{log}\left(17a\cdot 2b\right)$ as a sum.

96. Rewrite ${\mathrm{log}}_{t}\left(96\right)-{\mathrm{log}}_{t}\left(8\right)$ in compact form.

<details>
<summary>Solution</summary>

${\mathrm{log}}_{t}\left(12\right)$
</details>

97. Rewrite ${\mathrm{log}}_{8}\left({a}^{\frac{1}{b}}\right)$ as a product.

98. Use properties of logarithm to expand $\mathrm{ln}\left({y}^{3}{z}^{2}\cdot \sqrt[3]{x-4}\right).$

<details>
<summary>Solution</summary>

$3\phantom{\rule{0.2em}{0ex}}\mathrm{ln}\left(y\right)+2\mathrm{ln}\left(z\right)+\frac{\mathrm{ln}\left(x-4\right)}{3}$
</details>

99. Condense the expression $4\mathrm{ln}(c)+\mathrm{ln}(d)+\frac{\mathrm{ln}\left(a\right)}{3}+\frac{\mathrm{ln}\left(b+3\right)}{3}$ to a single logarithm.

100. Rewrite ${16}^{3x-5}=1000$ as a logarithm. Then apply the change of base formula to solve for $x$ using the natural log. Round to the nearest thousandth.

<details>
<summary>Solution</summary>

$x=\frac{\frac{\mathrm{ln}\left(1000\right)}{\mathrm{ln}\left(16\right)}+5}{3}\approx 2.497$
</details>

101. Solve ${\left(\frac{1}{81}\right)}^{x}\cdot \frac{1}{243}={\left(\frac{1}{9}\right)}^{-3x-1}$ by rewriting each side with a common base.

102. Use logarithms to find the exact solution for $-9{e}^{10a-8}-5=-41$ . If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

$a=\frac{\mathrm{ln}\left(4\right)+8}{10}$
</details>

103. Find the exact solution for $10{e}^{4x+2}+5=56.$ If there is no solution, write *no solution*.

104. Find the exact solution for $-5{e}^{-4x-1}-4=64.$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

no solution
</details>

105. Find the exact solution for ${2}^{x-3}={6}^{2x-1}.$ If there is no solution, write *no solution*.

106. Find the exact solution for ${e}^{2x}-{e}^{x}-72=0.$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

$x=\mathrm{ln}\left(9\right)$
</details>

107. Use the definition of a logarithm to find the exact solution for $4\mathrm{log}\left(2n\right)-7=-11$

108. Use the one-to-one property of logarithms to find an exact solution for $\mathrm{log}\left(4{x}^{2}-10\right)+\mathrm{log}\left(3\right)=\mathrm{log}\left(51\right)$ If there is no solution, write *no solution*.

<details>
<summary>Solution</summary>

$x=\pm \frac{3\sqrt{3}}{2}$
</details>

109. The formula for measuring sound intensity in decibels $D$ is defined by the equation $D=10\mathrm{log}\left(\frac{I}{{I}_{0}}\right),$ where $I$ is the intensity of the sound in watts per square meter and ${I}_{0}={10}^{-12}$ is the lowest level of sound that the average person can hear. How many decibels are emitted from a rock concert with a sound intensity of $4.7\cdot {10}^{-1}$ watts per square meter?

110. A radiation safety officer is working with $112$ grams of a radioactive substance.  After $17$ days, the sample has decayed to $80$ grams. Rounding to five significant digits, write an exponential equation representing this situation. To the nearest day, what is the half-life of this substance?

<details>
<summary>Solution</summary>

$f(t)=112{e}^{-.019792t};$ half-life: about $35$
days
</details>

111. Write the formula found in the previous exercise as an equivalent equation with base $e.$ Express the exponent to five significant digits.

112. A bottle of soda with a temperature of $\text{71\xb0}$ Fahrenheit was taken off a shelf and placed in a refrigerator with an internal temperature of $\text{35\xb0 F}\text{.}$ After ten minutes, the internal temperature of the soda was $\text{63\xb0 F}\text{.}$ Use Newton’s Law of Cooling to write a formula that models this situation. To the nearest degree, what will the temperature of the soda be after one hour?

<details>
<summary>Solution</summary>

$T(t)=36{e}^{-0.025131t}+35;T\left(60\right)\approx {43}^{\text{o}}\text{F}$
</details>

113. The population of a wildlife habitat is modeled by the equation $P\left(t\right)=\frac{360}{1+6.2{e}^{-0.35t}},$ where $t$ is given in years. How many animals were originally transported to the habitat? How many years will it take before the habitat reaches half its capacity?

114. Enter the data from  into a graphing calculator and graph the resulting scatter plot. Determine whether the data from the table would likely represent a function that is linear, exponential, or logarithmic.    | **x** | **f(x)** | | :--- | :--- | | 1 | 3 | | 2 | 8.55 | | 3 | 11.79 | | 4 | 14.09 | | 5 | 15.88 | | 6 | 17.33 | | 7 | 18.57 | | 8 | 19.64 | | 9 | 20.58 | | 10 | 21.42 |

<details>
<summary>Solution</summary>

logarithmic

![Graph of the table’s values.](../../media/CNX_PreCalc_Figure_04_08_242.jpg)
</details>

115. The population of a lake of fish is modeled by the logistic equation $P(t)=\frac{16,120}{1+25{e}^{-0.75t}},$ where $t$ is time in years. To the nearest hundredth, how many years will it take the lake to reach $80\%$ of its carrying capacity?

For the following exercises, use a graphing utility to create a scatter diagram of the data given in the table. Observe the shape of the scatter diagram to determine whether the data is best described by an exponential, logarithmic, or logistic model. Then use the appropriate regression feature to find an equation that models the data. When necessary, round values to five decimal places.
116. | **x** | **f(x)** | | :--- | :--- | | 1 | 20 | | 2 | 21.6 | | 3 | 29.2 | | 4 | 36.4 | | 5 | 46.6 | | 6 | 55.7 | | 7 | 72.6 | | 8 | 87.1 | | 9 | 107.2 | | 10 | 138.1 |

<details>
<summary>Solution</summary>

exponential; $y=15.10062{\left(1.24621\right)}^{x}$ 

![Graph of the table’s values.](../../media/CNX_PreCalc_Figure_04_08_243.jpg)
</details>

117. | **x** | **f(x)** | | :--- | :--- | | 3 | 13.98 | | 4 | 17.84 | | 5 | 20.01 | | 6 | 22.7 | | 7 | 24.1 | | 8 | 26.15 | | 9 | 27.37 | | 10 | 28.38 | | 11 | 29.97 | | 12 | 31.07 | | 13 | 31.43 |

118. | **x** | **f(x)** | | :--- | :--- | | 0 | 2.2 | | 0.5 | 2.9 | | 1 | 3.9 | | 1.5 | 4.8 | | 2 | 6.4 | | 3 | 9.3 | | 4 | 12.3 | | 5 | 15 | | 6 | 16.2 | | 7 | 17.3 | | 8 | 17.9 |

<details>
<summary>Solution</summary>

logistic; $y=\frac{18.41659}{1+7.54644{e}^{-0.68375x}}$ 

![Graph of the table’s values.](../../media/CNX_PreCalc_Figure_04_08_245.jpg)
</details>
