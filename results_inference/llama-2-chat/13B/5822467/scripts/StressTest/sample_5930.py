marks_premise = [86, 85, 92, 87, 95]
marks_hypothesis = [85, 80, 90, 80, 90]

# check if the hypothesis values contradict the premise values
for i in range(len(marks_premise)):
    if marks_hypothesis[i] < marks_premise[i]:
        label = "contradiction"
        break
    elif marks_hypothesis[i] == marks_premise[i]:
        label = "neutral"
        continue
    else:
        label = "entailment"

print(label)
