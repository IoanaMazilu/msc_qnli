# Premise: If KING is coded as less than 27 and DON is coded as 18 Then MASS is coded as.
# Hypothesis: If KING is coded as 17 and DON is coded as 18 Then MASS is coded as.
# Golden Label: neutral

king_code_premise = 27
don_code_premise = 18
king_code_hypothesis = 17
don_code_hypothesis = 18

# the hypothesis refers to the code of KING and DON mentioned in the premise
if king_code_hypothesis >= king_code_premise:
    # check if the 'king_code_hypothesis' contradicts the code of KING in the premise
    label = "contradiction"
elif don_code_hypothesis != don_code_premise:
    # check if the code of DON in the hypothesis contradicts the code of DON in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

