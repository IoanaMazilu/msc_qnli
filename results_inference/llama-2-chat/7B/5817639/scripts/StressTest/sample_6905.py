rent_hours_premise = 160
rent_hours_hypothesis = 760

# the hypothesis talks about the number of hours Rahul rented the tool, referenced also in the premise
if rent_hours_hypothesis <= rent_hours_premise:
    # check if the hypothesis value contradicts the estimate of'rent_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Rahul rented the tool
    # any number of hours greater than'rent_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
