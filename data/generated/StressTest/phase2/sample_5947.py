# Premise: If DON is coded as less than 58 and MASS is coded as 29 Then KING is coded as.
# Hypothesis: If DON is coded as 18 and MASS is coded as 29 Then KING is coded as.
# Golden Label: neutral

DON_code_premise = 58
DON_code_hypothesis = 18
MASS_code_premise = 29
MASS_code_hypothesis = 29

# the hypothesis refers to how DON and MASS are coded which is also mentioned in the premise
if DON_code_hypothesis >= DON_code_premise:
    # check if the value of 'DON_code_hypothesis' contradicts the condition of less than 'DON_code_premise'
    label = "contradiction"
elif MASS_code_hypothesis != MASS_code_premise:
    # check if the value of 'MASS_code_hypothesis' contradicts 'MASS_code_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

