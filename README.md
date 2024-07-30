# Shortest Path Problem
This was the final project of CS 355 (Data Structures and Algorithms). The project was done with the help of Ethan Nix and Krutivas Pradhan.  

The program gets nodes with weight (representing miles) from a text file. Then, program will turn that text file into a graph. Also, you can view the graph at any time. You are able to select 2 points on the graph and the program uses Dijkstra's Algorithm to find the shortest path. The program then highlights the shortest path red.  

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Program-Overview](#program-overview)

## Installation

You need [Python](https://www.python.org/downloads/) installed on your system. This project requires a few pip package, run the following to install them (after installing python): 
```sh
pip install graphviz
```

```sh
pip install heapq
```

### Option 1: using [git](https://git-scm.com/downloads)
1. Clone the repository:

    ```sh
    git clone https://github.com/LucasHasting/Shortest_Path_Problem.git
    ```

2. Navigate to the project directory and execute the program:

    ```sh
    cd Shortest_Path_Problem
    py driver.py
    ```
### Option 2: without git
1. Download the project as a zip file
2. [Extract the zip file](https://www.wikihow.com/Unzip-a-File)
3. In windows, the subnetting.py file can be clicked to execute

#### Run from the command line
1. Find the location of the files
2. Copy the path
3. go to the command line and run the following:
   ```sh
   cd /path/to/files
   py driver.py
   ```

## Usage

## Example

![EXAMPLE](example.png)

## Program-Overview

