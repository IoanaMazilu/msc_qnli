# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 35.
# Hypothesis: Joe’s average (arithmetic mean) test score across more than 4 equally weighted tests was 35.
# Golden Label: contradiction

tests_count_premise = 4
tests_count_hypothesis = 5  # assuming a minimum increase
average_score_premise = 35
average_score_hypothesis = 35

# the hypothesis refers to the number of tests and average test score mentioned in the premise
if tests_count_premise >= tests_count_hypothesis:
    # check if the hypothesis value contradicts the premise's number of tests
    label = "contradiction"
elif average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, the relation is neutral
    # because the premise does not give information for more than 'tests_count_premise' tests
    label = "neutral"

print(label)

