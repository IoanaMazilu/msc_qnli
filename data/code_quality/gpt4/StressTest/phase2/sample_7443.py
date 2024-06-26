petrol_expense_premise = 30
petrol_expense_hypothesis = 60

# the hypothesis talks about the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_expense_premise >= petrol_expense_hypothesis:
    # check if the hypothesis estimate contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
