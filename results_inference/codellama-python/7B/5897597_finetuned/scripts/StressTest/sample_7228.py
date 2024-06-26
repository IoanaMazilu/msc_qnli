# defining the marks obtained by Nancy in each subject according to the premise
marks_premise = [86, 75, 52, 68, 89]
# defining the marks obtained by Nancy in each subject according to the hypothesis
marks_hypothesis = [66, 75, 52, 68, 89]

# comparing the marks obtained by Nancy in the hypothesis with the marks obtained in the premise
for i in range(len(marks_premise)):
    if marks_hypothesis[i] >= marks_premise[i]:
        # if the marks obtained in the hypothesis contradict the marks obtained in the premise
        label = "contradiction"
        break
else:
    # if the marks obtained in the hypothesis do not contradict the marks obtained in the premise
    # but also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
