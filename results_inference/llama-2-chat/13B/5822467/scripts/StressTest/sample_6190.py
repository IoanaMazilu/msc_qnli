vacation_days_premise = 80
vacation_days_hypothesis = 30

# the hypothesis refers to the number of days Lexi needed to save for the vacation
if vacation_days_hypothesis <= vacation_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'vacation_days_premise'
    label = "contradiction"
elif vacation_days_hypothesis > vacation_days_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number of days needed for the vacation
    # any number of days needed less than or equal to 'vacation_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
