people_killed_premise = 52
bombers_killed_premise = 4
people_killed_hypothesis = 52
bombers_killed_hypothesis = 4

# the hypothesis talks about the number of people and bombers killed on July 7, which is also mentioned in the premise
if people_killed_hypothesis!= people_killed_premise or bombers_killed_hypothesis!= bombers_killed_premise:
    # check if the number of people and bombers killed on July 7 in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
