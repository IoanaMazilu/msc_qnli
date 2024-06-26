premise_salary = 75000
hypothesis_salary = 45000
premise_commission = 0.35
hypothesis_commission = 0.15

# the hypothesis mentions a sales job with a lower salary and a higher commission
if hypothesis_salary < premise_salary:
    # check if the hypothesis value contradicts the premise value for the salary
    label = "contradiction"
elif hypothesis_commission > premise_commission:
    # check if the hypothesis value contradicts the premise value for the commission
    label = "contradiction"
else:
    # the premise gives an estimate for the salary and commission, but the hypothesis provides more specific information
    # any salary and commission combination that is consistent with the premise is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
