king_premise = 17
king_hypothesis = 37
don_premise = 18
don_hypothesis = 18
mass_premise = None
mass_hypothesis = None

# the hypothesis talks about the coding of MASS, referenced also in the premise
if king_hypothesis > king_premise:
    # check if the hypothesis value contradicts the estimate of 'king' in the premise
    label = "contradiction"
elif don_hypothesis!= don_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
