income_petrol_premise = 30
income_petrol_hypothesis = 10

# the hypothesis refers to the percentage of income Bhanu spends on petrol, which is also mentioned in the premise
if income_petrol_hypothesis >= income_petrol_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
