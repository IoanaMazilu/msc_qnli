tool_rental_premise = 360
tool_rental_hypothesis = 160

# the hypothesis talks about the amount paid to rent a tool, which is also mentioned in the premise
if tool_rental_hypothesis <= tool_rental_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tool_rental_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount paid, but the hypothesis provides a specific value
    # any amount paid greater than 'tool_rental_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
