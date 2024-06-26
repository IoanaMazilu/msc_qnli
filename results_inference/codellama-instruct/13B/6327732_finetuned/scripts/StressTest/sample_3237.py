premise_percentage = 20
hypothesis_percentage = 50

# the hypothesis refers to the percentage of students with cars at Morse
if hypothesis_percentage >= premise_percentage:
    # check if the hypothesis value contradicts the premise percentage
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars at Morse
    # any percentage of students with cars less than 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
