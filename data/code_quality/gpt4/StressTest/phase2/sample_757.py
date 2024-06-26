participants_premise = 2
participants_hypothesis = 3

# the hypothesis talks about the number of participants in a race, referenced also in the premise
if participants_hypothesis <= participants_premise:
    # check if the number of participants in the hypothesis contradicts the estimate of more than 'participants_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants greater than 'participants_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
