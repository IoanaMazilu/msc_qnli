percentage_given_back_premise = 6
percentage_given_back_hypothesis = 4

# the hypothesis talks about the percentage of the amount Dana gives back to her parents each month
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_given_back_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the amount Dana gives back
    # any percentage less than 'percentage_given_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
