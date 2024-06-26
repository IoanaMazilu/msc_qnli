home_to_beach_premise = 80
home_to_beach_hypothesis = 60
beach_to_home_premise = 70
beach_to_home_hypothesis = 70

# the hypothesis refers to the average speed of the trips
if home_to_beach_hypothesis <= home_to_beach_premise:
    # check if the estimate of 'home_to_beach_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
elif beach_to_home_hypothesis!= beach_to_home_premise:
    # check if the speed of the return trip in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
