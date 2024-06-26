fred_sam_premise = 45
fred_sam_hypothesis = 35

# the hypothesis refers to the distance between Fred and Sam, mentioned in the premise
if fred_sam_premise <= fred_sam_hypothesis:
    # check if the estimate of 'fred_sam_hypothesis' contradicts the distance between Fred and Sam in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Fred and Sam
    # any distance less than or equal to 35 miles is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
