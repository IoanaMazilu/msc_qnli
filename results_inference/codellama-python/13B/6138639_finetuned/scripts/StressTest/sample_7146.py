difference_premise = 4
difference_hypothesis = 8

# the hypothesis refers to the difference between the number Cindy is thinking of and the square of a positive integer
if difference_hypothesis <= difference_premise:
    # check if the hypothesis value contradicts the estimate of 'difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference
    # any difference greater than 'difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
