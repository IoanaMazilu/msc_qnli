number_premise = 5
number_hypothesis = 7

# the hypothesis refers to a number formed by the product of X, Y and Z, which is also mentioned in the premise
if number_hypothesis <= number_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'number_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number
    # any number greater than 'number_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
