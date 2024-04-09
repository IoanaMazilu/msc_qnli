total_share_premise = 3800
total_share_hypothesis = 4800

# the hypothesis refers to the total share among John, Jose & Binoy mentioned in the premise
if total_share_hypothesis <= total_share_premise:
    # check if the total share in the hypothesis contradicts the estimate of more than 'total_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total share
    # any total share greater than 'total_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
