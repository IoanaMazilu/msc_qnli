percentage_given_back_premise = 2
percentage_given_back_hypothesis = 3

# the hypothesis talks about the percentage that Dana gives back to her parents each month, referenced also in the premise
if percentage_given_back_hypothesis <= percentage_given_back_premise:
    # check if the hypothesis value contradicts the percentage given back in the premise
    label = "contradiction"
else:
    # the premise and hypothesis both talk about a percentage that Dana gives back each month
    # any percentage less than 'percentage_given_back_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
