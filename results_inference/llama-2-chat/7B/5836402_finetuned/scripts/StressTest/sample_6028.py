tests_premise = 6
tests_hypothesis = 4

# the hypothesis refers to the number of tests Joe took, which is also mentioned in the premise
if tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
else:
    # if the number of tests in the hypothesis does not contradict the number of tests in the premise, we can infer entailment
    label = "entailment"

print(label)
