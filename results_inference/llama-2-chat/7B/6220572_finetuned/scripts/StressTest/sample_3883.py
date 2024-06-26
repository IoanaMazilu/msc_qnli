jogging_hours_premise = 4
jogging_hours_hypothesis = 3

# the hypothesis refers to the number of jogging hours mentioned in the premise
if jogging_hours_hypothesis >= jogging_hours_premise:
    # check if the hypothesis estimate contradicts the number of jogging hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of jogging hours
    # any number of jogging hours less than 'jogging_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
