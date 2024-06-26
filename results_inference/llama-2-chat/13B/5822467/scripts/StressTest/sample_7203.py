marks_premise = 85
marks_hypothesis = 60

# convert the premise and hypothesis to floats for comparison
marks_premise_float = float(marks_premise)
marks_hypothesis_float = float(marks_hypothesis)

# calculate the average marks up to two decimal places
average_marks_premise = marks_premise_float / 2
average_marks_hypothesis = marks_hypothesis_float / 2

# compare the average marks
if average_marks_hypothesis < average_marks_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif average_marks_hypothesis > average_marks_premise:
    # the hypothesis entails the premise
    label = "entailment"
else:
    # the premise and hypothesis are neutral
    label = "neutral"

print(label)
