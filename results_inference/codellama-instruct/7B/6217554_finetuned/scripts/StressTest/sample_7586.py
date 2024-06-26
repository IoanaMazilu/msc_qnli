# define variables for the numerical entities in both premise and hypothesis
king_code_premise = 17
king_code_hypothesis = 37
don_code_premise = 18
don_code_hypothesis = 18
mass_code_premise = 18
mass_code_hypothesis = 18

# check if the codes for KING and DON in the hypothesis contradict the codes reported in the premise
if king_code_hypothesis!= king_code_premise or don_code_hypothesis!= don_code_premise:
    label = "contradiction"
# check if the code for MASS in the hypothesis contradicts the code for MASS reported in the premise
elif mass_code_hypothesis!= mass_code_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
