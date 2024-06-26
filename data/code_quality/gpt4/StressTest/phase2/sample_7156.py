ratio_premise = 7 / 3
ratio_hypothesis = 4 / 3

# the hypothesis talks about the ratio of ages between Sandy and Molly, also referenced in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
