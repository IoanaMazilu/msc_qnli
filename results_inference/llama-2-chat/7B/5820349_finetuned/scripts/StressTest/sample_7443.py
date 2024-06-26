petrol_expense_premise = 30
petrol_expense_hypothesis = 60

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # check if the estimate of 'petrol_expense_hypothesis' contradicts the percentage of petrol expense in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
