# Premise: If KING is coded as less than 77 and MASS is coded as 29 Then DOC is coded as.
# Hypothesis: If KING is coded as 17 and MASS is coded as 29 Then DOC is coded as.
# Golden Label: neutral

king_code_premise = 77
king_code_hypothesis = 17
mass_code_premise = 29
mass_code_hypothesis = 29

# the hypothesis refers to the codes for KING and MASS mentioned in the premise
if king_code_hypothesis >= king_code_premise:
    # check if the 'king_code_hypothesis' contradicts the premise that KING is coded as less than 'king_code_premise'
    label = "contradiction"
elif mass_code_hypothesis != mass_code_premise:
    # check if the 'mass_code_hypothesis' contradicts the code for MASS reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

