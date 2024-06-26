score_premise = 10
score_hypothesis = 30
average_score_premise = 83
average_score_hypothesis = 83

# the hypothesis talks about Robin's score on a 30th test, which is not mentioned in the premise
if score_hypothesis!= score_premise:
    # check if Robin's score on the 30th test contradicts the score on the 10th test
    label = "contradiction"
elif average_score_hypothesis!= average_score_premise:
    # check if Robin's average score on the 10 tests contradicts the average score on the 10 tests
    label = "contradiction"
else:
    # if the scores and averages do not contradict, we can infer entailment
    label = "entailment"

print(label)
