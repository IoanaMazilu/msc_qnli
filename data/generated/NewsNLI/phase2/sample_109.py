# Premise: At least 48 people were killed during the riots that broke out in Madagascar.
# Hypothesis: At least 48 people die in the violence in Madagascar, official says.
# Golden Label: entailment

people_killed_premise = 48
people_killed_hypothesis = 48

# the hypothesis mentions the number of people that died in Madagascar, which is also mentioned in the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of people that died in the hypothesis contradicts the number of people that died in the premise
    label = "contradiction"
else:
    # if the number of people that died in the hypothesis does not contradict the number of people that died in the premise, we can infer entailment
    label = "entailment"

print(label)

