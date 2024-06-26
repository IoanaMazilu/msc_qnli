john_share_premise = 4800 / 3
jose_share_premise = 4800 / 4
binoy_share_premise = 4800 / 6

hypothesis_john = 3800 + john_share_premise
hypothesis_jose = 3800 + jose_share_premise
hypothesis_binoy = 3800 + binoy_share_premise

# check if the hypothesis values contradict the premise values
if hypothesis_john < john_share_premise or hypothesis_jose < jose_share_premise or hypothesis_binoy < binoy_share_premise:
    label = "contradiction"
elif hypothesis_john > john_share_premise or hypothesis_jose > jose_share_premise or hypothesis_binoy > binoy_share_premise:
    label = "entailment"
else:
    # the premise gives a ratio of 2:4:6, so any value greater than or equal to the ratio is consistent with the premise
    label = "neutral"

print(label)
