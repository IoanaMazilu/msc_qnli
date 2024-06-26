nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis refers to the number of marks obtained in each subject, mentioned in the premise
if nancy_marks_hypothesis[0] <= nancy_marks_premise[0]:
    # check if the estimate of 'nancy_marks_hypothesis[0]' contradicts the number of marks in American Literature in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[1]!= nancy_marks_premise[1]:
    # check if the number of marks in History in the hypothesis contradicts the number of marks in History reported in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[2]!= nancy_marks_premise[2]:
    # check if the number of marks in Home Economics in the hypothesis contradicts the number of marks in Home Economics reported in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[3]!= nancy_marks_premise[3]:
    # check if the number of marks in Physical Education in the hypothesis contradicts the number of marks in Physical Education reported in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[4]!= nancy_marks_premise[4]:
    # check if the number of marks in Art in the hypothesis contradicts the number of marks in Art reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
