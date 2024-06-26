petrol_spending_premise = 10
petrol_spending_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if petrol_spending_hypothesis <= petrol_spending_premise:
    # check if the petrol spending percentage in the hypothesis contradicts the estimate of more than 'petrol_spending_premise' from the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the petrol spending percentage
    # any petrol spending percentage greater than 'petrol_spending_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
