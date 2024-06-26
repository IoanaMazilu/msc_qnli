firing_premise = 6
firing_hypothesis = 6
suspending_premise = 14
suspending_hypothesis = 14

# the hypothesis mentions the number of TSA screeners being fired and suspended, which are also mentioned in the premise
if firing_hypothesis != firing_premise:
    # check if the number of firings in the hypothesis contradicts the number of firings reported in the premise
    label = "contradiction"
elif suspending_hypothesis != suspending_premise:
    # check if the number of suspensions from the hypothesis contradicts the number of suspensions in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
