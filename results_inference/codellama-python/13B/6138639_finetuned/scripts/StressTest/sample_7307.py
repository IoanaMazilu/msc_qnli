work_hours_monday_premise = 9
work_hours_monday_hypothesis = 5
work_hours_tuesday_premise = 5
work_hours_tuesday_hypothesis = 5
work_hours_wednesday_premise = 9
work_hours_wednesday_hypothesis = 5
work_hours_thursday_premise = 5
work_hours_thursday_hypothesis = 5
work_hours_friday_premise = 9
work_hours_friday_hypothesis = 5

# the hypothesis refers to the number of work hours Mary works per day on different days mentioned in the premise
if work_hours_monday_premise!= work_hours_monday_hypothesis:
    # check if the number of work hours Mary works on Monday in the premise contradicts the number of work hours Mary works on Monday in the hypothesis
    label = "contradiction"
elif work_hours_tuesday_premise!= work_hours_tuesday_hypothesis:
    # check if the number of work hours Mary works on Tuesday in the premise contradicts the number of work hours Mary works on Tuesday in the hypothesis
    label = "contradiction"
elif work_hours_wednesday_premise!= work_hours_wednesday_hypothesis:
    # check if the number of work hours Mary works on Wednesday in the premise contradicts the number of work hours Mary works on Wednesday in the hypothesis
    label = "contradiction"
elif work_hours_thursday_premise!= work_hours_thursday_hypothesis:
    # check if the number of work hours Mary works on Thursday in the premise contradicts the number of work hours Mary works on Thursday in the hypothesis
    label = "contradiction"
elif work_hours_friday_premise!= work_hours_friday_hypothesis:
    # check if the number of work hours Mary works on Friday in the premise contradicts the number of work hours Mary works on Friday in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
