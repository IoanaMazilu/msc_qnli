petrol_expense_premise = 30
petrol_expense_hypothesis = 80

# the hypothesis talks about the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_expense_hypothesis >= petrol_expense_premise:
    # check if the hypothesis value contradicts the estimate of 'petrol_expense_premise'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
