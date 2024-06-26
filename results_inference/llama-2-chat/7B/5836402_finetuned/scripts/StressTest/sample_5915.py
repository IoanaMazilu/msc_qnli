tests_premise = 4
tests_hypothesis = 4
tests_premise_score = 3
tests_hypothesis_score = 3

# the hypothesis refers to the number of tests and the score mentioned in the premise
if tests_hypothesis < tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif tests_hypothesis_score!= tests_premise_score:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
