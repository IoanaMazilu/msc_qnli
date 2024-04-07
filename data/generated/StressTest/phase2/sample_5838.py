# Premise: The next day, Ella took the test, and with this grade included, the new average was 75.
# Hypothesis: The next day, Ella took the test, and with this grade included, the new average was less than 85.
# Golden Label: entailment

average_grade_premise = 75
average_grade_hypothesis = 85

# the hypothesis refers to the average grade mentioned in the premise
if average_grade_premise > average_grade_hypothesis:
    # check if the 'average_grade_premise' contradicts the estimate of less than 'average_grade_hypothesis'
    label = "contradiction"
elif average_grade_premise == average_grade_hypothesis:
    # check if the 'average_grade_premise' contradicts the estimate of less than 'average_grade_hypothesis'
    label = "contradiction"
else:
    # if the average grade in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

