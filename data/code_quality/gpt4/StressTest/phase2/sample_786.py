petrol_expense_premise = 30
house_rent_expense_premise = 30
petrol_expense_hypothesis = 60

# the hypothesis talks about the expenses of Bhanu, which are also referenced in the premise
if petrol_expense_hypothesis >= petrol_expense_premise:
    # check if the estimate of 'petrol_expense_hypothesis' contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)