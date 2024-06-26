king_code_premise = 17
don_code_premise = 18
king_code_hypothesis = 27
don_code_hypothesis = 18

# the hypothesis talks about the code representation of words KING and DON
if king_code_premise >= king_code_hypothesis:
    # check if the given 'king_code_hypothesis' contradicts the 'king_code_premise'
    label = "contradiction"
elif don_code_premise != don_code_hypothesis:
    # check if the 'don_code_hypothesis' contradicts the 'don_code_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
