dan_work_hours_premise = 8
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the number of hours in the hypothesis contradicts the premise of less than 'dan_work_hours_premise'
    label = "contradiction"
elif dan_work_hours_hypothesis < dan_work_hours_premise:
    # if the number of hours in the hypothesis is less than the number of hours in the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
