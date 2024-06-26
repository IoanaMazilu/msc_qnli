king_code_premise = 17
don_code_premise = 18
king_code_hypothesis = 37
don_code_hypothesis = 18

# the hypothesis refers to the codes of KING and DON mentioned in the premise
if king_code_premise!= king_code_hypothesis:
    # check if the code of KING in the hypothesis contradicts the code of KING in the premise
    label = "contradiction"
elif don_code_premise!= don_code_hypothesis:
    # check if the code of DON in the hypothesis contradicts the code of DON in the premise
    label = "contradiction"
else:
    # if the codes of KING and DON in the hypothesis do not contradict the codes in the premise, we can infer entailment
    label = "entailment"

print(label)
