# Premise: Lilly has 10 fish and Rosy has 8 fish.
# Hypothesis: Lilly has 40 fish and Rosy has 8 fish.
# Golden Label: contradiction

lilly_fish_premise = 10
lilly_fish_hypothesis = 40
rosy_fish_premise = 8
rosy_fish_hypothesis = 8

# the hypothesis refers to the number of fish that Lilly and Rosy have, as mentioned in the premise
if lilly_fish_hypothesis != lilly_fish_premise:
    # check if the number of Lilly's fish in the hypothesis contradicts the number of Lilly's fish reported in the premise
    label = "contradiction"
elif rosy_fish_hypothesis != rosy_fish_premise:
    # check if the number of Rosy's fish in the hypothesis contradicts the number of Rosy's fish reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

