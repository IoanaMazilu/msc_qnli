debentures_premise = 50000
debentures_hypothesis = 80000

# the hypothesis refers to the amount of debentures bought by Jaclyn, mentioned in the premise
if debentures_premise >= debentures_hypothesis:
    # check if the premise value contradicts the estimate of 'less than debentures_hypothesis'
    label = "contradiction"
elif debentures_premise != debentures_hypothesis:
    # check if the number of debentures in the premise contradicts the number of debentures in the hypothesis
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
