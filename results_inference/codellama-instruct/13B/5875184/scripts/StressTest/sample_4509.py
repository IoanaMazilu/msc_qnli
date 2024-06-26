premise_hours = 41
hypothesis_hours = 11

# the hypothesis refers to the number of hours worked by James
if premise_hours <= hypothesis_hours:
    # check if the estimate of 'hypothesis_hours' contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours greater than 'hypothesis_hours' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
