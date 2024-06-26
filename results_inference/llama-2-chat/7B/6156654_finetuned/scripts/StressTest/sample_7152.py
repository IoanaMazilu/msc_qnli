pink_highlighters_premise = 9
yellow_highlighters_premise = 8
blue_highlighters_premise = 5

more_than_7_pink_highlighters_hypothesis = 7
more_than_7_yellow_highlighters_hypothesis = 7
more_than_7_blue_highlighters_hypothesis = 7

# the hypothesis talks about the number of highlighters in the desk, which is also mentioned in the premise
if pink_highlighters_premise <= 7 and yellow_highlighters_premise <= 7 and blue_highlighters_premise <= 7:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif pink_highlighters_premise > more_than_7_pink_highlighters_hypothesis or yellow_highlighters_premise > more_than_7_yellow_highlighters_hypothesis or blue_highlighters_premise > more_than_7_blue_highlighters_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
