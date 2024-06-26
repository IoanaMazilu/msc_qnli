don_code_premise = 58
don_code_hypothesis = 18
mass_code_premise = 29
mass_code_hypothesis = 29

# the hypothesis refers to the coding of DON and MASS mentioned in the premise
if don_code_hypothesis >= don_code_premise:
    # check if the estimate of 'don_code_hypothesis' contradicts the number of DON coding in the premise
    label = "contradiction"
elif mass_code_hypothesis!= mass_code_premise:
    # check if the number of MASS coding in the hypothesis contradicts the number of MASS coding reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
