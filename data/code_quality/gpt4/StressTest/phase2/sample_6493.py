percentage_back_premise = 7
percentage_back_hypothesis = 3

# the hypothesis talks about the percentage Dana gives back each month, also referenced in the premise
if percentage_back_hypothesis >= percentage_back_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_back_premise'
    label = "contradiction"
else:
    # the premise specifies that Dana gives back less than 'percentage_back_premise' each month
    # any percentage less than 'percentage_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)