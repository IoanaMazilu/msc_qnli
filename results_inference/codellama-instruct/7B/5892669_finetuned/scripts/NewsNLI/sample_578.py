peacekeepers_premise = 11800
peacekeepers_hypothesis = 11800

# the hypothesis mentions the number of peacekeepers deployed, which is also referenced in the premise
if peacekeepers_hypothesis!= peacekeepers_premise:
    # check if the number of peacekeepers in the hypothesis contradicts the number of peacekeepers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
