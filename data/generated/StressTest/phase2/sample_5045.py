# Premise: Meg and Bob are among the 4 participants in a cycling race.
# Hypothesis: Meg and Bob are among the less than 4 participants in a cycling race.
# Golden Label: contradiction

participants_premise = 4
participants_hypothesis = 4

# the hypothesis talks about the number of participants in a cycling race, which is also mentioned in the premise
if participants_hypothesis >= participants_premise:
    # check if the hypothesis value contradicts the estimate of less than 'participants_hypothesis'
    label = "contradiction"
else:
    # the premise gives an explicit number for the participants
    # any number of participants less than 'participants_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

