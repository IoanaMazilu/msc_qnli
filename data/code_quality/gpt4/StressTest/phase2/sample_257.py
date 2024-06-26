jessica_text_speed_premise = 85
maurice_text_speed_premise = 25
jessica_text_speed_hypothesis = 85
maurice_text_speed_hypothesis = 25

# The hypothesis refers to the texting speed of Jessica and Maurice mentioned in the premise
if jessica_text_speed_hypothesis != jessica_text_speed_premise:
    # check if the stated 'jessica_text_speed_hypothesis' contradicts the texting speed of Jessica in the premise
    label = "contradiction"
elif maurice_text_speed_hypothesis != maurice_text_speed_premise:
    # check if the stated 'maurice_text_speed_hypothesis' contradicts the texting speed of Maurice in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
