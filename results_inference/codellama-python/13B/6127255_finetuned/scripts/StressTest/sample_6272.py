participants_premise = 7
participants_hypothesis = 2

# the hypothesis talks about the number of participants in a cycling race, referenced also in the premise
if participants_hypothesis == participants_premise:
    # check if the number of participants in the hypothesis is the same as in the premise
    label = "entailment"
elif participants_hypothesis < participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants greater than 'participants_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
