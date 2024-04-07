# Premise: Lilly has less than 70 fish and Rosy has 11 fish.
# Hypothesis: Lilly has 10 fish and Rosy has 11 fish.
# Golden Label: neutral

lilly_fish_premise = 70
lilly_fish_hypothesis = 10
rosy_fish_premise = 11
rosy_fish_hypothesis = 11

# the hypothesis refers to the number of fish Lilly and Rosy have, as mentioned in the premise
if lilly_fish_hypothesis >= lilly_fish_premise:
    # check if the number of fish Lilly has in the hypothesis contradicts the premise
    label = "contradiction"
elif rosy_fish_hypothesis != rosy_fish_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

