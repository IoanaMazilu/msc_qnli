rent_paid_premise = 88
rent_paid_hypothesis = 38

# the hypothesis talks about the amount Dravid paid for renting the tool, referenced also in the premise
if rent_paid_hypothesis >= rent_paid_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rent_paid_premise'
    label = "contradiction"
elif rent_paid_hypothesis < rent_paid_premise:
    # if the hypothesis value is less than 'rent_paid_premise', it is consistent with the premise
    # but we cannot infer the exact amount from the premise, so it's not an entailment
    label = "neutral"

print(label)
