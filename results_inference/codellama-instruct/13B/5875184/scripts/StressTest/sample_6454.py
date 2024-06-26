premise_marks = [76, 60, 72, 77, 55, 85]
hypothesis_marks = [66, 60, 72, 77, 55, 85]

# calculate the average mark for the premise
premise_avg = sum(premise_marks) / len(premise_marks)

# calculate the average mark for the hypothesis
hypothesis_avg = sum(hypothesis_marks) / len(hypothesis_marks)

# check if the hypothesis average is greater than the premise average
if hypothesis_avg > premise_avg:
    label = "entailment"
elif hypothesis_avg < premise_avg:
    label = "contradiction"
else:
    label = "neutral"

print(label)
