worked_hours_premise = 41
worked_hours_hypothesis = 11

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if worked_hours_hypothesis <= worked_hours_premise:
    # check if the hypothesis value contradicts the estimate of 'worked_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours worked by James greater than 'worked_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
