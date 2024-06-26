raj_age_future_premise = 42
raj_age_future_hypothesis = 32

# the hypothesis refers to Raj's age in the future, mentioned in the premise
if raj_age_future_hypothesis > raj_age_future_premise:
    # check if the hypothesis age contradicts the maximum age of Raj in the premise
    label = "contradiction"
elif raj_age_future_hypothesis < raj_age_future_premise:
    # the hypothesis age is less than the maximum age of Raj in the premise, so it does not contradict, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis age is equal to the maximum age of Raj in the premise, we can infer entailment
    label = "entailment"

print(label)
