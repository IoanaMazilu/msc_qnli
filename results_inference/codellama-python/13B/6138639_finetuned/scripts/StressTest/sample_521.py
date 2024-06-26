roses_vase_premise = 18
roses_vase_hypothesis = 18

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if roses_vase_hypothesis <= roses_vase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'roses_vase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)