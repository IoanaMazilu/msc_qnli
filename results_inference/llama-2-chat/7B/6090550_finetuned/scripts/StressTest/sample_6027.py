average_premise = 50
tests_premise = 4
tests_hypothesis = 6

# the hypothesis refers to the number of tests mentioned in the premise
if tests_hypothesis < tests_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
