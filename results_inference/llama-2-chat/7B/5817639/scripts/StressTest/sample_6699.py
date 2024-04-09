share_premise = 4500
share_hypothesis = 6500

# the hypothesis talks about a lower share value than the premise
if share_hypothesis <= share_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share value
    # any share value greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
