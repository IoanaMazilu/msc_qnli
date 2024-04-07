# Premise: Meg and Bob are among the 3 participants in a cycling race.
# Hypothesis: Meg and Bob are among the less than 4 participants in a cycling race.
# Golden Label: entailment

participants_premise = 3
participants_hypothesis = 4

# the hypothesis talks about the number of participants in a cycling race, referenced also in the premise
if participants_hypothesis < participants_premise:
    # check if the hypothesis value contradicts the number of 'participants_premise'
    label = "contradiction"
elif participants_premise != participants_hypothesis:
    # check if the number of participants in the hypothesis is different from the number of participants mentioned in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

