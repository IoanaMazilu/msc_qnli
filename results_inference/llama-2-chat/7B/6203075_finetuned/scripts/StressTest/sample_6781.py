# The premise and hypothesis are both describing the pay rate for Harry
pay_rate_premise = 1
pay_rate_hypothesis = 1

# The premise talks about the pay rate for the first less than 80 hours,
# the hypothesis talks about the pay rate for the first 30 hours
if pay_rate_premise > pay_rate_hypothesis:
    # check if the pay rate in the hypothesis contradicts the pay rate in the premise
    label = "contradiction"
elif pay_rate_hypothesis > pay_rate_premise:
    # check if the pay rate in the hypothesis contradicts the pay rate in the premise
    label = "contradiction"
else:
    # if the pay rate in the hypothesis does not contradict the pay rate in the premise, we can infer entailment
    label = "entailment"

print(label)
