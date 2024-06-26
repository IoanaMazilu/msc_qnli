buses_premise = 2
people_premise = 80
buses_hypothesis = 2

# the hypothesis mentions the number of buses that skidded off the road, which is also mentioned in the premise
# however, the hypothesis does not refer to the number of people involved in the incident, which is provided in the premise
if buses_hypothesis != buses_premise:
    # check if the number of buses in the hypothesis contradicts the number of buses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values but does not mention all the details, we can infer neutrality
    label = "neutral"

print(label)
