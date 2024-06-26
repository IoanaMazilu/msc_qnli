score_hypothesis = 78
score_premise = 78
tests = 4
tests_hypothesis = 3

# the hypothesis refers to the average score on the first less than 6 tests, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
elif tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
