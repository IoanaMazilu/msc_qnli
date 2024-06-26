tests_premise = 4
tests_hypothesis = 6

# the hypothesis refers to the number of tests Joe took, which is also mentioned in the premise
if tests_premise >= tests_hypothesis:
    # check if the number of tests in the premise contradicts the number of tests in the hypothesis
    label = "contradiction"
elif tests_premise < tests_hypothesis:
    # if the number of tests in the premise is less than the number of tests in the hypothesis, it can be entailed
    label = "entailment"
else:
    # if the number of tests in the premise is equal to the number of tests in the hypothesis, it cannot be explicitly entailed
    label = "neutral"

print(label)
