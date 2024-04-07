# Premise: Ravi's average (arithmetic mean) test score on 4 tests is 78.
# Hypothesis: Ravi's average (arithmetic mean) test score on less than 5 tests is 78.
# Golden Label: entailment

tests_premise = 4
tests_hypothesis = 5
avg_score_premise = 78
avg_score_hypothesis = 78

# the hypothesis refers to the average test score and number of tests taken by Ravi mentioned in the premise
if avg_score_premise != avg_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
elif tests_premise >= tests_hypothesis:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

