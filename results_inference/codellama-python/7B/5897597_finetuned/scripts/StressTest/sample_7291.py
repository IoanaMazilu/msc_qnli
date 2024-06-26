share_premise = 500
share_hypothesis = 600

# the hypothesis refers to Greg's share mentioned in the premise
if share_hypothesis <= share_premise:
    # check if the value of'share_hypothesis' contradicts the estimate of more than'share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Greg's share
    # any share greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
