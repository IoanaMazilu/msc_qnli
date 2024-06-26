petrol_expense_percentage_premise = 30
petrol_expense_percentage_hypothesis = 30

# the hypothesis talks about the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_expense_percentage_hypothesis > petrol_expense_percentage_premise:
    # check if the hypothesis value contradicts the exact percentage of income Bhanu spends on petrol in the premise
    label = "contradiction"
else:
    # the premise gives an exact percentage for the petrol expenses
    # any percentage of income spent on petrol less than or equal to 'petrol_expense_percentage_premise' is consistent with the premise
    # but if the hypothesis suggests an exact percentage equal to 'petrol_expense_percentage_premise', we can infer entailment
    label = "entailment"

print(label)
