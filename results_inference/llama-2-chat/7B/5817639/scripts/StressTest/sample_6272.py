participants_premise = 7
participants_hypothesis = 2

# the hypothesis refers to a smaller number of participants than the premise
if participants_hypothesis <= participants_premise:
    # check if the hypothesis value contradicts the estimate of 'participants_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants greater than 'participants_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
