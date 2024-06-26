people_killed_premise = 52
bombers_premise = 4
people_killed_hypothesis = 52
bombers_hypothesis = 4

# the hypothesis talks about the number of people and bombers killed on a certain day, which is also mentioned in the premise
if people_killed_hypothesis!= people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed from the premise
    label = "contradiction"
elif bombers_hypothesis!= bombers_premise:
    # check if the number of bombers in the hypothesis contradicts the number of bombers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
