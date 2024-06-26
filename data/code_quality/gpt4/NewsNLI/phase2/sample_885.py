people_killed_premise = 23
people_killed_hypothesis = 23

# the hypothesis references the number of people killed, which is also mentioned in the premise
# however, the hypothesis introduces a new location (Rawalpindi) that is not mentioned in the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
else:
    # if the number of people killed in the hypothesis does not contradict the number in the premise, we infer neutrality
    label = "neutral"

print(label)
