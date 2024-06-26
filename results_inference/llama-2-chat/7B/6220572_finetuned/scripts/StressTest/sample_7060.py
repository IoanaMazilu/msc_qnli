leaving_time_premise = 20
leaving_time_hypothesis = 90

# the hypothesis refers to the time Dan leaves City A after Cara, also mentioned in the premise
if leaving_time_hypothesis <= leaving_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'leaving_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Dan leaves City A
    # any time greater than 'leaving_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
