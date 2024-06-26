current_age_premise = 18
future_age_premise = 6 * current_age_premise
future_age_hypothesis = 88

# the hypothesis refers to the future age of Molly, which is also mentioned in the premise
# the premise does not mention the current age of Molly
if future_age_hypothesis <= future_age_premise:
    # check if the future age in the hypothesis contradicts the estimate of 'future_age_premise'
    label = "contradiction"
elif current_age_premise <= future_age_hypothesis:
    # check if the current age in the premise contradicts the future age in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
