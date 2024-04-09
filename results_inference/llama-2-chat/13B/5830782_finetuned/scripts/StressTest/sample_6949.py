ratio_premise = 1/4
ratio_hypothesis = 5/4

# the hypothesis talks about the ratio of ages between Arun and Deepak, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
