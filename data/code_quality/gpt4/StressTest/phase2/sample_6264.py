dan_work_hours_premise = 3
dan_work_hours_hypothesis = 2

# the hypothesis refers to the number of hours Dan works alone, mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the hypothesis value contradicts the exact number of hours Dan worked in the premise
    label = "contradiction"
elif dan_work_hours_hypothesis < dan_work_hours_premise:
    # the premise gives an exact number of hours Dan worked
    # any number of hours less than 'dan_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
