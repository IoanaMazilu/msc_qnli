king_coded_premise = 17
don_coded_premise = 18
mass_coded_hypothesis = 27

# the hypothesis refers to the coded values of KING and DON, which are also mentioned in the premise
if king_coded_premise >= mass_coded_hypothesis:
    # check if the estimate of'mass_coded_hypothesis' contradicts the coded value of KING in the premise
    label = "contradiction"
elif don_coded_premise!= don_coded_hypothesis:
    # check if the coded value of DON in the hypothesis contradicts the coded value of DON reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
