# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 45.
# Hypothesis: Joe’s average (arithmetic mean) test score across more than 3 equally weighted tests was 45.
# Golden Label: entailment

# Define the variables
average_test_score_premise = 45
tests_premise = 4

average_test_score_hypothesis = 45
tests_hypothesis = 3

# the hypothesis refers to the average test score and the number of tests which are also mentioned in the premise
if average_test_score_premise != average_test_score_hypothesis:
    # check if the average test score in the hypothesis contradicts the average in the premise
    label = "contradiction"
elif tests_premise <= tests_hypothesis:
    # check if the number of tests in the premise contradicts the estimate of more than 'tests_hypothesis' tests
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

