pink_highlighters_premise = 4
pink_highlighters_hypothesis = 3
yellow_highlighters_premise = 2
yellow_highlighters_hypothesis = 2
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis talks about the number of pink, yellow and blue highlighters in Kaya's teacher's desk, mentioned also in the premise
if pink_highlighters_hypothesis != pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the number of pink highlighters reported in the premise
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
