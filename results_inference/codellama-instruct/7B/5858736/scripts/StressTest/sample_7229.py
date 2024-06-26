marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in the five subjects mentioned in the premise
if all(mark_hypothesis <= mark_premise for mark_hypothesis, mark_premise in zip(marks_hypothesis, marks_premise)):
    # check if the hypothesis values do not contradict the premise ones
    label = "entailment"
else:
    # the hypothesis values contradict the premise ones
    label = "contradiction"

print(label)
