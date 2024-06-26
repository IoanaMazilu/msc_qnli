average_grade_premise = 79
average_grade_hypothesis = 29

# The hypothesis refers to the average grade that Alice got after she took the test
if average_grade_premise < average_grade_hypothesis:
    # check if the average grade in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif average_grade_premise == average_grade_hypothesis:
    # check if the average grade in the premise contradicts the estimate of more than 'average_grade_hypothesis'
    label = "contradiction"
else:
    # if the average grade in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
