premise_trip_home = 1/2
premise_trip_beach = 1
hypothesis_trip_home = 4/2
hypothesis_trip_beach = 1

# the hypothesis refers to the number of kilometers driven each way
if hypothesis_trip_home <= premise_trip_home:
    # check if the estimate of 'hypothesis_trip_home' contradicts the number of kilometers driven each way in the premise
    label = "contradiction"
elif hypothesis_trip_beach!= premise_trip_beach:
    # check if the number of kilometers driven each way in the hypothesis contradicts the number of kilometers driven each way reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
