sameer_anand_ratio_premise = 1/4
sameer_anand_ratio_hypothesis = 5/4

# the hypothesis talks about the ratio of ages of Sameer and Anand, referenced also in the premise
if sameer_anand_ratio_hypothesis <= sameer_anand_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than'sameer_anand_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than'sameer_anand_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)