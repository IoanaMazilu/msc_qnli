petrol_income_spent_premise = 30
petrol_income_spent_hypothesis = 80

# the hypothesis refers to the percentage of income Bhanu spends on petrol, mentioned in the premise
if petrol_income_spent_hypothesis <= petrol_income_spent_premise:
    # check if the estimate of 'petrol_income_spent_hypothesis' contradicts the percentage of income spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
