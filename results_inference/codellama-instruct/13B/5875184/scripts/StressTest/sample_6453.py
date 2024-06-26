premise_marks = [66, 60, 72, 77, 55, 85]
hypothesis_marks = [less_than_76, 60, 72, 77, 55, 85]

# calculate the average mark scored by Andrea in the premise
premise_average = sum(premise_marks) / len(premise_marks)

# calculate the average mark scored by Andrea in the hypothesis
hypothesis_average = sum(hypothesis_marks) / len(hypothesis_marks)

# check if the hypothesis value contradicts the premise value
if hypothesis_average < premise_average:
    label = "contradiction"
else:
    label = "neutral"

print(label)
