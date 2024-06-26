premise_wage = 8.00
premise_tip_rate = 0.30

hypothesis_wage = 8.00
hypothesis_tip_rate = 0.30

# the hypothesis talks about the wage and tip rate of Jill, referenced also in the premise
if hypothesis_wage <= premise_wage:
    # check if the hypothesis value contradicts the estimate of 'premise_wage'
    label = "contradiction"
elif hypothesis_tip_rate >= premise_tip_rate:
    # check if the hypothesis value contradicts the estimate of 'premise_tip_rate'
    label = "contradiction"
else:
    # the premise gives only an estimate for the wage and tip rate of Jill
    # any number of wage and tip rate greater than 'premise_wage' and less than 'premise_tip_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
