average_marks_premise = 35
average_marks_hypothesis = 75

# the hypothesis refers to the number of marks secured by Reema mentioned in the premise
if average_marks_hypothesis == average_marks_premise:
    # check if the hypothesis value contradicts the average marks in the premise
    label = "contradiction"
else:
    # any number of marks greater than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
