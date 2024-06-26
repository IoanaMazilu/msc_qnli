average_score_premise = 95
average_score_hypothesis = 65
tests_premise = 5
tests_hypothesis = 5

# The hypothesis refers to the average score and the number of tests mentioned in the premise
if tests_premise != tests_hypothesis:
    # Check if the number of tests in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
elif average_score_premise != average_score_hypothesis:
    # Check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
