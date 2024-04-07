# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 50.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 6 equally weighted tests was 50.
# Golden Label: entailment

tests_premise = 4
tests_hypothesis = 6
average_score_premise = 50
average_score_hypothesis = 50

# The hypothesis refers to the number of tests and average score mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # Check if the average test score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif tests_hypothesis <= tests_premise:
    # Check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

