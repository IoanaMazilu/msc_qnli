premise_scores = [8, 2, 3]
hypothesis_scores = [1, 2, 3]

# the hypothesis refers to the scores mentioned in the premise
if hypothesis_scores[0] <= premise_scores[0]:
    # check if the estimate of 'hypothesis_scores[0]' contradicts the number of scores in the premise
    label = "contradiction"
elif hypothesis_scores[1]!= premise_scores[1]:
    # check if the number of scores in the hypothesis contradicts the number of scores reported in the premise
    label = "contradiction"
elif hypothesis_scores[2]!= premise_scores[2]:
    # check if the number of scores in the hypothesis contradicts the number of scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
