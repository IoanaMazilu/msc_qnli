# Premise: If KING is coded as 17 and MASS is coded as 29 Then DOC is coded as.
# Hypothesis: If KING is coded as less than 17 and MASS is coded as 29 Then DOC is coded as.
# Golden Label: contradiction

king_code_premise = 17
mass_code_premise = 29
king_code_hypothesis = 17
mass_code_hypothesis = 29

# the hypothesis refers to the codes of KING and MASS mentioned in the premise
if king_code_hypothesis >= king_code_premise:
    # check if the estimate of 'king_code_hypothesis' contradicts the code of KING in the premise
    label = "contradiction"
elif mass_code_hypothesis != mass_code_premise:
    # check if the code of MASS in the hypothesis contradicts the code of MASS reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

