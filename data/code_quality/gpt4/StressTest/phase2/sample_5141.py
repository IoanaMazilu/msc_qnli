participants_premise = 4
participants_hypothesis = 6

# the hypothesis talks about the number of participants in a race, referenced also in the premise
if participants_hypothesis < participants_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif participants_hypothesis > participants_premise:
    # the premise gives only a specific number of participants
    # any number of participants greater than 'participants_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the number of participants in the hypothesis exactly matches the number of participants in the premise, we can infer entailment
    label = "entailment"

print(label)
