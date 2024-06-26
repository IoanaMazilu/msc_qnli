pink_highlighters_premise = 6
pink_highlighters_hypothesis = 8
yellow_highlighters_premise = 2
yellow_highlighters_hypothesis = 2
blue_highlighters_premise = 4
blue_highlighters_hypothesis = 4

# the hypothesis refers to the number of each color of highlighters mentioned in the premise
if pink_highlighters_premise >= pink_highlighters_hypothesis:
    # check if the 'pink_highlighters_hypothesis' contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters reported in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
