average_marks_premise = 56
average_marks_hypothesis = 56

# the hypothesis refers to the average marks of a student in certain subjects, which are also mentioned in the premise
if average_marks_premise >= average_marks_hypothesis:
    # check if the average marks in the premise contradicts the hypothesis of less than 'average_marks_hypothesis'
    label = "contradiction"
else:
    # if the average marks in the premise is less than 'average_marks_hypothesis', it entails the hypothesis
    label = "entailment"

print(label)
