share_tony_premise = 4500
share_tony_hypothesis = 6500

# the hypothesis refers to the number of shares of Tony mentioned in the premise
if share_tony_hypothesis <= share_tony_premise:
    # check if the hypothesis value contradicts the number of shares in the premise
    label = "contradiction"
else:
    # any number of shares less than'share_tony_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
