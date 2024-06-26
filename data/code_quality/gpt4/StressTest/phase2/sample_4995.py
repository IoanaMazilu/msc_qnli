average_grade_premise = 76
average_grade_hypothesis = 16

# the hypothesis talks about the average grade after Dan took the test, referenced also in the premise
if average_grade_premise <= average_grade_hypothesis:
    # check if the average grade in the premise contradicts the estimate of more than 'average_grade_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
