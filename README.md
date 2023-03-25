# 8-puzzle-solver
My AI programs written in Python to solve 8-puzzle using the following searching algotirhms:
* "**IDS.py**": Iterative Deepening Search Algorithm
* "**A\*.py**": A\* search Algorithm
## Initialization
**Cutumized Start State:**
* Input a list of 9 numbers (0-8). 
* The first number will be the first tile in the first row, the second number will be the second tile in the first row, the fourth number will be the first tile in the second row and so on. 
* 0 represents the empty tile. 
* Default state will be used instead for invalid inputs.
<p>For example, input 9 numbers in the format:
  
  ```
2 1 0 8 3 4 7 6 5
  ```
 <p aligin="left"><table>
    <caption>will create the following state </caption>
    <tr>
      <td>2</td> <td>1</td> <td>0</td>
    </tr>
    <tr>
      <td>8</td> <td>3</td> <td>4</td>
    </tr>
    <tr>
      <td>7</td> <td>6</td> <td>5</td>
    </tr>
  </table>
  </td>
  <td>

  <table>
    <caption><b> Default start state </caption>
      <tr>
      <td>7</td> <td>2</td> <td>4</td>
      </tr>
      <tr>
        <td>5</td> <td>0</td> <td>6</td>
      </tr>
      <tr>
        <td>8</td> <td>3</td> <td>1</td>
      </tr>
      </table>


<table>
  <caption><b> Goal State </caption>
  <tr>
    <td>0</td> <td>1</td> <td>2</td>
  </tr>
  <tr>
    <td>3</td> <td>4</td> <td>5</td>
  </tr>
  <tr>
    <td>6</td> <td>7</td> <td>8</td>
  </tr>
</table>
<hr>
	
### Iterative Deepening Search
* Program ends if solution is found or search limit exceeded, ie. 1,000,000 nodes expanded. 


### A* Search
It will ask to choose the heuristics for A* search,
* h1 = the number of misplaced tiles
* h2 = the sum of Manhattan distances
* Program ends if solution is found.
