tests_premise = 4
tests_hypothesis = 4

# the hypothesis refers to the number of tests mentioned in the premise
if tests_hypothesis < tests_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif tests_hypothesis > tests_premise:
    # the premise gives only an upper limit for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
