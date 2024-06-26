total_share_premise = 1000
total_share_hypothesis = 3000

# the hypothesis refers to the total share mentioned in the premise
if total_share_hypothesis <= total_share_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total share
    # any total share greater than 'total_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
