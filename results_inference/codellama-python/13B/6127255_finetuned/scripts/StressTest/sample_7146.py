number_premise = 4
number_hypothesis = 8

# the hypothesis refers to the number Cindy is thinking of, which is also mentioned in the premise
if number_hypothesis <= number_premise:
    # check if the hypothesis value contradicts the estimate of 'number_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number
    # any number less than 'number_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)