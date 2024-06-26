premise = 18
hypothesis = 58

# the hypothesis refers to the percentage of students with cars at Morse
if hypothesis <= premise:
    # check if the estimate of 'hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage greater than 'premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
