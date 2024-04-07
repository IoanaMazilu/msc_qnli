# Premise: Meg and Bob are among the more than 3 participants in a cycling race.
# Hypothesis: Meg and Bob are among the 8 participants in a cycling race.
# Golden Label: neutral

participants_premise = 3
participants_hypothesis = 8

# the hypothesis talks about the number of participants in a cycling race, referenced also in the premise
if participants_hypothesis <= participants_premise:
    # check if the hypothesis value contradicts the estimate of more than 'participants_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants greater than 'participants_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

