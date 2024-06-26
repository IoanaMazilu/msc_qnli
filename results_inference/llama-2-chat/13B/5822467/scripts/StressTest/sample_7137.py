# define variables with representative names for the numerical entities in both inputs
balance_premise = Rs.
balance_hypothesis = Rs.
percentage_decrease_premise = 10
percentage_decrease_hypothesis = <60

# extract all quantities as valid numbers (integers or floats)
balance_premise = float(balance_premise)
balance_hypothesis = float(balance_hypothesis)
percentage_decrease_premise = float(percentage_decrease_premise)
percentage_decrease_hypothesis = float(percentage_decrease_hypothesis)

# perform calculations if necessary
balance_hypothesis = balance_hypothesis - (balance_hypothesis * percentage_decrease_hypothesis / 100)

# compare the variables using brief comments to explain what comparison you do
if balance_hypothesis <= balance_premise:
    # check if the estimate of 'balance_hypothesis' contradicts the number of balance reported in the premise
    label = "contradiction"
elif balance_hypothesis > balance_premise:
    # check if the number of balance in the hypothesis is greater than the number of balance reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
