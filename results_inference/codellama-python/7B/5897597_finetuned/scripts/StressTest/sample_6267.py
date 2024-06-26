death_rate_premise = 10
death_rate_hypothesis = 30
left_rate_premise = 20
left_rate_hypothesis = 20

# the hypothesis refers to the death and leaving rates mentioned in the premise
if death_rate_premise >= death_rate_hypothesis:
    # check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif left_rate_hypothesis!= left_rate_premise:
    # check if the leaving rate in the hypothesis contradicts the leaving rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
