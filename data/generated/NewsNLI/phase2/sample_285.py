# Premise: Each Spurs victory was by at least 15 points.
# Hypothesis: Each win was by 15 points or more.
# Golden Label: entailment

victory_points_premise = 15
victory_points_hypothesis = 15

# the hypothesis mentions the margin of victory in each game, which is also mentioned in the premise
if victory_points_hypothesis != victory_points_premise:
    # check if the margin of victory in the hypothesis contradicts the margin of victory stated in the premise
    label = "contradiction"
else:
    # if the margin of victory in the hypothesis does not contradict the margin of victory in the premise, we can infer entailment
    label = "entailment"

print(label)

