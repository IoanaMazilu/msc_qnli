managers_premise = 3
managers_hypothesis = 3

# the hypothesis mentions the aim of Mourinho and Van Gaal to become the third manager to win the tournament with two teams
# which is also mentioned in the premise
if managers_hypothesis != managers_premise:
    # check if the number of managers in the hypothesis contradicts the number of managers reported in the premise
    label = "contradiction"
else:
    # if the number of managers in the hypothesis does not contradict the number of managers in the premise, we can infer entailment
    label = "entailment"

print(label)
