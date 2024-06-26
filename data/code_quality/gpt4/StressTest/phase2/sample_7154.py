pink_highlighters_premise = 9
pink_highlighters_hypothesis = 3
yellow_highlighters_premise = 8
yellow_highlighters_hypothesis = 8
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of pink, yellow, and blue highlighters mentioned in the premise
if pink_highlighters_hypothesis > pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "contradiction"

print(label)
