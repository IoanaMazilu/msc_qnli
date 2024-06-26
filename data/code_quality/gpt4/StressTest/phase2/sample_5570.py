jessica_text_speed_premise = 75
maurice_text_speed_premise = 10
jessica_text_speed_hypothesis = 25
maurice_text_speed_hypothesis = 10

# the hypothesis refers to the text speed of Jessica and Maurice mentioned in the premise
if jessica_text_speed_hypothesis > jessica_text_speed_premise:
    # check if the speed of 'jessica_text_speed_hypothesis' contradicts the speed of Jessica in the premise
    label = "contradiction"
elif maurice_text_speed_hypothesis != maurice_text_speed_premise:
    # check if the speed of Maurice in the hypothesis contradicts the speed of Maurice in the premise
    label = "contradiction"
elif jessica_text_speed_hypothesis < jessica_text_speed_premise:
    # the hypothesis speed for Jessica is less than the premise speed, but it does not contradict the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
