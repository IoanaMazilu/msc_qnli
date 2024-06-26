nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis talks about the number of marks in each subject, referenced also in the premise
if nancy_marks_hypothesis[0] <= nancy_marks_premise[0]:
    # check if the hypothesis value contradicts the estimate of less than 'nancy_marks_premise[0]'
    label = "contradiction"
elif nancy_marks_hypothesis[1]!= nancy_marks_premise[1]:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[2]!= nancy_marks_premise[2]:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[3]!= nancy_marks_premise[3]:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif nancy_marks_hypothesis[4]!= nancy_marks_premise[4]:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
