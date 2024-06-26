average_score_premise = 18
average_score_hypothesis = 38

# the hypothesis refers to the average golf score of Scott in his first four rounds, which is also mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
