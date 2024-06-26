leave_time_premise = 120
leave_time_hypothesis = 520

# the hypothesis refers to the time Dan leaves City A after Cara, which is also mentioned in the premise
if leave_time_hypothesis < leave_time_premise:
    # check if the estimate of 'leave_time_hypothesis' contradicts the leave time reported in the premise
    label = "contradiction"
elif leave_time_hypothesis == leave_time_premise:
    # check if the leave time in the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, but it cannot be fully entailed from it, we have neutrality
    label = "neutral"

print(label)
