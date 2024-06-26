marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis refers to the marks obtained by Nancy in each subject, as mentioned in the premise
if marks_hypothesis == marks_premise:
    # check if the marks in the hypothesis match the marks in the premise
    label = "entailment"
elif any(marks_hypothesis[i]!= marks_premise[i] for i in range(5)):
    # check if the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
