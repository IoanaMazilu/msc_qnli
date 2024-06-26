plate_number_premise = 7
plate_number_hypothesis = 5

# the hypothesis refers to the number of the Ferrari's plate mentioned in the premise
if plate_number_hypothesis >= plate_number_premise:
    # check if the number of 'plate_number_hypothesis' contradicts the number of digits in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of digits in the plate
    # any number of digits less than 'plate_number_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
