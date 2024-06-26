premise_hours = 8
hypothesis_hours = 6

# the hypothesis refers to the number of hours worked by Dan and Annie
if hypothesis_hours <= premise_hours:
    # check if the estimate of 'hypothesis_hours' contradicts the number of hours worked by Dan in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by Dan
    # any number of hours greater than 'premise_hours' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
