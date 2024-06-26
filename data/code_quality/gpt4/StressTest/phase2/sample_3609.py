average_marks_diff_premise = 20
average_marks_diff_hypothesis = 40

# the hypothesis refers to the difference in average marks in certain subjects mentioned in the premise
if average_marks_diff_hypothesis < average_marks_diff_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_diff_premise'
    label = "contradiction"
elif average_marks_diff_hypothesis != average_marks_diff_premise:
    # check if the hypothesis value is not the same as the premise value
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
