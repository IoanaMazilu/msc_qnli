pink_highlighters_premise = 24
pink_highlighters_hypothesis = 64
yellow_highlighters_premise = 28
yellow_highlighters_hypothesis = 28
blue_highlighters_premise = 25
blue_highlighters_hypothesis = 25

# hypothesis refers to the number of each type of highlighters in Kaya's teacher's desk mentioned in the premise
if pink_highlighters_premise > pink_highlighters_hypothesis:
    # check if the number of pink highlighters in the premise contradicts the estimate of less than 'pink_highlighters_hypothesis'
    label = "contradiction"
elif yellow_highlighters_premise != yellow_highlighters_hypothesis:
    # check if the number of yellow highlighters in the premise contradicts the number of yellow highlighters in the hypothesis
    label = "contradiction"
elif blue_highlighters_premise != blue_highlighters_hypothesis:
    # check if the number of blue highlighters in the premise contradicts the number of blue highlighters in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
