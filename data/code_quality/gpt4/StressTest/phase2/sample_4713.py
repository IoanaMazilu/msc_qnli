debentures_premise = 30000
debentures_hypothesis = 40000

# the hypothesis refers to the amount of debentures Jaclyn bought, which is also mentioned in the premise
if debentures_premise >= debentures_hypothesis:
    # check if the premise value contradicts the 'less than debentures_hypothesis' condition
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis condition, we can infer entailment
    label = "entailment"

print(label)
