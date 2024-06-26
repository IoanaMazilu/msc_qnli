males_premise = 4
males_hypothesis = 4
females_premise = 3
females_hypothesis = 3

# the hypothesis refers to the number of males and females mentioned in the premise
if males_hypothesis <= males_premise:
    # check if the number of males in the hypothesis contradicts the number of males in the premise
    label = "contradiction"
elif females_hypothesis!= females_premise:
    # check if the number of females in the hypothesis contradicts the number of females in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
