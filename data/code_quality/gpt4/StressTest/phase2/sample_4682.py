first_segment_premise = 360
first_segment_hypothesis = 160
speed_first_segment = 60
second_segment_premise = 120
second_segment_hypothesis = 120
speed_second_segment = 40

# the hypothesis talks about the distance driven at certain speeds, mentioned in the premise
if first_segment_hypothesis > first_segment_premise:
    # check if the distance of the first segment in the hypothesis contradicts the distance of the first segment in the premise
    label = "contradiction"
elif second_segment_hypothesis != second_segment_premise:
    # check if the distance of the second segment in the hypothesis contradicts the distance of the second segment in the premise
    label = "contradiction"
elif first_segment_hypothesis < first_segment_premise:
    # the hypothesis suggests a smaller distance for the first segment compared to the premise, which is consistent but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
