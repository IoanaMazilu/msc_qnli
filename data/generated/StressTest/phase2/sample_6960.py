# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 60.
# Hypothesis: Joe’s average (arithmetic mean) test score across more than 2 equally weighted tests was 60.
# Golden Label: entailment

num_tests_premise = 4
num_tests_hypothesis = 2
avg_score_premise = 60
avg_score_hypothesis = 60

# the hypothesis refers to the number of tests and the average score mentioned in the premise
if num_tests_hypothesis >= num_tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
elif avg_score_hypothesis != avg_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

