wage_premise = 8.00
wage_hypothesis = 8.00
tip_rate_premise = 70
tip_rate_hypothesis = 30

# the hypothesis talks about the hourly wage and the tip rate of Jill, which are also mentioned in the premise
if wage_hypothesis!= wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hourly wage and the tip rate in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
