# Logic Locking


## Problem Statement
Information about Oracle:- \
==> "a.out" is a executable file, which acts like Oracle Here. \
==> Oracle takes 11 input (i1,i2,i3,i4,i6,G1,G2,G3,G4,GG1,GG2). \
==> Oracle Gives us 4 Output (o1,o2,o3,o4). 

To run the oracle you have to execute [./a.out 1 2 3 4 5 6 7 8 9 10 11] where value of i1=1,i2=2,i3=3,i4=4,i6=5,G1=6,G2=7,G3=8,G4=9,GG1=10,GG2=11

Information about Obfuscated File:-
==> Obfuscated file is the locked C-Code. \
==> This code is locked with value Key1 to Key7. \
==> You have to find the Correct value of Keys. 


## Oracle

```
./a.out
```

## Locked Code
```
obfuscated.c
```
The file contains the locked logic of the function used by oracle. \
The function 'arf' takes all the inputs as arguments along with 7 keys.

## SMT attack

### Installing dependencies
```
sudo apt-get update
sudo apt-get install python3
pip3 install z3-solver
```
### Running the code

#### Executing Oracle
```
./a.out 1 2 3 4 5 6 7 8 9 10 11
```
The oracle expects 11 arguments passed at runtime.

#### Executing Python code
```
python3 solver.py
```
The DIP values are already added to the solver. Thus, executing the file will provide the values for the keys.
