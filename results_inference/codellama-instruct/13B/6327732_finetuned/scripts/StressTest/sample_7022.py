premise_percentage = 20
hypothesis_percentage = 50

# the hypothesis refers to the percentage of students with cars at Morse, which is also mentioned in the premise
if hypothesis_percentage <= premise_percentage:
    # check if the estimate of 'hypothesis_percentage' contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage greater than 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
