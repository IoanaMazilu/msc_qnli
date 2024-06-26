petrol_income_premise = 60
petrol_income_hypothesis = 30

# the hypothesis refers to the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_income_hypothesis >= petrol_income_premise:
    # check if the percentage of income spent on petrol in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of income spent on petrol in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)