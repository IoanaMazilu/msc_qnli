roses_vase_premise = 1500
roses_vase_hypothesis = 6500

# the hypothesis talks about the value of the bonds purchased by Robert, referenced also in the premise
if roses_vase_hypothesis <= roses_vase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'roses_vase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of the bonds
    # any value greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
