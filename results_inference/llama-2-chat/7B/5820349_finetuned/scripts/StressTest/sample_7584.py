king_code_premise = 17
don_code_premise = 18
mass_code_premise = 27

king_code_hypothesis = 27
don_code_hypothesis = 18

# the hypothesis refers to the codes of KING and DON mentioned in the premise
if king_code_premise >= king_code_hypothesis:
    # check if the estimate of 'king_code_hypothesis' contradicts the code of KING in the premise
    label = "contradiction"
elif don_code_hypothesis!= don_code_premise:
    # check if the code of DON in the hypothesis contradicts the code of DON reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
