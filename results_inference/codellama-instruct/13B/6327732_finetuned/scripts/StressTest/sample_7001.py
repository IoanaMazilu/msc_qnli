ramesh_days = 20
sushil_days = 25

# the hypothesis refers to the number of days it takes for Ramesh to finish a work
if ramesh_days <= 20:
    # check if the estimate of 'ramesh_days' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days it takes for Ramesh to finish a work
    # any number of days greater than 'ramesh_days' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
