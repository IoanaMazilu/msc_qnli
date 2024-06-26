tool_rental_premise = 160
tool_rental_hypothesis = 760

# the hypothesis refers to the total amount paid to rent the tool, mentioned in the premise
if tool_rental_hypothesis <= tool_rental_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tool_rental_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount paid to rent the tool
    # any amount greater than 'tool_rental_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
