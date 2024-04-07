# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 90.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 6 equally weighted tests was 90.
# Golden Label: entailment

num_tests_premise = 4
num_tests_hypothesis = 6
avg_score_premise = 90
avg_score_hypothesis = 90

# the hypothesis talks about the average test score and number of tests, which are also mentioned in the premise
if num_tests_hypothesis <= num_tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif avg_score_hypothesis != avg_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

