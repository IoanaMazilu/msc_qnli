jane_age_premise = 54
jane_age_hypothesis = 34

# the hypothesis talks about Jane's age, which is also mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of Jane's age in the premise
    label = "contradiction"
elif jane_age_hypothesis - jane_age_premise > 10:
    # check if the difference between the hypothesis value and the premise value is greater than 10 years
    label = "entailment"
else:
    # if the hypothesis value and the premise value are close, but not exactly equal, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
