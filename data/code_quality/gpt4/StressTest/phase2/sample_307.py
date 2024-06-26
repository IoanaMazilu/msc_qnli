ratio_premise = 2/3
ratio_hypothesis = 4/3

# the hypothesis talks about the ratio between Sandy's and Molly's ages which is also discussed in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between Sandy's and Molly's ages
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
