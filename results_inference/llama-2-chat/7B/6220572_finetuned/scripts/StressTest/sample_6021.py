borrowed_pounds_premise = 5000
borrowed_pounds_hypothesis = 2000

# the hypothesis refers to the amount of money borrowed for college education mentioned in the premise
if borrowed_pounds_hypothesis <= borrowed_pounds_premise:
    # check if the estimate of 'borrowed_pounds_hypothesis' contradicts the amount of money borrowed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money borrowed
    # any amount of money borrowed greater than 'borrowed_pounds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
