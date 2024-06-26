future_age_premise = 18
future_age_hypothesis = 88
past_age = 7

# the hypothesis refers to Molly's age in the future and in the past, mentioned in the premise
if future_age_premise > future_age_hypothesis:
    # check if the estimate of 'future_age_hypothesis' contradicts the future age in the premise
    label = "contradiction"
elif future_age_premise < future_age_hypothesis:
    # check if the future age in the hypothesis is greater than the future age in the premise
    label = "entailment"
else:
    # if the future age in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
