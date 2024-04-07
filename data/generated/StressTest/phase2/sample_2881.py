# Premise: Jerry’s average (arithmetic mean) score on the first less than 7 of 4 tests is 94.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 94.
# Golden Label: neutral

tests_taken_premise = 7
tests_taken_hypothesis = 3
average_score_premise = 94
average_score_hypothesis = 94

# the hypothesis talks about the number of tests taken and the average scores, both mentioned in the premise
if tests_taken_hypothesis > tests_taken_premise:
    # check if the number of tests taken in the hypothesis contradicts the estimate of less than 'tests_taken_premise'
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

