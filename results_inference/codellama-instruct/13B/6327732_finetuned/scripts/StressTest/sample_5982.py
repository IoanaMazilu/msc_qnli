premise_percentage = 25
hypothesis_percentage = 35

# the hypothesis refers to the percentage of students with cars at Morse
if hypothesis_percentage < premise_percentage:
    # check if the hypothesis value contradicts the premise percentage
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars at Morse
    # any percentage greater than or equal to 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
