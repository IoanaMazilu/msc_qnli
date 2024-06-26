rental_premise = 160
rental_hypothesis = 760

# the hypothesis refers to the total amount paid for renting the tool, referenced also in the premise
if rental_hypothesis <= rental_premise:
    # check if the hypothesis value contradicts the estimate of more than'rental_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total amount paid for renting the tool
    # any amount greater than'rental_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
