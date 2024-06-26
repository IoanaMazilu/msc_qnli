dig_days_premise = 24
dig_days_hypothesis = 84

# the hypothesis refers to the number of days Paul can dig a well, mentioned in the premise
if dig_days_premise >= dig_days_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'dig_days_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
