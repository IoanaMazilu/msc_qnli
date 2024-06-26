pink_highlighters_premise = 9
yellow_highlighters_premise = 8
blue_highlighters_premise = 5

pink_highlighters_hypothesis = 7
yellow_highlighters_hypothesis = 8
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of pink, yellow and blue highlighters in the teacher's desk
if pink_highlighters_premise <= pink_highlighters_hypothesis:
    # check if the estimate of 'pink_highlighters_hypothesis' contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis!= yellow_highlighters_premise or blue_highlighters_hypothesis!= blue_highlighters_premise:
    # check if the number of yellow or blue highlighters in the hypothesis contradicts the number of yellow or blue highlighters in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
