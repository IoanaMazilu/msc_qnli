parts_premise = 4
parts_hypothesis = 5

# the hypothesis talks about the number of parts Antony can divide his herd into, referenced also in the premise
if parts_hypothesis <= parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'parts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parts
    # any number of parts greater than 'parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
