people_killed_premise = 52
people_killed_hypothesis = 52
bombers_killed_premise = 4
bombers_killed_hypothesis = 4

# the hypothesis mentions the number of people and bombers killed, which are also mentioned in the premise
if people_killed_hypothesis!= people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
elif bombers_killed_hypothesis!= bombers_killed_premise:
    # check if the number of bombers killed in the hypothesis contradicts the number of bombers killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
