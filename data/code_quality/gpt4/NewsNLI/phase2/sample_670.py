ashton_tries = 2
flood_conversion_kicks = 2
flood_penalty_kicks = 3
wilkinson_penalty = 1

flood_points_premise = flood_conversion_kicks * 2 + flood_penalty_kicks * 3
wilkinson_points_premise = wilkinson_penalty * 3

flood_points_hypothesis = 13
wilkinson_points_hypothesis = 3

# the hypothesis refers to the points scored by Toby Flood and Jonny Wilkinson, which are also mentioned in the premise
if flood_points_hypothesis != flood_points_premise:
    # check if the points scored by Toby Flood in the hypothesis contradicts the points scored by Toby Flood in the premise
    label = "contradiction"
elif wilkinson_points_hypothesis != wilkinson_points_premise:
    # check if the points scored by Jonny Wilkinson in the hypothesis contradicts the points scored by Jonny Wilkinson in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
