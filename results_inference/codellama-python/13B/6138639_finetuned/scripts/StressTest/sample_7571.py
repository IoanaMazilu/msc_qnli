fred_sam_distance_premise = 35
fred_sam_distance_hypothesis = 35

# the hypothesis talks about the distance between Fred and Sam, referenced also in the premise
if fred_sam_distance_hypothesis <= fred_sam_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'fred_sam_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Fred and Sam
    # any distance greater than 'fred_sam_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
