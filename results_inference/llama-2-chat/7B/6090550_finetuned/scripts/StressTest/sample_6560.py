 score_premise_3_tests = 78
score_hypothesis_6_tests = 78

# the hypothesis talks about the average score of the first 6 tests, referenced also in the premise
if score_hypothesis_6_tests!= score_premise_3_tests:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are equal, we can infer entailment
    label = "entailment"

print(label)
