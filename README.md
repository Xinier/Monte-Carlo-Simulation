# Monte Carlo Simulation
A simulation to predict budgeting cost for sales commission using Monte Carlo.

<img src="https://media.istockphoto.com/vectors/business-observation-and-prediction-businessman-standing-in-front-of-vector-id1229705491?k=20&m=1229705491&s=612x612&w=0&h=iis9KrOEbBEDtLFtQxaF9Hw0n8vnIPl7bYYEdgNC8No=" />

## General Information
For this simulation, we will try to predict how much money we should budget for sales commissions for the next year.
Sales commissions can be a large selling expense and it is important to plan appropriately for this expense.
Therefore, build a Monte Carlo simulation using prior years’ commissions payments to predict the range of potential values for a sales compensation budget.

Number of sales agent = 500

Number of simulation = 1,000

- Actual Sales: Sales Target * Percent to Target
- Commission Amount: Actual Sales * Commission Rate
- Percent to Target: Assumed normally distributed with a mean of 1 and standard deviation of 0.1
- Sales Target and Probability based on the table:

Sales Target | 75,000 | 100,000 | 200,000 | 300,000 | 400,000 | 500,000
--- | --- | --- | --- | --- | --- | --- 
Probability | 0.30 | 0.30 | 0.20 | 0.10 | 0.05 | 0.05  


- Commission rate based on the table:

Percent To Plan | 0-90% | 91-99% | >=100%
--- | --- | --- | ---  
Commission Rate | 2% | 3% | 4%  

## Reference 

https://pbpython.com/monte-carlo.html

Created Jan 2020
