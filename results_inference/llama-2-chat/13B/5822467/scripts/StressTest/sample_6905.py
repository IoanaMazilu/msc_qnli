tool_rental_premise = 160
tool_rental_hypothesis = 760

# the hypothesis talks about the total amount paid to rent the tool, referenced also in the premise
if tool_rental_hypothesis <= tool_rental_premise:
    # check if the hypothesis value contradicts the estimate of less than $160
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount paid
    # any amount greater than $160 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
