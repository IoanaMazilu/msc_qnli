percentage_premise = 7
percentage_hypothesis = 3

# the hypothesis talks about the percentage of the amount Dana gives back to her parents, referenced also in the premise
if percentage_hypothesis >= percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of the amount Dana gives back
    # any percentage less than 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
