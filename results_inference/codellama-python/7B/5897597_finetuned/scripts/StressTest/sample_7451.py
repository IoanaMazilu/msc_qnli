petrol_spending_premise = 30
petrol_spending_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if petrol_spending_hypothesis <= petrol_spending_premise:
    # check if the hypothesis value contradicts the estimate of 'petrol_spending_premise'
    label = "contradiction"
else:
    # the premise gives the exact percentage of income Bhanu spends on petrol
    # any percentage greater than 'petrol_spending_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
