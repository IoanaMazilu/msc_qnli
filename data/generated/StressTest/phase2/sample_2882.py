# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 94.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first 5 of 4 tests is 94.
# Golden Label: contradiction

total_tests_premise = 4
average_tests_premise = 3

total_tests_hypothesis = 4
average_tests_hypothesis = 5

# the hypothesis refers to more average tests than the total tests in the premise
if average_tests_hypothesis > total_tests_premise:
    # check if the number of average tests in the hypothesis contradicts the number of total tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

