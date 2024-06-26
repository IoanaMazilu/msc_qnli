participants_premise = 4
participants_hypothesis = 2

# the hypothesis refers to the number of participants in a race, also mentioned in the premise
if participants_hypothesis > participants_premise:
    # check if the hypothesis value contradicts the number of participants in the premise
    label = "contradiction"
elif participants_hypothesis == participants_premise:
    # check if the number of participants in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # the number of participants in the hypothesis is less than in the premise
    # this doesn't contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
