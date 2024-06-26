tool_rental_premise = 160
tool_rental_hypothesis = 360

# the hypothesis talks about the total cost of renting a tool, referenced also in the premise
if tool_rental_hypothesis <= tool_rental_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tool_rental_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total cost of renting the tool
    # any total cost greater than 'tool_rental_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
