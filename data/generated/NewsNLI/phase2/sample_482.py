# Premise: Overland Park, Kansas (CNN) -- The man accused of killing three people at two Jewish-affiliated facilities in Kansas made no secret of his racist views, writing letters to newspapers and inviting people to white-supremacist meetings at his home, say those who knew him.
# Hypothesis: Cross is accused of killing three people at two Jewish-affiliated facilities.
# Golden Label: neutral

people_killed_premise = 3
people_killed_hypothesis = 3

# the hypothesis mentions the number of people killed at the Jewish-affiliated facilities, which is also mentioned in the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed reported in the premise
    label = "contradiction"
else:
    # if the number of people killed in the hypothesis does not contradict the number of people killed in the premise, we can infer entailment
    label = "entailment"

print(label)

