work_days_sreedhar_premise = 75
work_days_sreedhar_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work alone, mentioned in the premise
if work_days_sreedhar_hypothesis >= work_days_sreedhar_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
