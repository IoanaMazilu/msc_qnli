# Premise: Jessica can text 85 words per minute, while Maurice can text 55 words per minute.
# Hypothesis: Jessica can text more than 25 words per minute, while Maurice can text 55 words per minute.
# Golden Label: entailment

jessica_speed_premise = 85
maurice_speed_premise = 55
jessica_speed_hypothesis = 25
maurice_speed_hypothesis = 55

# the hypothesis refers to the texting speed of Jessica and Maurice mentioned in the premise
if jessica_speed_premise <= jessica_speed_hypothesis:
    # check if the estimate of 'jessica_speed_hypothesis' contradicts the speed of Jessica in the premise
    label = "contradiction"
elif maurice_speed_hypothesis != maurice_speed_premise:
    # check if the speed of Maurice in the hypothesis contradicts the speed of Maurice reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

