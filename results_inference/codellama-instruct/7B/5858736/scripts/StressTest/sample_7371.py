premise_wage = 10.00
premise_tip_rate = 0.40
hypothesis_wage = 10.00
hypothesis_tip_rate = 0.80

# the hypothesis talks about the tip rate, referenced also in the premise
if hypothesis_tip_rate <= premise_tip_rate:
    # check if the hypothesis value contradicts the estimate of less than 'premise_tip_rate'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any number of tips greater than 'premise_tip_rate' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
