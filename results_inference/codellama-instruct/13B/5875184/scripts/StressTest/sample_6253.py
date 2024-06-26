premise_scores = [7, 2, 3, 4]
hypothesis_scores = [1, 2, 3, 4]

# the hypothesis refers to the scores mentioned in the premise
if hypothesis_scores[0] <= premise_scores[0]:
    # check if the hypothesis value contradicts the estimate of 'premise_scores[0]'
    label = "contradiction"
elif hypothesis_scores[1]!= premise_scores[1]:
    # check if the hypothesis value contradicts the number of scores in the premise
    label = "contradiction"
elif hypothesis_scores[2]!= premise_scores[2]:
    # check if the hypothesis value contradicts the number of scores in the premise
    label = "contradiction"
elif hypothesis_scores[3]!= premise_scores[3]:
    # check if the hypothesis value contradicts the number of scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
