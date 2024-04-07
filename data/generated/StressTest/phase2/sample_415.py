# Premise: Jerry’s average (arithmetic mean) score on the first less than 8 of 4 tests is 81.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 81.
# Golden Label: neutral

tests_premise = 8
tests_hypothesis = 3
average_score_premise = 81
average_score_hypothesis = 81

# the hypothesis talks about the number of tests and average score, referenced also in the premise
if tests_hypothesis > tests_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'tests_premise'
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # the exact number of tests in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

