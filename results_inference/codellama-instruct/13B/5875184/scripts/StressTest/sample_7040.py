premise_marks = [56, 60, 72, 85, 80]
hypothesis_marks = [less than 56, 60, 72, 85, 80]

# the hypothesis refers to the number of marks obtained in each subject
if len(hypothesis_marks) < len(premise_marks):
    # check if the hypothesis value contradicts the number of marks obtained in each subject in the premise
    label = "contradiction"
elif hypothesis_marks[0] > premise_marks[0]:
    # check if the hypothesis value contradicts the number of marks obtained in the first subject in the premise
    label = "contradiction"
elif hypothesis_marks[1] > premise_marks[1]:
    # check if the hypothesis value contradicts the number of marks obtained in the second subject in the premise
    label = "contradiction"
elif hypothesis_marks[2] > premise_marks[2]:
    # check if the hypothesis value contradicts the number of marks obtained in the third subject in the premise
    label = "contradiction"
elif hypothesis_marks[3] > premise_marks[3]:
    # check if the hypothesis value contradicts the number of marks obtained in the fourth subject in the premise
    label = "contradiction"
elif hypothesis_marks[4] > premise_marks[4]:
    # check if the hypothesis value contradicts the number of marks obtained in the fifth subject in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
