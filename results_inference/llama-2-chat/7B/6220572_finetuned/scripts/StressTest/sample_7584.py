king_coded_premise = 17
king_coded_hypothesis = 27
don_coded_premise = 18
don_coded_hypothesis = 18

# the hypothesis refers to the coding of KING and DON mentioned in the premise
if king_coded_hypothesis >= king_coded_premise:
    # check if the estimate of 'king_coded_hypothesis' contradicts the coding of KING in the premise
    label = "contradiction"
elif don_coded_hypothesis!= don_coded_premise:
    # check if the coding of DON in the hypothesis contradicts the coding of DON reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
