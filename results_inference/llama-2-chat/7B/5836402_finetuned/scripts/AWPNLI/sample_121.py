distance_premise = 40.0
speed_premise = 8.0
time_hypothesis = 3.0

# the hypothesis talks about the time Heather bicycled, which is not referenced in the premise
# compute the time Heather bicycled from the premise
time_premise = distance_premise / speed_premise
if time_hypothesis!= time_premise:
    # check if the time from the hypothesis contradicts the time estimated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
