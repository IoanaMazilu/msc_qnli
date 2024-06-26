marks_premise = 36
marks_hypothesis = 86
correct_marks = 66

# the hypothesis refers to the marks secured by Reema that is mentioned in the premise
if marks_hypothesis <= correct_marks:
    # check if the estimate of 'marks_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif marks_premise != correct_marks:
    # check if the number of marks in the hypothesis contradicts the number of correct marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an incorrect value for the number of marks
    # any number of marks less than 'marks_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
