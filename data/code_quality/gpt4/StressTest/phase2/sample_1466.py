king_code_premise = 17
king_code_hypothesis = 77
mass_code_premise = 29
mass_code_hypothesis = 29

# the hypothesis refers to the coded values for 'KING' and 'MASS' mentioned in the premise
if king_code_premise != king_code_hypothesis:
    # check if the coded value of 'KING' in the hypothesis contradicts the coded value of 'KING' in the premise
    label = "contradiction"
elif mass_code_hypothesis != mass_code_premise:
    # check if the coded value of 'MASS' in the hypothesis contradicts the coded value of 'MASS' in the premise
    label = "contradiction"
else:
    # if the coded values of 'KING' and 'MASS' in the hypothesis do not contradict the premise ones, we can infer neutrality, since the 
    # coded value of 'DOG' is not explicitly mentioned in the premise.
    label = "neutral"

print(label)
