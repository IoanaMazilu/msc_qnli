marks_premise = [40, 60, 70, 80, 80]
marks_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the marks obtained by Reeya in different subjects, referenced also in the premise
if any(mark_hypothesis >= mark_premise for mark_hypothesis, mark_premise in zip(marks_hypothesis, marks_premise)):
    # check if any of the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
