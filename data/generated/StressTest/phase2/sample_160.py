# Premise: Joe’s average (arithmetic mean) test score across less than 6 equally weighted tests was 90.
# Hypothesis: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 90.
# Golden Label: neutral

num_tests_premise = 6
num_tests_hypothesis = 4
avg_score_premise = 90
avg_score_hypothesis = 90

# the hypothesis talks about the number of tests and the average score, both referenced also in the premise
if num_tests_hypothesis >= num_tests_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'num_tests_premise'
    label = "contradiction"
elif avg_score_hypothesis != avg_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

