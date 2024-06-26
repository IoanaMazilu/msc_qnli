premise_salary = 75000
hypothesis_salary = 45000
premise_commission = 0.45
hypothesis_commission = 0.15

# the hypothesis refers to the salary and commission mentioned in the premise
if hypothesis_salary <= premise_salary:
    # check if the hypothesis value contradicts the premise value for salary
    label = "contradiction"
elif hypothesis_commission >= premise_commission:
    # check if the hypothesis value contradicts the premise value for commission
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
