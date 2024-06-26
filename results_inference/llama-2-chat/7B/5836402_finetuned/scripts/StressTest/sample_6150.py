james_work_hours_premise = 41
james_work_hours_hypothesis = 71

# the hypothesis refers to the number of hours worked by James, also mentioned in the premise
if james_work_hours_hypothesis >= james_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'james_work_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'james_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)