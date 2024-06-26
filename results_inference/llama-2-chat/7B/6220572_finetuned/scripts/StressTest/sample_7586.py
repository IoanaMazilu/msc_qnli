king_code_premise = 17
king_code_hypothesis = 37
don_code_premise = 18
don_code_hypothesis = 18

# the hypothesis refers to the coding of KING and DON, also mentioned in the premise
if king_code_hypothesis == king_code_premise and don_code_hypothesis == don_code_premise:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
else:
    # if the hypothesis values and estimates contradict the premise ones, we can infer contradiction
    label = "contradiction"

print(label)
