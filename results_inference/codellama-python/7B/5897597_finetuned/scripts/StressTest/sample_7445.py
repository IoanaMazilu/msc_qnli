petrol_spending_premise = 30
petrol_spending_hypothesis = 30

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if petrol_spending_hypothesis <= petrol_spending_premise:
    # check if the hypothesis value contradicts the estimate of 'petrol_spending_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
