# Calculus Solver

## Description
This Python script allows users to perform various calculus operations such as differentiation, basic and definite integration, limits, and double integrals using the `sympy` library.

## Features
- Compute derivatives
- Evaluate indefinite and definite integrals
- Calculate limits
- Solve double integrals (both definite and indefinite)

## Requirements
Ensure you have Python installed along with the required dependency:
```sh
pip install sympy
```

## Usage
Run the script and follow the prompts to enter your desired calculus operation and expression.

```sh
python calculus_solver.py
```

Upon execution, the script will display a menu:
```
      1-Derivatives
      2-Basic Antiderivatives
      3-Definite Integrals
      4-Limits
      5-Double Integrals
      6-Definite Double Integrals
```
Choose an option by entering the corresponding number and follow the prompts to input the expression and variables.

## Example Usage
### Derivative Calculation
```
What Calculus you want to do?: 1
Enter a Problem: x**2
What do you want to solve for: x
```
**Output:**
```
  d     
─────(x²)
  dx    

2⋅x
```

### Definite Integral Calculation
```
What Calculus you want to do?: 3
Enter a Problem: x**2
You Want to solve from: 0
You Want to solve to: 2
What do you want to solve for: x
```
**Output:**
```
  2    
⌠      
⎮ x² dx
⌡      
  0    

8/3
```
![Screenshot 2025-01-29 172142](https://github.com/user-attachments/assets/942f9bac-dfbf-4ef0-84d8-8f9c2cc3fe31)

## Author
Uttkarsh Singh

## License
This project is licensed under the MIT License.

