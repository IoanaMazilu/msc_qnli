# Premise: Lucy has an aquarium with 212.0 fish and she wants to buy 68.0 more fish.
# Hypothesis: Lucy would have 284.0 fish then.
# Golden Label: contradiction

current_fish_premise = 212.0
buy_fish_premise = 68.0
total_fish_hypothesis = 284.0

# the hypothesis refers to the total number of fish, which is also calculated in the premise
# compute the total number of fish in the premise
total_fish_premise = current_fish_premise + buy_fish_premise
if total_fish_hypothesis != total_fish_premise:
    # check if the total number of fish in the hypothesis contradicts the total number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

