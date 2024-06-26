nancy_marks_premise = [86, 75, 52, 68, 89]
nancy_marks_hypothesis = [66, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in certain subjects, which are also mentioned in the premise
for i in range(len(nancy_marks_premise)):
    if nancy_marks_premise[i] > nancy_marks_hypothesis[i]:
        # check if the premise value exceeds the hypothesis value
        label = "contradiction"
        break
    elif nancy_marks_hypothesis[i]!= nancy_marks_premise[i]:
        # check if the hypothesis value contradicts the premise value
        label = "contradiction"
        break
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
