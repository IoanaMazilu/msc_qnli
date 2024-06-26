required_ratio_premise = 4/4
required_ratio_hypothesis = 1/4

# the hypothesis talks about the required ratio of top-10-movies lists, referenced also in the premise
if required_ratio_hypothesis >= required_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than'required_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the required ratio
    # any ratio less than'required_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
