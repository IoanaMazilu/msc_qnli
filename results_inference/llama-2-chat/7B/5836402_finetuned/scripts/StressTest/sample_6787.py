james_work_hours_premise = 21
james_work_hours_hypothesis = 41

# the hypothesis refers to the number of hours James worked, also mentioned in the premise
if james_work_hours_hypothesis <= james_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'james_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'james_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
