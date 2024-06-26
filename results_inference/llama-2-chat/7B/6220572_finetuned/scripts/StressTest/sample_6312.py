males_females_premise = 4
males_females_hypothesis = 2

# the hypothesis refers to the number of males and females in the premise
if males_females_hypothesis <= males_females_premise:
    # check if the hypothesis value contradicts the number of males and females in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males and females
    # any number of males and females greater than'males_females_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
