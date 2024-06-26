marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [0, 0, 0, 0, 0]

# check if the hypothesis values contradict the premise values
for i in range(len(marks_premise)):
    if marks_hypothesis[i] < marks_premise[i]:
        label = "contradiction"
        break
    elif marks_hypothesis[i] > marks_premise[i]:
        label = "entailment"
        break
    else:
        label = "neutral"

print(label)
