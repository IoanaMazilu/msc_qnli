# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 90.
# Hypothesis: Joe’s average (arithmetic mean) test score across more than 4 equally weighted tests was 90.
# Golden Label: contradiction

total_tests_premise = 4
average_score_premise = 90
total_tests_hypothesis = 5
average_score_hypothesis = 90

# the hypothesis talks about the average test score and number of tests, referenced also in the premise
if total_tests_hypothesis <= total_tests_premise:
    # check if number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # the premise gives the average score for 'total_tests_premise' tests
    # the average score for 'total_tests_hypothesis' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

