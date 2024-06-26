test_score_premise = 10
test_score_hypothesis = 70
average_score_premise = 83
average_score_hypothesis = 83

# the hypothesis refers to Robin's average score on the 10 tests, which is also mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average scores in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
