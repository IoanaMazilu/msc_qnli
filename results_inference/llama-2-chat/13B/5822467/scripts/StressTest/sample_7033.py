fred_sam_premise = 800
fred_sam_hypothesis = 100

# the hypothesis talks about the distance between Fred and Sam, referenced also in the premise
if fred_sam_hypothesis <= fred_sam_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fred_sam_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Fred and Sam
    # any distance less than or equal to 100 miles is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
