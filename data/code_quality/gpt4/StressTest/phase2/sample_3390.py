king_code_premise = 17
king_code_hypothesis = 77
mass_code_premise = 29
mass_code_hypothesis = 29

# the hypothesis talks about the codes of KING and MASS, referenced also in the premise
if king_code_premise >= king_code_hypothesis:
    # check if the code of KING in the premise contradicts the estimate of less than 'king_code_hypothesis' in hypothesis
    label = "contradiction"
elif mass_code_premise != mass_code_hypothesis:
    # check if the code of MASS in the premise contradicts the code of MASS in hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
