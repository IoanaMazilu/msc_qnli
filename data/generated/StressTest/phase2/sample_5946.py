# Premise: If DON is coded as 18 and MASS is coded as 29 Then KING is coded as.
# Hypothesis: If DON is coded as less than 58 and MASS is coded as 29 Then KING is coded as.
# Golden Label: entailment

don_code_premise = 18
don_code_hypothesis = 58
mass_code_premise = 29
mass_code_hypothesis = 29

# the hypothesis talks about the coded values of DON and MASS, mentioned also in the premise
if don_code_premise >= don_code_hypothesis:
    # check if the premise value contradicts the estimate of less than 'don_code_hypothesis'
    label = "contradiction"
elif mass_code_hypothesis != mass_code_premise:
    # check if the coded value of MASS in the hypothesis contradicts the coded value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

