pink_highlighters_premise = 8
pink_highlighters_hypothesis = 6
yellow_highlighters_premise = 2
yellow_highlighters_hypothesis = 2
blue_highlighters_premise = 4
blue_highlighters_hypothesis = 4

# the hypothesis specifies the number of each type of highlighter mentioned in the premise
if pink_highlighters_hypothesis >= pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the estimate of less than 'pink_highlighters_premise'
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters reported in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
