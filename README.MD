## Bubbler
This is a sample package to sort an array using bubble sort. 

## Usage
- Create Virtual Environment
```sh
pip install virtualenv
virtualenv -p python3 .
source bin/activate
```
- Install Package
```sh
pip install yuzhuhwbubbler==0.0.1
```
- Use as Module
```py
from yuzhuhwbubbler import bubbleSort

arr = [31, 2, 11, 23, 8, 7, 11,14,20]
 
bubbleSort(arr)
 
print ("sorted:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
```