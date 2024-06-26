dig_days_premise = 24
dig_days_hypothesis = 74

# the hypothesis mentions the number of days in which Paul can dig a well, which is also mentioned in the premise
if dig_days_hypothesis <= dig_days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif dig_days_hypothesis > dig_days_premise:
    # check if the hypothesis value is more than the premise
    # the premise gives a definite number of days
    # any number of days less than 'dig_days_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
