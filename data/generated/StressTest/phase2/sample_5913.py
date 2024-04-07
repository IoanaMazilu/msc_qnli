# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 90.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first less than 4 of 4 tests is 90.
# Golden Label: entailment

tests_taken_premise = 3
tests_taken_hypothesis = 4
avg_score_premise = 90
avg_score_hypothesis = 90

# the hypothesis refers to the number of taken tests and their average score mentioned in the premise
if tests_taken_premise != tests_taken_hypothesis - 1:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken in the premise
    label = "contradiction"
elif avg_score_premise != avg_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

