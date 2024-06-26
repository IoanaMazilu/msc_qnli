males_premise = 2
males_hypothesis = 8
females_premise = 3
females_hypothesis = 3

# the hypothesis talks about the number of males and females around a table, also referenced in the premise
if males_hypothesis < males_premise:
    # check if the number of males in the hypothesis contradicts the number of males in the premise
    label = "contradiction"
elif females_hypothesis != females_premise:
    # check if the number of females in the hypothesis contradicts the number of females in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of males and females
    # any number of males less than 'males_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
