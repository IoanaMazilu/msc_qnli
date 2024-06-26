premise_marks = [76, 65, 82, 67, 75]
hypothesis_marks = [46, 65, 82, 67, 75]

# the hypothesis refers to the number of marks scored in each subject
if hypothesis_marks[0] > premise_marks[0]:
    # check if the estimate of 'hypothesis_marks[0]' contradicts the number of marks scored in Mathematics in the premise
    label = "contradiction"
elif hypothesis_marks[1]!= premise_marks[1]:
    # check if the number of marks scored in Science in the hypothesis contradicts the number of marks scored in the premise
    label = "contradiction"
elif hypothesis_marks[2]!= premise_marks[2]:
    # check if the number of marks scored in Social studies in the hypothesis contradicts the number of marks scored in the premise
    label = "contradiction"
elif hypothesis_marks[3]!= premise_marks[3]:
    # check if the number of marks scored in English in the hypothesis contradicts the number of marks scored in the premise
    label = "contradiction"
elif hypothesis_marks[4]!= premise_marks[4]:
    # check if the number of marks scored in Biology in the hypothesis contradicts the number of marks scored in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
