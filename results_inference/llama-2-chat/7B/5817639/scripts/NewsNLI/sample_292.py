legal_premise = True
moral_hypothesis = False

# the hypothesis mentions the morality of a sentence, which is also referenced in the premise
if moral_hypothesis!= legal_premise:
    # check if the morality in the hypothesis contradicts the legality in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
