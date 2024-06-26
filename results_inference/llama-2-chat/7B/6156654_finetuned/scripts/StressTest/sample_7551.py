# the premise mentions a group of 6 boys and 4 girls, and the hypothesis mentions a group of more than 2 boys and 4 girls
if (6 + 4) <= 2 + 4:
    # check if the sum of boys and girls in the premise is less than or equal to the sum in the hypothesis
    label = "contradiction"
else:
    # if the sum is greater than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
