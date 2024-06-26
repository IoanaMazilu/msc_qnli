premise_marks = [46, 75, 72, 63, 65]
hypothesis_marks = [86, 75, 72, 63, 65]

# calculate the average mark for the premise
premise_avg = sum(premise_marks) / len(premise_marks)

# calculate the average mark for the hypothesis
hypothesis_avg = sum(hypothesis_marks) / len(hypothesis_marks)

# check if the hypothesis value contradicts the premise estimate
if hypothesis_avg > premise_avg:
    label = "contradiction"
else:
    label = "neutral"

print(label)
