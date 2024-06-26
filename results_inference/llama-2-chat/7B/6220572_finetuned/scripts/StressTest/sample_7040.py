average_marks_premise = [56, 60, 72, 85, 80]
average_marks_hypothesis = [56, 60, 72, 85, 80]

# the hypothesis refers to the average marks of a student in different subjects, also mentioned in the premise
if average_marks_hypothesis[0] <= average_marks_premise[0]:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_premise[0]'
    label = "contradiction"
elif average_marks_hypothesis[1]!= average_marks_premise[1]:
    # check if the number of marks in History and Government in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif average_marks_hypothesis[2]!= average_marks_premise[2]:
    # check if the number of marks in Art in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif average_marks_hypothesis[3]!= average_marks_premise[3]:
    # check if the number of marks in Computer Science in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif average_marks_hypothesis[4]!= average_marks_premise[4]:
    # check if the number of marks in Modern Literature in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
