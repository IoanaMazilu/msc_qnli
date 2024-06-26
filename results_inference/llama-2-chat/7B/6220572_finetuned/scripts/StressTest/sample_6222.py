share_difference_premise = 200
share_difference_hypothesis = 400

# the hypothesis talks about the difference in shares between Mani and Rani, referenced also in the premise
if share_difference_hypothesis <= share_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_difference_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in shares
    # any difference in shares greater than'share_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
