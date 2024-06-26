# define variables for the numerical entities in the premise
money_converted_premise = 6359.0
spent_premise = 3485.0

# define variables for the numerical entities in the hypothesis
left_hypothesis = 2870.0

# compute the total amount of money left in the checking account
total_left_premise = money_converted_premise - spent_premise

# check if the amount of money left in the hypothesis contradicts the amount of money left in the premise
if left_hypothesis!= total_left_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
