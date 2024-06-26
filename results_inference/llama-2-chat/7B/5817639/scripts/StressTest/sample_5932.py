herd_parts_premise = 4
herd_parts_hypothesis = 5

# the hypothesis talks about the number of equal parts Antony can divide his herd into, referenced also in the premise
if herd_parts_hypothesis <= herd_parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'herd_parts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of equal parts Antony can divide his herd into
    # any number of equal parts greater than 'herd_parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
