peacekeepers_approved_premise = 11800
peacekeepers_approved_hypothesis = 11800

# the hypothesis mentions the number of peacekeepers approved by the council, which is also mentioned in the premise
if peacekeepers_approved_hypothesis!= peacekeepers_approved_premise:
    # check if the number of peacekeepers approved in the hypothesis contradicts the number approved in the premise
    label = "contradiction"
else:
    # if the number of peacekeepers approved in the hypothesis matches the number approved in the premise, we can infer entailment
    label = "entailment"

print(label)