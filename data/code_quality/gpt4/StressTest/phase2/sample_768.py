raj_age_future_premise = 32
raj_age_future_hypothesis = 42

# the hypothesis talks about the age of Raj in the future, also mentioned in the premise
if raj_age_future_hypothesis < raj_age_future_premise:
    # check if the hypothesis value contradicts the age of Raj in the future mentioned in the premise
    label = "contradiction"
elif raj_age_future_hypothesis > raj_age_future_premise:
    # the hypothesis value is greater than the premise one, but it does not contradict it
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
