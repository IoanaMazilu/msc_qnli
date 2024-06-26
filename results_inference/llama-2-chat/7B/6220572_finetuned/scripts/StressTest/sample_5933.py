parts_premise = 5
parts_hypothesis = 5

# the hypothesis talks about the number of equal parts Antony can divide his herd into, referenced also in the premise
if parts_hypothesis <= parts_premise:
    # check if the hypothesis value contradicts the number of parts in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of parts
    # any number of parts less than 'parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
