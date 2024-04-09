males_premise = 25
less_than_45_males_hypothesis = True

# the hypothesis refers to the number of males altogether, which is mentioned in the premise
if males_premise <= less_than_45_males_hypothesis:
    # check if the hypothesis value contradicts the number of males in the premise
    label = "contradiction"
elif less_than_45_males_hypothesis:
    # check if the hypothesis value is consistent with the estimate of'males_premise'
    label = "neutral"
else:
    # the premise gives only an estimate for the number of males
    # any number of males less than'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
