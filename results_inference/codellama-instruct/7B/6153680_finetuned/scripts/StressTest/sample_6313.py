males_premise = 2
females_premise = 3
males_hypothesis = 4
females_hypothesis = 3

# the hypothesis talks about the number of males and females, which is also mentioned in the premise
if males_hypothesis!= males_premise or females_hypothesis!= females_premise:
    # check if the number of males or females in the hypothesis contradicts the number of males or females in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
