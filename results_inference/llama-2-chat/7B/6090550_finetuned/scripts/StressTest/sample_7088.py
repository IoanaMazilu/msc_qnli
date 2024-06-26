work_hours_dan_premise = 6
work_hours_dan_hypothesis = 6

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if work_hours_dan_hypothesis >= work_hours_dan_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise, so the relation is neutral
    label = "neutral"

print(label)
