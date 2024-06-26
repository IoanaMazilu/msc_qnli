roses_vase_premise = 10
roses_vase_hypothesis = 70

# the hypothesis talks about the number of roses in a vase, referenced also in the premise
if roses_vase_hypothesis <= roses_vase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'roses_vase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
