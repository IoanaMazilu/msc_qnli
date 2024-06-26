males_premise = 3
males_hypothesis = 1
females_premise = 4
females_hypothesis = 4

# the hypothesis refers to the number of males and females mentioned in the premise
if males_premise != males_hypothesis:
    # check if the number of males in the hypothesis contradicts the number of males reported in the premise
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
