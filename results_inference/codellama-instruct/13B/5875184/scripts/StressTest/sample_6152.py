premise_hours = 41
hypothesis_hours = 11

# the hypothesis refers to the number of hours worked by James and Harry
if premise_hours!= hypothesis_hours:
    # check if the hypothesis value contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours worked by Harry greater than 'hypothesis_hours' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
