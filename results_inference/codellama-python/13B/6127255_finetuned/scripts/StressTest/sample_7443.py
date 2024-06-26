income_petrol_premise = 30
income_petrol_hypothesis = 60

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if income_petrol_hypothesis <= income_petrol_premise:
    # check if the estimate of 'income_petrol_hypothesis' contradicts the percentage spent on petrol in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
