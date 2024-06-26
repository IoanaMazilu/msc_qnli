peacekeepers_premise = 11800
peacekeepers_hypothesis = 11800

# the hypothesis mentions the number of peacekeepers approved by the council, which is also mentioned in the premise
if peacekeepers_hypothesis!= peacekeepers_premise:
    # check if the number of peacekeepers in the hypothesis contradicts the number of peacekeepers in the premise
    label = "contradiction"
else:
    # if the number of peacekeepers in the hypothesis matches the number of peacekeepers in the premise, we can infer entailment
    label = "entailment"

print(label)