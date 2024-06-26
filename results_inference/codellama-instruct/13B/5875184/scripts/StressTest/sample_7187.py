catherina_work_hours_premise = [5, 5, 5, 10, 10]
catherina_work_hours_hypothesis = [6, 6, 6, 10, 10]

# the hypothesis refers to the number of work hours per day for each day of the week
if catherina_work_hours_hypothesis <= catherina_work_hours_premise:
    # check if the estimate of 'catherina_work_hours_hypothesis' contradicts the number of work hours per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work hours per day
    # any number of work hours greater than 'catherina_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
