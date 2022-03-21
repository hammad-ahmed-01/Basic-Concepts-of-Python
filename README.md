<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="Python.png" alt="Logo" width="190" height="130">
  </a>

  <h1 align="center">Basic Concepts of Python </h1>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><strong>Explore the MDN docs »</strong></a>
    <br />
    
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ul>
    <li><a href="#about-the-repository">About The Repository</a></li>
    <li><a href="#grade-printing">Python Concept 1 - Conditional statements</a></li>
    <li><a href="#bank-withdrawal-and-deposit">Python Concept 2 - Loops and iterations</a></li>
    <li><a href="#matrices">Python Concept 3 - Functions</a></li>
    <li><a href="#list">Python Concept 4 - Lists</a></li>
    <li><a href="#tuple">Python Concept 5 - Tuples</a></li>
  </ul>
</details>

<!-- ABOUT THE REPO -->

## About The Repository

I have added some programs on the basic concepts of Python for starters. The concepts are regarding Functions, conditional statements, iterations, strings, lists, tuples and dictionaries etc.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Grade Printing

In this program, conditional if-else, elif statements are used to produce grades on numbers given by the user.

In the first step, five numbers of floating number datatype in respective subjects are input by the user and stored in five variables.

Then, the numbers are added and stored in a variable sum. Afterwards sum is divided by the total number of subjects i.e, 5 to get the average.

After getting the average in a variable avg, if-else elif condition is used to compare the avg in order to assign grade.

The grades, according to the average marks are A,B,C,D,E and F.

if the average is higher than or equal to 90 and smaller than 100, then it will print grade A.

if the average is higher than or equal to 80 and smaller than 90, then it will print grade B.

if the average is higher than or equal to 70 and smaller than 80, then it will print grade C.

if the average is higher than or equal to 60 and smaller than 70, then it will print grade D.

if the average is higher than or equal to 50 and smaller than 60, then it will print grade E.

if the average is higher than or equal to 0 and smaller than 50, then it will print grade F.

if the average marks are not between 0 to 100, then the else option will be printed, which will give a warning that the numbers entered are wrong.

<p align="right">(<a href="#top">back to top</a>)</p>

## Bank Withdrawal and Deposit

In this program, while-loop is used to repeatedly run the program in a neverending sequence.

In the first step, two variables are initialized with the value 1 and 2 and a while condition is applied that will run the program for an unlimited period.

The balance is taken as input from the user as floating point number and stored in a variable balance.

A condition is given to the user to enter 1 or 2 for Withdrawal or Depositing.

If the user types 1, then a certain amount, to be input by the user, would be withdrawed from the balance entered previously.

If the user types 2, then a certain amount, to be input by the user, would be deposited into the balance entered previously.

<p align="right">(<a href="#top">back to top</a>)</p>

## Matrices

In this program, two matrices of same order are created by input from the user and these matrices are added together to form another matrix.

In the first step, a function matrix1() is defined with m,n as perimeteres. then by using the append function in a for loop, the input values are added in the list on that specific position. 

The elements of the list are printed in position through another for loop to form a matrix.

The function is then called with 5,3 as perimeter.

Another function matrix2() is defined with a,b as perimeteres. then by using the append function in a for loop, the input values are added in the list on that specific position. 

The elements of the list are printed in position through another for loop to form a matrix.

The function is then called with 5,3 as perimeter for the order to remain the same.

Now using the append function in for loop again, the elements of the matrices in alike positions are added to form a list.

The list is then again printed in a sequence to form a matrix through the for loop.

<p align="right">(<a href="#top">back to top</a>)</p>

## List

In this program, a list is made by user input and the Maximum,Minimum,Sum and Average of the list are to be find.

In the first step, a list is made by iterating an append function by user input in a for loop.

Two functions, myMax() and myMin() are defined to find Maximum and Minimum number in the list.

Then these functions are called to be printed.

Sum of the list is found through iterating the list in for loop and then the average is calculated and printed.

<p align="right">(<a href="#top">back to top</a>)</p>

## Tuple

In this program two tuples are made by user input and are compared. Then the Maximum and Minimum of both tuples are found. Also elements are added in the original tuples to create new ones.

A function tup() is defined in order to create tuples. 

In the function, a list is created by user input using apopend functionin a for loop, then the list is converted to tuple.

Both tuples are created using this function tup().

Then the tuples are compared by if-else condition.

In the next step, minimum and maximum of both tuples are printed using built-in functions min() and max().

At the end both tuples undergo addition of elements and new tuples are created and printed. 

<p align="right">(<a href="#top">back to top</a>)</p>
