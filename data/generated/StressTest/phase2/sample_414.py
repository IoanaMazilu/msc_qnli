# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 81.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first less than 8 of 4 tests is 81.
# Golden Label: entailment

tests_taken_premise = 3
tests_taken_hypothesis = 8
average_score_premise = 81
average_score_hypothesis = 81

# the hypothesis talks about the number of tests taken by Jerry and his average score, referenced also in the premise
if tests_taken_hypothesis < tests_taken_premise or average_score_hypothesis != average_score_premise:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken in the premise
    # or if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

