marks_premise = [86, 75, 52, 68, 89]
marks_hypothesis = [66, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in the five subjects mentioned in the premise
if all(mark_hypothesis <= mark_premise for mark_hypothesis, mark_premise in zip(marks_hypothesis, marks_premise)):
    # check if all the marks in the hypothesis are less than or equal to the marks in the premise
    label = "entailment"
else:
    # if any of the marks in the hypothesis is greater than the corresponding mark in the premise, we can infer contradiction
    label = "contradiction"

print(label)
