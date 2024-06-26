petrol_income_premise = 30
petrol_income_hypothesis = 80

# the hypothesis refers to the percentage of income spent on petrol, which is also mentioned in the premise
if petrol_income_hypothesis < petrol_income_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif petrol_income_hypothesis == petrol_income_premise:
    # check if the hypothesis value equals the premise value
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
