time_premise = 7 * 24 * 60 + 1 # convert days to minutes
time_hypothesis = 6 * 24 * 60 + 1

# the hypothesis refers to the time required by a train to cover the distance between Chennai and Jammu, also mentioned in the premise
if time_hypothesis >= time_premise:
    # check if the hypothesis value contradicts the exact time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
