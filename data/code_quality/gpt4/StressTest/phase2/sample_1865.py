participants_premise = 7
participants_hypothesis = 7

# the hypothesis talks about the number of participants in a cycling race, referenced also in the premise
if participants_hypothesis < participants_premise:
    # check if the hypothesis value contradicts the exact number of participants in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
