number_premise = 0
number_hypothesis = 8

# the hypothesis talks about the number Cindy is thinking of, referenced in the premise
if number_hypothesis <= number_premise:
    # check if the hypothesis value contradicts the estimate of 'number_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number Cindy is thinking of, but the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
