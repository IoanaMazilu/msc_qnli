# Premise: The average of Pratyush's marks in more than 4 subjects is 75.
# Hypothesis: The average of Pratyush's marks in 7 subjects is 75.
# Golden Label: neutral

average_marks_premise = 75
subjects_premise = 4
average_marks_hypothesis = 75
subjects_hypothesis = 7

# the hypothesis refers to the number of subjects and average marks mentioned in the premise
if average_marks_hypothesis != average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks reported in the premise
    label = "contradiction"
elif subjects_hypothesis <= subjects_premise:
    # check if the number of subjects in the hypothesis contradicts the estimate of more than 'subjects_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of subjects
    # any number of subjects greater than 'subjects_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

