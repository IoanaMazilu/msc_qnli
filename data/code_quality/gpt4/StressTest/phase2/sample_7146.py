less_than_square_premise = 4
less_than_square_hypothesis = 8

# the hypothesis refers to the number Cindy is thinking of, mentioned also in the premise
if less_than_square_premise >= less_than_square_hypothesis:
    # check if 'less_than_square_hypothesis' contradicts the number which is less than the square in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the less than the square number
    # any number which is less than a larger number than 'less_than_square_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
