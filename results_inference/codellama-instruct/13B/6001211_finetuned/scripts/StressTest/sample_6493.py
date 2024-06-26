percentage_given_back_premise = 7
percentage_given_back_hypothesis = 3

# the hypothesis talks about the percentage given back each month by Dana, referenced also in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_given_back_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage given back each month
    # any percentage less than 'percentage_given_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
