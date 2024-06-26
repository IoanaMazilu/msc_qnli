jessica_text_speed_premise = 95
maurice_text_speed_premise = 10
jessica_text_speed_hypothesis = 75
maurice_text_speed_hypothesis = 10

# the hypothesis refers to the texting speed of Jessica and Maurice mentioned in the premise
if jessica_text_speed_premise <= jessica_text_speed_hypothesis:
    # check if the estimate of 'jessica_text_speed_hypothesis' contradicts the speed of Jessica in the premise
    label = "contradiction"
elif maurice_text_speed_hypothesis != maurice_text_speed_premise:
    # check if the speed of Maurice in the hypothesis contradicts the speed of Maurice reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
