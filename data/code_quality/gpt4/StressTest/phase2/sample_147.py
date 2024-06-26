average_grade_premise = 78
average_grade_hypothesis = 48

# both the premise and hypothesis speak about the average grade after Bob took a test
if average_grade_premise <= average_grade_hypothesis:
    # check if the average grade in the premise contradicts the estimate of more than 'average_grade_hypothesis'
    label = "contradiction"
else:
    # if the average grade in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
