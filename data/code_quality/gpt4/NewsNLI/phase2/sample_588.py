people_killed_premise = 5
people_killed_hypothesis = 5

# the hypothesis mentions the number of people Crawford allegedly killed, which is also mentioned in the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number killed reported in the premise
    label = "contradiction"
else:
    # if the number of people killed in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
