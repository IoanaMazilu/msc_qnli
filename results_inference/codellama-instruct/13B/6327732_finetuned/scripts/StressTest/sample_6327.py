boxes_per_minute_premise = 10
boxes_per_minute_hypothesis = 20

# the hypothesis refers to the number of boxes packed per minute, mentioned in the premise
if boxes_per_minute_hypothesis >= boxes_per_minute_premise:
    # check if the estimate of 'boxes_per_minute_hypothesis' contradicts the number of boxes packed in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of boxes packed per minute
    # any number of boxes packed per minute less than 'boxes_per_minute_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
