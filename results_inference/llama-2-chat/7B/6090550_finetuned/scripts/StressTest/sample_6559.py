 score_premise = 78
tests_premise = 4
tests_hypothesis = 3

# the hypothesis refers to the average score of Jerry on the first 3 tests, which is also mentioned in the premise
if tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
else:
    # if the number of tests in the hypothesis is less than the number of tests in the premise, we can infer entailment
    label = "entailment"

print(label)

