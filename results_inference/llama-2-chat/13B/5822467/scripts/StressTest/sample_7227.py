marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [less than 86, 75, 52, 68, 89]

# iterate through the marks in the premise and compare them to the hypothesis
for mark in marks_premise:
    if mark <= marks_hypothesis[0]:
        # check if the estimate of'marks_hypothesis[0]' contradicts the mark in the premise
        label = "contradiction"
    elif marks_hypothesis[1:] and any(mark not in marks for marks in marks_hypothesis[1:]):
        # check if any of the marks in the hypothesis contradict the marks in the premise
        label = "contradiction"
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"
        break

print(label)
