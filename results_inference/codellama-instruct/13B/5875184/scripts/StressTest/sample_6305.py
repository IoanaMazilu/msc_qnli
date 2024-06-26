premise_hours = 41
hypothesis_hours = 61

# the hypothesis refers to the total number of hours worked by James
if hypothesis_hours <= premise_hours:
    # check if the estimate of 'hypothesis_hours' contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours greater than 'premise_hours' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
