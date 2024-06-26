males_premise = 3
males_hypothesis = 2
females_premise = 3
females_hypothesis = 3

# the hypothesis talks about the number of males and females, referenced also in the premise
if males_hypothesis >= males_premise:
    # check if the hypothesis value contradicts the estimate of 'males_premise'
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
