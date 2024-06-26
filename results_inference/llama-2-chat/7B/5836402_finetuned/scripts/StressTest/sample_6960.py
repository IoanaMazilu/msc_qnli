tests_premise = 4
tests_hypothesis = 2

# the hypothesis refers to the number of tests Joe took, which is also mentioned in the premise
if tests_premise > tests_hypothesis:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif tests_hypothesis == 0:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
