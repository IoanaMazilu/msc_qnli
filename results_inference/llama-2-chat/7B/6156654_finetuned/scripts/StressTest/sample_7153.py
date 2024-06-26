pink_highlighters_premise = 7
yellow_highlighters_premise = 8
blue_highlighters_premise = 5
pink_highlighters_hypothesis = 9
yellow_highlighters_hypothesis = 8
blue_highlighters_hypothesis = 5

# the hypothesis talks about the number of highlighters in the teacher's desk, which is also mentioned in the premise
if pink_highlighters_hypothesis!= pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis!= yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis!= blue_highlighters_premise:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
