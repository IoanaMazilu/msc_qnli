he_future_age_premise = 5/3
he_future_age_hypothesis = 7/3
tom_age_premise = 6

# the hypothesis refers to the future age of 'He' mentioned in the premise
if he_future_age_premise <= he_future_age_hypothesis:
    # check if the estimate of 'he_future_age_hypothesis' contradicts the future age of 'He' in the premise
    label = "contradiction"
elif he_future_age_premise > he_future_age_hypothesis:
    # check if the future age of 'He' in the premise contradicts the estimate of 'he_future_age_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
