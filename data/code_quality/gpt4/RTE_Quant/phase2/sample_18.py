people_killed_premise = 70000
people_killed_hypothesis = 200000

# the hypothesis talks about the number of people killed in the Darfur region, which is also mentioned in the premise
if people_killed_hypothesis > people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
