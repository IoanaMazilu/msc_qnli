herd_parts_premise = 5
herd_parts_hypothesis = 5

# the hypothesis talks about the number of equal parts Antony can divide his herd into, which is also referenced in the premise
if herd_parts_hypothesis >= herd_parts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'herd_parts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parts
    # any number of parts less than 'herd_parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
