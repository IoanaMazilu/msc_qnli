nancy_marks_premise = [66, 75, 52, 68, 89]
nancy_marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis refers to the exact marks obtained by Nancy in each subject
if nancy_marks_hypothesis == nancy_marks_premise:
    # check if the hypothesis values contradict the premise ones
    label = "entailment"
else:
    # the hypothesis values do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
