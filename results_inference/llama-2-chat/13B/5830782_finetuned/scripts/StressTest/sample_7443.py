petrol_expense_premise = 30
petrol_expense_hypothesis = 60

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
