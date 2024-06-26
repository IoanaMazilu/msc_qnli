peacekeepers_premise = 11800
peacekeepers_hypothesis = 11800

# the hypothesis mentions the deployment of 11,800 peacekeepers to the country, which is also mentioned in the premise
if peacekeepers_hypothesis!= peacekeepers_premise:
    # check if the number of peacekeepers in the hypothesis contradicts the number of peacekeepers reported in the premise
    label = "contradiction"
else:
    # if the number of peacekeepers in the hypothesis does not contradict the number of peacekeepers in the premise, we can infer entailment
    label = "entailment"

print(label)
