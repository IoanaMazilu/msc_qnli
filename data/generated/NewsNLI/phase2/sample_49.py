# Premise: It ended Lorenzo's two-race winning streak and boosted Marquez's overall advantage to a substantial 39 points with only four races remaining.
# Hypothesis: With four races remaining, Marc Marquez leads the MotoGP standings by 39 points.
# Golden Label: entailment

winning_streak_premise = 2
advantage_premise = 39
remaining_races_premise = 4

advantage_hypothesis = 39
remaining_races_hypothesis = 4

# the hypothesis mentions the points lead and remaining races, which are also mentioned in the premise
if advantage_hypothesis != advantage_premise:
    # check if the points lead in the hypothesis contradicts the points lead reported in the premise
    label = "contradiction"
elif remaining_races_hypothesis != remaining_races_premise:
    # check if the number of remaining races from the hypothesis contradicts the number of remaining races in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

