# Premise: Lilly has 10 fish and Rosy has 9 fish.
# Hypothesis: Lilly has 30 fish and Rosy has 9 fish.
# Golden Label: contradiction

lilly_fish_premise = 10
rosy_fish_premise = 9
lilly_fish_hypothesis = 30
rosy_fish_hypothesis = 9

# the hypothesis refers to the number of fish that Lilly and Rosy have, mentioned in the premise
if lilly_fish_hypothesis != lilly_fish_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the number of fish Lilly has in the premise
    label = "contradiction"
elif rosy_fish_hypothesis != rosy_fish_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

