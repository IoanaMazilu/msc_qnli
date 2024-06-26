king_coded_premise = 17
king_coded_hypothesis = 37
don_coded_premise = 18
don_coded_hypothesis = 18
mass_coded_premise = None
mass_coded_hypothesis = None

# the hypothesis refers to the coded values of KING and DON, which are also mentioned in the premise
if king_coded_premise!= king_coded_hypothesis or don_coded_premise!= don_coded_hypothesis:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif mass_coded_premise is not None and mass_coded_hypothesis is not None:
    # check if the hypothesis values entail the premise ones
    if mass_coded_premise == mass_coded_hypothesis:
        label = "entailment"
    else:
        label = "neutral"
else:
    # the premise gives only an estimate for the coded values of KING and DON
    # any coded value for MASS that is consistent with the premise is not explicitly entailed from the premise
    label = "neutral"

print(label)
