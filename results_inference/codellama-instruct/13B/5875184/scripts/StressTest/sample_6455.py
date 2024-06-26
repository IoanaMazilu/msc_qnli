premise_marks = [66, 60, 72, 77, 55, 85]
hypothesis_marks = [less than 66, 60, 72, 77, 55, 85]

# calculate the average mark for the premise
premise_average = sum(premise_marks) / len(premise_marks)

# calculate the average mark for the hypothesis
hypothesis_average = sum(hypothesis_marks) / len(hypothesis_marks)

# check if the hypothesis average is less than the premise average
if hypothesis_average < premise_average:
    label = "entailment"
else:
    label = "neutral"

print(label)
