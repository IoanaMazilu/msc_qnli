# Premise: Lucy has a tank with 212.0 fish and she moves 68.0 of them into a different tank.
# Hypothesis: 144.0 are left in the first tank.
# Golden Label: entailment

total_fish_premise = 212.0
moved_fish_premise = 68.0
left_fish_hypothesis = 144.0

# the hypothesis refers to the number of fish left in the first tank, which can be computed from the premise
# compute the number of fish left in the first tank after Lucy moved some of them
left_fish_premise = total_fish_premise - moved_fish_premise
if left_fish_hypothesis != left_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

