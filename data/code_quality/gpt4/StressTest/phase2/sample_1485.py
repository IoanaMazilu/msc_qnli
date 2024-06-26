average_marks_premise = 17
average_marks_hypothesis = 47

# the hypothesis mentions the average marks scored by Ganesh in specific subjects, which is also mentioned in the premise
if average_marks_hypothesis <= average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' contradicts the estimate in the premise
    label = "contradiction"
elif average_marks_premise != average_marks_hypothesis:
    # any other value of 'average_marks_hypothesis' would neither explicitly entail nor contradict the premise
    label = "neutral"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
