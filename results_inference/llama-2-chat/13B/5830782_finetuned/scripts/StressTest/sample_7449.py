petrol_expense_premise = 30
petrol_expense_hypothesis = 80

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # check if the hypothesis estimate contradicts the petrol expense percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
