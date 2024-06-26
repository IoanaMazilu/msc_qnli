marks_scored_premise = [76, 65, 82, 67, 75]
marks_scored_hypothesis = [76, 65, 82, 67, 75]

# the hypothesis refers to the marks scored in different subjects as mentioned in the premise
if any(marks_scored_hypothesis <= marks_scored_premise[i] for i in range(6)):
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks scored
    # any number of marks greater than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
