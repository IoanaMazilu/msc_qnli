john_future_age_premise = 5
john_future_age_hypothesis = 8

# the hypothesis refers to the future age of John and Frank mentioned in the premise
if john_future_age_premise > john_future_age_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'john_future_age_hypothesis' years
    label = "contradiction"
elif john_future_age_premise < john_future_age_hypothesis:
    # if the premise value is less than the hypothesis estimate, we can infer entailment
    label = "entailment"
else:
    # if the premise value is equal to the hypothesis estimate, we can infer neutrality
    label = "neutral"

print(label)
