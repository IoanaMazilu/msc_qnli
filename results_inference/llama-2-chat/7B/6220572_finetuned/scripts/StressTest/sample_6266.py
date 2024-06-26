dan_work_hours_premise = 3
dan_work_hours_hypothesis = 4

# the hypothesis talks about the number of hours Dan works alone, referenced also in the premise
if dan_work_hours_hypothesis!= dan_work_hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
