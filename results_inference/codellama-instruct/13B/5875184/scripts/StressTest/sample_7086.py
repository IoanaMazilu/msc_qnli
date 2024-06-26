premise_hours = 6
hypothesis_hours = 8

# the hypothesis refers to the number of hours Dan works alone
if premise_hours < hypothesis_hours:
    # check if the hypothesis value contradicts the number of hours Dan works alone in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours Dan works alone
    # any number of hours greater than 'premise_hours' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
