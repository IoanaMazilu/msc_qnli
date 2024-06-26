miami_passengers_premise = 1/2
miami_passengers_hypothesis = 3/2
logan_passengers_premise = 4
logan_passengers_hypothesis = 4

# the hypothesis refers to the number of passengers in the premise
if miami_passengers_hypothesis!= miami_passengers_premise:
    # check if the number of Miami passengers in the hypothesis contradicts the number of Miami passengers in the premise
    label = "contradiction"
elif logan_passengers_hypothesis!= logan_passengers_premise:
    # check if the number of Logan passengers in the hypothesis contradicts the number of Logan passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
