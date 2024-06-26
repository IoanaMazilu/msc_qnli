leave_city_premise = 30
leave_city_hypothesis = 60

# the hypothesis talks about the time Kerri leaves City A after Jim, which is also referenced in the premise
if leave_city_hypothesis <= leave_city_premise:
    # check if the hypothesis value contradicts the estimate of more than 'leave_city_premise' minutes
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Kerri leaves after Jim
    # any time greater than 'leave_city_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
