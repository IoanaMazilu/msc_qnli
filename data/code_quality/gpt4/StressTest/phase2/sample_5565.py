marks_premise = [70, 57, 69, 89, 85]
marks_hypothesis = [10, 57, 69, 89, 85]

# calculate the average score in the premise
average_score_premise = sum(marks_premise) / len(marks_premise)

# the hypothesis talks about the average score too, but with a different mark for the first subject
if marks_hypothesis[0] > marks_premise[0]:
    # check if the new mark contradicts the initial mark from the premise
    label = "contradiction"
elif marks_hypothesis[1:] != marks_premise[1:]:
    # check if the rest of the marks are different
    label = "contradiction"
else:
    # a different mark for the first subject is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
