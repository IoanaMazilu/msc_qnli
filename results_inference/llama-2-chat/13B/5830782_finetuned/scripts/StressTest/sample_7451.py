petrol_expense_premise = 30
petrol_expense_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_expense_hypothesis <= petrol_expense_premise:
    # check if the hypothesis value contradicts the estimate of more than 'petrol_expense_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the petrol expense
    # any percentage of petrol expense greater than 'petrol_expense_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
