don_code_premise = 58
don_code_hypothesis = 18
mass_code_premise = 29
mass_code_hypothesis = 29

# the hypothesis refers to the codes of DON and MASS mentioned in the premise
if don_code_hypothesis >= don_code_premise:
    # check if the code of DON in the hypothesis contradicts the premise
    label = "contradiction"
elif mass_code_hypothesis!= mass_code_premise:
    # check if the code of MASS in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
