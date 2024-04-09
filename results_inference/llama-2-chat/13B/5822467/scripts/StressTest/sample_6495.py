mumbai_to_pune_premise = 44
mumbai_to_pune_hypothesis = 24
average_speed_premise = 50

# the hypothesis refers to the time taken to reach Pune and the average speed
if mumbai_to_pune_hypothesis > mumbai_to_pune_premise:
    # check if the hypothesis time is greater than the premise time, which is contradictory
    label = "contradiction"
elif average_speed_premise!= average_speed_hypothesis:
    # check if the average speed in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
