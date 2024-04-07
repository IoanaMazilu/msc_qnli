# Premise: Lilly has 10 fish and Rosy has 11 fish.
# Hypothesis: Lilly has 30 fish and Rosy has 11 fish.
# Golden Label: contradiction

lilly_fish_premise = 10
rosy_fish_premise = 11
lilly_fish_hypothesis = 30
rosy_fish_hypothesis = 11

# the hypothesis talks about the number of fishes Lilly and Rosy have, which is also mentioned in the premise
if lilly_fish_hypothesis != lilly_fish_premise:
    # check if the number of fishes Lilly has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif rosy_fish_hypothesis != rosy_fish_premise:
    # check if the number of fishes Rosy has in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

