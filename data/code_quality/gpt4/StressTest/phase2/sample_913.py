average_marks_difference_premise = 24
average_marks_difference_hypothesis = 14

# the hypothesis refers to the difference in average marks between sets of subjects mentioned in the premise
if average_marks_difference_hypothesis >= average_marks_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_difference_premise'
    label = "contradiction"
elif average_marks_difference_hypothesis < average_marks_difference_premise:
    # check if the hypothesis value is less than 'average_marks_difference_premise' and hence can be entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise, and cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
