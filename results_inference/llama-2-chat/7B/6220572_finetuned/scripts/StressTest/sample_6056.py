jogging_hours_premise = 3
jogging_hours_hypothesis = 4

# the hypothesis refers to the number of hours spent jogging mentioned in the premise
if jogging_hours_hypothesis!= jogging_hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'jogging_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
