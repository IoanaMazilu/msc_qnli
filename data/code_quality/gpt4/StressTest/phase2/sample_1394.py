males_premise = 6
females_premise = 3
males_hypothesis = 4
females_hypothesis = 3

# the hypothesis refers to the same situation as the premise, but with a different number of males
if males_hypothesis != males_premise:
    # the number of males in the hypothesis contradicts the number of males in the premise
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females in the premise
    label = "contradiction"
else:
    # the number of females is the same in both the premise and the hypothesis
    label = "entailment"

print(label)
