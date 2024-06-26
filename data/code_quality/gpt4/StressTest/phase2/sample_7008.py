males_premise = 25
males_hypothesis = 45

# the hypothesis refers to the number of males, also mentioned in the premise
if males_hypothesis <= males_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif males_premise >= males_hypothesis:
    # check if the premise value contradicts the hypothesis
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males less than 'males_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
