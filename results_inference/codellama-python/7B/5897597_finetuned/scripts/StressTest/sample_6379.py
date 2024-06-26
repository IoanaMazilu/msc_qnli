first_hours_premise = 10
first_hours_hypothesis = 30

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, as mentioned in the premise
if first_hours_hypothesis <= first_hours_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of more than 'first_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'first_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
