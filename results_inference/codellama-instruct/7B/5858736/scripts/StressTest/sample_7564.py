jill_wage_premise = 8.00
jill_wage_hypothesis = 8.00
jill_tip_premise = 0.70
jill_tip_hypothesis = 0.30

# the hypothesis talks about the hourly wage and standard tip rate of Jill, referenced also in the premise
if jill_wage_hypothesis!= jill_wage_premise:
    # check if the hypothesis value contradicts the estimate of $8.00 per hour
    label = "contradiction"
elif jill_tip_hypothesis!= jill_tip_premise:
    # check if the standard tip rate in the hypothesis contradicts the estimate of less than 70% of the cost of the orders she serves
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
