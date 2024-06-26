y_premise = 3
y_hypothesis = 4

distance_premise = 3
distance_hypothesis = 4

time_premise = 1.5
time_hypothesis = 1.5

rate_premise = distance_premise / time_premise
rate_hypothesis = distance_hypothesis / time_hypothesis

# the hypothesis talks about the distance Jack walked and the time he walked it in
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of walking in the hypothesis contradicts the rate of walking in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
