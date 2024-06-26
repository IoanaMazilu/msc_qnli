pink_highlighters_premise = 9
pink_highlighters_hypothesis = 7
yellow_highlighters_premise = 8
yellow_highlighters_hypothesis = 8
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of each color of highlighters in the teacher's desk
if pink_highlighters_premise <= pink_highlighters_hypothesis:
    # check if the hypothesis statement contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_premise!= yellow_highlighters_hypothesis:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters in the premise
    label = "contradiction"
elif blue_highlighters_premise!= blue_highlighters_hypothesis:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
