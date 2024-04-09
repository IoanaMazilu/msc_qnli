marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [less_than_86, less_than_75, less_than_52, less_than_68, less_than_89]

# the hypothesis refers to the marks obtained by Nancy in different subjects
for i in range(len(marks_premise)):
    if marks_premise[i] <= marks_hypothesis[i]:
        label = "contradiction"
    else:
        # the premise gives an estimate for the marks obtained by Nancy in each subject
        # any marks value greater than'marks_hypothesis[i]' is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"
print(label)
