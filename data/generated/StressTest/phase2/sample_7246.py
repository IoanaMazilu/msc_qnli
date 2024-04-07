# Premise: Joe’s average (arithmetic mean) test score across more than 3 equally weighted tests was 45.
# Hypothesis: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 45.
# Golden Label: neutral

average_score_premise = 45
num_tests_premise = 3
average_score_hypothesis = 45
num_tests_hypothesis = 4

# the hypothesis refers to the average test score and number of tests mentioned in the premise
if average_score_hypothesis != average_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif num_tests_hypothesis <= num_tests_premise:
    # check if the number of tests in the hypothesis contradicts the lower limit of tests reported in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the number of tests
    # any number of tests greater than 'num_tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

