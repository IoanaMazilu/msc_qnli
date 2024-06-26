premise_scores = [40, 60, 70, 80, 80]
hypothesis_scores = [50, 60, 70, 80, 80]

# the hypothesis refers to the number of scores mentioned in the premise
if len(hypothesis_scores) <= len(premise_scores):
    # check if the hypothesis value contradicts the number of scores in the premise
    label = "contradiction"
elif hypothesis_scores!= premise_scores:
    # check if the hypothesis scores contradict the premise scores
    label = "contradiction"
else:
    # if the hypothesis scores and estimates do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
