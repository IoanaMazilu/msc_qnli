# Premise: Joe’s average (arithmetic mean) test score across less than 5 equally weighted tests was 70.
# Hypothesis: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 70.
# Golden Label: neutral

average_score_premise = 70
tests_taken_premise = 5
average_score_hypothesis = 70
tests_taken_hypothesis = 4

# The hypothesis is about Joe's test scores, which is also referenced in the premise
if average_score_hypothesis != average_score_premise:
    # Check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
elif tests_taken_hypothesis >= tests_taken_premise:
    # Check if the number of tests taken in the hypothesis contradicts the estimate of less than 'tests_taken_premise' tests taken
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

