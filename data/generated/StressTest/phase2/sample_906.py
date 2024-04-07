# Premise: If the three started to fish together and after 40 minutes Mike and Bob left, how many fish did the three fishermen catch in one hour?
# Hypothesis: If the three started to fish together and after more than 20 minutes Mike and Bob left, how many fish did the three fishermen catch in one hour?
# Golden Label: entailment

fishing_time_premise = 40
fishing_time_hypothesis = 20

# the hypothesis refers to the fishing time mentioned in the premise
if fishing_time_premise < fishing_time_hypothesis:
    # check if the estimated 'fishing_time_hypothesis' contradicts the fishing time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

