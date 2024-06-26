rescued_people_premise = 23
rescued_people_hypothesis = 23

# the hypothesis mentions the number of people rescued, which is also mentioned in the premise
if rescued_people_hypothesis != rescued_people_premise:
    # check if the number of rescued people in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the number of rescued people in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
