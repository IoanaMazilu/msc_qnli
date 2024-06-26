average_score_premise = 78
average_score_hypothesis = 78

# the hypothesis refers to the average score of Jerry on the first 6 of 4 tests, which is also mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
