# Premise: Nick's average (arithmetic mean) test score on 4 tests is 78.
# Hypothesis: Nick's average (arithmetic mean) test score on less than 7 tests is 78.
# Golden Label: entailment

average_test_score_premise = 78
tests_taken_premise = 4
average_test_score_hypothesis = 78
tests_taken_hypothesis = 7

# the hypothesis is about Nick's average test score and total tests taken, mentioned in the premise as well
if average_test_score_hypothesis != average_test_score_premise:
    # check if the average test scores in the hypothesis contradicts the average test scores in the premise
    label = "contradiction"
elif tests_taken_hypothesis <= tests_taken_premise:
    # check if the total tests taken in the hypothesis contradicts the total tests taken in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

