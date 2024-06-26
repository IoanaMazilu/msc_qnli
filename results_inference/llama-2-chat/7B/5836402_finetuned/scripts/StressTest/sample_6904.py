tool_rent_premise = 360
tool_rent_hypothesis = 160

# the hypothesis refers to the cost of renting the tool mentioned in the premise
if tool_rent_hypothesis <= tool_rent_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tool_rent_premise'
    label = "contradiction"
elif tool_rent_hypothesis > tool_rent_premise:
    # if the hypothesis value is greater than the premise, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the cost of renting the tool
    # any cost less than 'tool_rent_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
