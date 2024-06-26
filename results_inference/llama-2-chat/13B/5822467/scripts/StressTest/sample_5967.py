dawson_time_premise = 38
dawson_time_hypothesis = 28

# the hypothesis refers to the time taken by Dawson to run the first leg of the course
if dawson_time_hypothesis > dawson_time_premise:
    # the hypothesis value is greater than the premise value, so there is no contradiction
    label = "entailment"
elif dawson_time_hypothesis <= dawson_time_premise:
    # the hypothesis value is less than or equal to the premise value, so there is no entailment
    label = "neutral"
else:
    # there is no explicit contradiction, but the hypothesis value is not explicitly entailed from the premise
    label = "neutral"

print(label)
