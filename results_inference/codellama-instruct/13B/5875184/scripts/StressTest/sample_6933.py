premise_salary = 75000
hypothesis_salary = 45000
premise_commission = 15
hypothesis_commission = 45

# the hypothesis refers to the salary and commission mentioned in the premise
if hypothesis_salary <= premise_salary:
    # check if the estimate of 'hypothesis_salary' contradicts the salary in the premise
    label = "contradiction"
elif hypothesis_commission >= premise_commission:
    # check if the estimate of 'hypothesis_commission' contradicts the commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)