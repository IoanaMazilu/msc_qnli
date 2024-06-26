petrol_spending_premise = 30
petrol_spending_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_spending_hypothesis <= petrol_spending_premise:
    # check if the hypothesis value contradicts the estimate of more than 'petrol_spending_premise'
    label = "contradiction"
else:
    # the premise gives an exact percentage for the petrol spending
    # any percentage greater than 'petrol_spending_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)