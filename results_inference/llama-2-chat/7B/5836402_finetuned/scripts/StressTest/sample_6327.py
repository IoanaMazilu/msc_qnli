boxes_packed_per_minute_premise = 10
boxes_packed_per_minute_hypothesis = 20

# the hypothesis refers to the number of boxes of cigarettes packed per minute, which is also mentioned in the premise
if boxes_packed_per_minute_premise >= boxes_packed_per_minute_hypothesis:
    # check if the estimate of 'boxes_packed_per_minute_hypothesis' contradicts the number of boxes packed per minute in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
