premise_wage = 6.00
premise_tip_rate = 0.75
hypothesis_wage = 6.00
hypothesis_tip_rate = 0.35

# the hypothesis talks about the hourly wage and tip rate of Jill, referenced in the premise
if hypothesis_wage!= premise_wage:
    # check if the hypothesis value contradicts the premise value for the hourly wage
    label = "contradiction"
elif hypothesis_tip_rate <= premise_tip_rate:
    # check if the hypothesis value contradicts the premise value for the tip rate
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage and tip rate
    # any combination of hourly wage and tip rate greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
