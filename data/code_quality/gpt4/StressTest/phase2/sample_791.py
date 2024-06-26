apples_eaten_premise = 4
apples_eaten_hypothesis = 4
ratio_premise = 3 / 2
ratio_hypothesis = 3 / 2

# the hypothesis refers to the number of eaten apples and the ratio after eating, mentioned in the premise
if apples_eaten_hypothesis != apples_eaten_premise:
    # check if the number of eaten apples in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
