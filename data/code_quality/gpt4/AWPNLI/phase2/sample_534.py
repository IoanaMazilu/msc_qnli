birds_initially_premise = 12.0
birds_fly_away_premise = 8.0
birds_hypothesis = 4.0

# the hypothesis refers to the number of birds, which are also mentioned in the premise
# compute the remaining number of birds in the premise
birds_remaining_premise = birds_initially_premise - birds_fly_away_premise
if birds_hypothesis != birds_remaining_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds remaining from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
