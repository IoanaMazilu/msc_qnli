weeks_premise = 3
weeks_hypothesis = 6

# the hypothesis refers to the number of weeks mentioned in the premise
if weeks_hypothesis <= weeks_premise:
    # check if the estimate of 'weeks_hypothesis' contradicts the number of weeks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks greater than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
