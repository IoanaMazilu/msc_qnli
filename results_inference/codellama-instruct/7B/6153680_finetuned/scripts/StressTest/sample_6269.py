death_rate_premise = 10
death_rate_hypothesis = 10
fear_rate_premise = 20
fear_rate_hypothesis = 20

# the hypothesis refers to the same situation as the premise
if death_rate_hypothesis > death_rate_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif death_rate_hypothesis == death_rate_premise and fear_rate_hypothesis == fear_rate_premise:
    # check if the hypothesis is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise but are not consistent either, we infer neutrality
    label = "neutral"

print(label)
