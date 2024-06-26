premise_wage = 6.00
premise_tip_rate = 0.75
hypothesis_wage = 6.00
hypothesis_tip_rate = 0.35

# the hypothesis talks about the wage and tip rate of Jill, referenced also in the premise
if hypothesis_wage!= premise_wage:
    # check if the hypothesis value contradicts the estimate of $6.00 per hour
    label = "contradiction"
elif hypothesis_tip_rate!= premise_tip_rate:
    # check if the tip rate in the hypothesis contradicts the standard tip rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
