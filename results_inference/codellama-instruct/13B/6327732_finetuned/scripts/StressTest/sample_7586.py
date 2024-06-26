king_coded_premise = 17
king_coded_hypothesis = 37
don_coded_premise = 18
don_coded_hypothesis = 18
mass_coded_premise = None
mass_coded_hypothesis = None

# the hypothesis refers to the coded values of KING and DON, which are also mentioned in the premise
if king_coded_premise!= king_coded_hypothesis or don_coded_premise!= don_coded_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif mass_coded_premise is not None and mass_coded_hypothesis is not None:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the coded values of KING and DON
    # any coded value for MASS is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
