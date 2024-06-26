#don_code_premise = 58
#don_code_hypothesis = 18
#mass_code_premise = 29
#mass_code_hypothesis = 29

# the hypothesis refers to the codes of DON and MASS mentioned in the premise
# if the codes of DON and MASS in the hypothesis contradict the codes in the premise, we have a contradiction
if don_code_hypothesis >= don_code_premise:
    label = "contradiction"
elif mass_code_hypothesis!= mass_code_premise:
    label = "contradiction"
else:
    # if the codes in the hypothesis do not contradict the codes in the premise, we cannot infer the code of KING from the premise
    label = "neutral"

print(label)
#