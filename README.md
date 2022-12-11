# Calculator for Matrix and Algebra

This is Text-based user interface program that use to solve matrix and algebra problems.

## Table of Content
- [Calculator for Matrix and Algebra](#calculator-for-matrix-and-algebra)
  - [Table of Content](#table-of-content)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirement](#requirement)
  - [Program design](#program-design)
  - [Code structure](#code-structure)
  - [Install and Usage](#install-and-usage)
  - [Guide/Documentation](#guidedocumentation)
    - [Polynomial](#polynomial)
  - [Contributing](#contributing)


## Overview

...

## Features

**Calculator for Matrix and Algebra** provide the following function.

- Ability to solve for basic quadratic, cubic and quartic function.
- Calculate operations of Polynomial function e.g. +/-/*/÷/^.
- Calculate operations of Matrix e.g. Inverse/Tranpose/Basic Operation/Determinant.
- Evaluate the expression(No Variable) that has complex parentheses.
- Some basic algebra operation. e.g. Find reduce form of Fraction etc.

## Requirement
This program has been created in **Python 3.10.5** and has the following built-in module.
- [ast](https://docs.python.org/3/library/ast.html) : Abstract Syntax Trees
- [math](https://docs.python.org/3/library/math.html)

## Program design

...

## Code structure

...

## Install and Usage

Clone this repository and run the **main.py**

````
$ git clone https://github.com/Sosokker/Algebraic-Solving-Tool
````

## Guide/Documentation

After the running of the **main.py**. You can type the command and input into the terminal that look like this.
````
[1] <- This is line-count.
````
There are two types of command, input style.\
*No need expression command* and *Need expression command.*

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***Command*** 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***or*** 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***Command[expression]***

Whitespace and Case are not matter. Command is same as command.

For example.
````py
[1] history
# RESULT OF THE INPUT COMMAND
[2] det[[1,2],[3,4]]
# RESULT OF THE INPUT COMMAND
````
Every command you put in and result of it will be save in **history.json** file.

### Polynomial
&nbsp;&nbsp;&nbsp;&nbsp;Polynomial in this class is store in form of array. This are the following command.
- <span style="color:yellow">Polynomial[<span style="color:lightblue">expression</span>]</span>
-> expression str or list

  - This Command use to print all property of the polynomial that user input.

  ````
  [1] polynomial[x^2+2x+1]
  
  ````


## Contributing

Pull requests are always welcome and that would be a honor. This first Python project I've dones. I practice using OOP and using github in this work so  many parts of code look a bit messy. 🙈

Thank you so much.



