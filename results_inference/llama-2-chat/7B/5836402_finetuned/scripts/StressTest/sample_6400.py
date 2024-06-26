miami_passengers_premise = 8/2
miami_passengers_hypothesis = 1/2
logan_passengers_premise = 4
logan_passengers_hypothesis = 4

# the hypothesis refers to the number of passengers from Miami Airport and the relationship with the number of passengers from Kennedy Airport and Logan Airport mentioned in the premise
if miami_passengers_hypothesis!= miami_passengers_premise:
    # check if the number of passengers from Miami Airport in the hypothesis contradicts the number of passengers from Miami Airport in the premise
    label = "contradiction"
elif logan_passengers_hypothesis!= logan_passengers_premise:
    # check if the number of passengers from Logan Airport in the hypothesis contradicts the number of passengers from Logan Airport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
