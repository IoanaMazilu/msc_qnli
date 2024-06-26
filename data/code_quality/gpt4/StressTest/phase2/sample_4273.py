hourly_rate_premise = 7.00
hourly_rate_hypothesis = 7.00
work_hours_premise = 70
work_hours_hypothesis = 50

# the hypothesis refers to David's wage per hour and the number of hours he works per week, both mentioned in the premise
if hourly_rate_premise != hourly_rate_hypothesis:
    # check if the hypothesis contradicts the hourly rate in the premise
    label = "contradiction"
elif work_hours_hypothesis >= work_hours_premise:
    # check if the number of work hours stated in the hypothesis contradicts the estimate of less than 'work_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
