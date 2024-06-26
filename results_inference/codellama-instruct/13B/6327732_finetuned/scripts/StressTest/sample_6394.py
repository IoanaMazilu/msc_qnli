cylinders_premise = 7
cylinders_hypothesis = 8

# the hypothesis refers to the number of cylinders used in the car, mentioned in the premise
if cylinders_hypothesis <= cylinders_premise:
    # check if the estimate of 'cylinders_hypothesis' contradicts the number of cylinders in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cylinders
    # any number of cylinders greater than 'cylinders_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
