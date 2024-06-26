premise_marks = [76, 65, 82, 67, 85]
hypothesis_marks = [86, 65, 82, 67, 85]

# the hypothesis talks about the number of marks in each subject
# the premise gives the exact number of marks in each subject
if hypothesis_marks[0] <= premise_marks[0]:
    # check if the hypothesis value contradicts the premise value for the first subject
    label = "contradiction"
elif hypothesis_marks[1]!= premise_marks[1]:
    # check if the hypothesis value contradicts the premise value for the second subject
    label = "contradiction"
elif hypothesis_marks[2]!= premise_marks[2]:
    # check if the hypothesis value contradicts the premise value for the third subject
    label = "contradiction"
elif hypothesis_marks[3]!= premise_marks[3]:
    # check if the hypothesis value contradicts the premise value for the fourth subject
    label = "contradiction"
elif hypothesis_marks[4]!= premise_marks[4]:
    # check if the hypothesis value contradicts the premise value for the fifth subject
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
