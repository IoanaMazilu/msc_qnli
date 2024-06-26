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
