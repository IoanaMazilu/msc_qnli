work_days_premise = 75
work_days_hypothesis = 75

# the hypothesis refers to the number of days Sreedhar can do the work, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be inferred as entailment
    label = "entailment"

print(label)
