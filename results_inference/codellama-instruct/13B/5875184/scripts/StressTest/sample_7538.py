premise_scores = [40, 60, 70, 80, 80]
hypothesis_scores = [less than 40, 60, 70, 80, 80]

# the hypothesis talks about the scores in different subjects, referenced also in the premise
if hypothesis_scores[0] <= premise_scores[0]:
    # check if the hypothesis value contradicts the estimate of more than 'premise_scores[0]'
    label = "contradiction"
elif hypothesis_scores[1]!= premise_scores[1]:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
