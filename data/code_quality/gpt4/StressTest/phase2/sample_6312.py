males_premise = 4
males_hypothesis = 2
females_premise = 3
females_hypothesis = 3

# the hypothesis talks about the number of males and females that can sit around a table, referenced also in the premise
if males_hypothesis >= males_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif females_premise != females_hypothesis:
    # check if the number of females in the hypothesis contradicts the number of females reported in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of males and females
    # any number of males greater than 'males_hypothesis' and any number of females equal to 'females_hypothesis' is consistent with the premise, 
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
