# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 85.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first less than 8 of 4 tests is 85.
# Golden Label: entailment

num_tests_premise = 3
num_tests_hypothesis = 8
avg_score_premise = 85
avg_score_hypothesis = 85

# the hypothesis talks about the average score and number of tests taken by Jerry, referenced also in the premise
if num_tests_hypothesis > num_tests_premise:
    # check if the hypothesis value contradicts the number of tests mentioned in the premise
    label = "contradiction"
elif avg_score_hypothesis != avg_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

