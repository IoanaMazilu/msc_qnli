sreedhar_work_days_premise = 75
sreedhar_work_days_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work alone, mentioned in the premise
if sreedhar_work_days_hypothesis >= sreedhar_work_days_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
