share_premise = 600
share_hypothesis = 400

# the hypothesis talks about the share value and Greg's share mentioned in the premise
if share_hypothesis!= share_premise:
    # check if the hypothesis value contradicts the share value reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the share value
    # any share value consistent with'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
