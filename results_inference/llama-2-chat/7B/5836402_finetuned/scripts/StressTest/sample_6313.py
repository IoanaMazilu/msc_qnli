males_premise = 2
males_hypothesis = 4
females_premise = 3
females_hypothesis = 3

# the hypothesis talks about the number of males and females, referenced also in the premise
if males_hypothesis < males_premise:
    # check if the hypothesis value contradicts the estimate of more than'males_premise'
    label = "contradiction"
elif females_hypothesis!= females_premise:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males greater than'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
