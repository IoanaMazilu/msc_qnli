males_premise = 7
males_hypothesis = 6
females_premise = 3
females_hypothesis = 3

# the hypothesis refers to the same situation described in the premise, with a specific number of males and females
if males_hypothesis >= males_premise:
    # check if the number of males in the hypothesis contradicts the premise (less than 'males_premise')
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
