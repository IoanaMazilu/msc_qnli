pink_highlighters_premise = 9
pink_highlighters_hypothesis = 3
yellow_highlighters_premise = 8
yellow_highlighters_hypothesis = 8
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of highlighters of different colors in the teacher's desk mentioned in the premise
if pink_highlighters_hypothesis!= pink_highlighters_premise or yellow_highlighters_hypothesis!= yellow_highlighters_premise or blue_highlighters_hypothesis!= blue_highlighters_premise:
    # check if the number of highlighters in the hypothesis contradicts the number of highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
