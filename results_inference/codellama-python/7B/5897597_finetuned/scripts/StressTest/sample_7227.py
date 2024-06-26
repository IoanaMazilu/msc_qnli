# defining the marks obtained by Nancy in each subject according to the premise
marks_premise = [66, 75, 52, 68, 89]

# defining the marks obtained by Nancy in each subject according to the hypothesis
marks_hypothesis = [86, 75, 52, 68, 89]

# comparing the marks obtained by Nancy in the premise and hypothesis
if marks_premise[0] >= marks_hypothesis[0] or marks_premise[1] >= marks_hypothesis[1] or marks_premise[2] >= marks_hypothesis[2] or marks_premise[3] >= marks_hypothesis[3] or marks_premise[4] >= marks_hypothesis[4]:
    # if any of the marks obtained in the premise is greater than or equal to the corresponding mark in the hypothesis
    label = "contradiction"
else:
    # if none of the marks obtained in the premise is greater than or equal to the corresponding mark in the hypothesis
    label = "entailment"

print(label)
