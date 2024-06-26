dan_work_hours_premise = 6
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, which is also mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the hypothesis value contradicts the premise value of 'dan_work_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
