# Premise: Jessica can text 85 words per minute, while Maurice can text 25 words per minute.
# Hypothesis: Jessica can text more than 75 words per minute, while Maurice can text 25 words per minute.
# Golden Label: entailment

jessica_text_speed_premise = 85
jessica_text_speed_hypothesis = 75
maurice_text_speed_premise = 25
maurice_text_speed_hypothesis = 25

# the hypothesis refers to Jessica's and Maurice's texting speed mentioned in the premise
if jessica_text_speed_premise <= jessica_text_speed_hypothesis:
    # check if the estimate of 'jessica_text_speed_hypothesis' contradicts Jessica's texting speed in the premise
    label = "contradiction"
elif maurice_text_speed_hypothesis != maurice_text_speed_premise:
    # check if the Maurice's texting speed in the hypothesis contradicts Maurice's texting speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

