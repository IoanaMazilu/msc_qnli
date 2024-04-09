john_ratio_premise = 4800
john_ratio_hypothesis = 3800
jose_ratio_premise = 4800
jose_ratio_hypothesis = 3800
binoy_ratio_premise = 4800
binoy_ratio_hypothesis = 3800

# the hypothesis talks about the ratio of John, Jose, and Binoy
if john_ratio_hypothesis <= john_ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio of John in the premise
    label = "contradiction"
elif jose_ratio_hypothesis <= jose_ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio of Jose in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of John, Jose, and Binoy
    # any ratio greater than the estimate of the ratio of John, Jose, and Binoy in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
