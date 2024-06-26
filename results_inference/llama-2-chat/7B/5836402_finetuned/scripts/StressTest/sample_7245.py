tests_premise = 4
tests_hypothesis = 3

# the hypothesis refers to the number of tests taken by Joe, which is also mentioned in the premise
if tests_hypothesis < tests_premise:
    # check if the hypothesis value contradicts the premise value of 'tests_premise'
    label = "contradiction"
elif math.fabs(tests_hypothesis - tests_premise) > 1:
    # check if the difference between the number of tests in the hypothesis and the premise is greater than 1
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
