y_premise = 210
y_hypothesis = more_than_210

# the hypothesis refers to the amount of money Michael earned, mentioned in the premise
if y_hypothesis >= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
