# Premise: Meg and Bob are among the less than 8 participants in a cycling race.
# Hypothesis: Meg and Bob are among the 7 participants in a cycling race.
# Golden Label: neutral

participants_premise = 8
participants_hypothesis = 7

# the hypothesis refers to the number of participants in a cycling race, which is also mentioned in the premise
if participants_hypothesis >= participants_premise:
    # check if the hypothesis value contradicts the upper estimate of less than 'participants_premise'
    label = "contradiction"
elif participants_hypothesis < participants_premise:
    # if the number of participants in the hypothesis is less than 'participants_premise', we can infer entailment
    label = "entailment"

print(label)

