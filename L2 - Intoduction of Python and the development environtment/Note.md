# Basic of Python
## Table of contents
* [History of Python](#history-of-Python)
* [Features of Python](#history-of-Python)
* [Setup Python Environment on ECS](#history-of-Python)
* [Python Example Program: Echo](#history-of-Python)

## History of Python
[gambar]
### Why Python
* Python is an interpreted, object-oriented, dynamic, high level programming language
* Python is the language of choice for data analyst and the language of choice for smart hardware.

### The Birth of the Python Language

### Python 2.X VS 3.X
* Python 2.0 was released in October 2000 amd as of 2022 python2 will no longer be maintained
* Python 3.0 was released in December 2008, this version was not fully compatible with Python 2.0
* Python divided into two camps: the Python 3.5 faction and the Python 2.7 faction.
#### Major differences:
* Python3 has built-in support for Unicode characters
* Python3 uses absolute paths for import
* Python3 uses stricted indentation
* `print`, `exec` and other statements are replaced with corresponding functions.

## Features of Python
### Advantages of Python
#### Advantage 1 : Simplicity
&nbsp;&nbsp; Python follows the "simple, elegant, and clear" design philosophy.
#### Advantage 2 : Rich standard library
&nbsp;&nbsp; A comprehensive librari covering networking, IO, database, graphics systems, XML processing, and much more.
#### Advantage 3 : High-level programming language
&nbsp;&nbsp; Python is high-level language that **sacrifices performace for the efficiency** as opposed to C.
#### Advantage 4 : Free and Open Source
&nbsp;&nbsp; Python is one of the FLOSS (Free/Open Source Software), which allows free distribution of software, reading and modifying its source code,
and using parts of it freely in new free software.
#### Advantage 5 : Compile and execute
&nbsp;&nbsp; Python is an interpreted language and executes as it is compiled.

#### Advantage 6 : Portability and embeddability
&nbsp;&nbsp; The source code can run on any OS as long as the Python interpreter exists on it, making it portable.
Python can be embedded in C and C++ to provide scripting functionality to them.
     
### Disadvantages of Python
* Slow running speed
* indentation rules
* multi-thread disaster | There is a global lock in Cpython interpreter, allowing only one thread of code execution.
* hard to encript | Unlike compiled languages where the code is compiled into an executable, Python runs the code directly, so it's more difficult to encrypt the code.
 
 ### The Zen of Python
 [gambar]
 
 <hr>

## Python Development Environment and Package Management
 * Runtimen environment and package management tool: <br>
 	Anaconda for Python installation, environment configuration, and package management.
 * Python development Environment
 	* IPython
 	* Qt Console
 	* PyCharm
 	* Jupyter Notebook
 	* Spyder
 * **NOTE** <br>
	* **Runtime environment** is  the environment that a Python program depends on so that it is possible to run on a computer system.
	* **Python development environment**: the environment inside which we can develop Python programs, and usually provides a run-time environment.
 ### IPython | Python Development Environment
 [gambar]

 ### Qt Console | Python Development Environment

 ### Jupyter | Python Development Environment

 ### PyCharm & Spyder | Integrated Development Environment (IDE)
 * **An integrated development environment** is a dekstop software and it provides all the tools for development, from source code writing, running and debugging the program, even package management.
 ### Anaconda | Python Development Environment and Package Management Tool


## Setup Python Environment on ECS
* ECS : Elastic Compute Service from Alibaba Cloud
<br>
[gambar]
 
 ## Python Example Program: Echo
 ### Python Example 1 | Echo
 * Get the user from console and print the same content to the console.
 * Thus, it's called echo
 * code

 ### Python Example 2 | Fibonacci Numbers
 * In math, the Fibonacci numbers form a sequence such that each number is the sum of the 2 preceding numbers, starting from 0 and 1. That is $F_n = F_{n-1} + F_{n-2}$, dan $n \geq 2$. The sequence formed by Fibonacci numbers is called the Fibonacci sequence.
 * Find the sum of the Fibonacci sequence containing $N$ elements. 
 * code

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   