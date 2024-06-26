males_premise = 5
males_hypothesis = 3
females_premise = 4
females_hypothesis = 4

# the hypothesis refers to the number of males and females mentioned in the premise
if males_hypothesis >= males_premise:
    # check if the number of males in the hypothesis contradicts the number of males mentioned in the premise
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
