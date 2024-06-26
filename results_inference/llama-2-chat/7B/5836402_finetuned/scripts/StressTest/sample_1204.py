home_to_beach_speed_premise = 40
home_to_beach_speed_hypothesis = 80
beach_to_home_speed_premise = 70
beach_to_home_speed_hypothesis = 70

# the hypothesis refers to the average speed of Carl's trip from home to the beach and back
if home_to_beach_speed_premise <= home_to_beach_speed_hypothesis:
    # check if the estimate of 'home_to_beach_speed_hypothesis' contradicts the average speed from home to the beach in the premise
    label = "contradiction"
elif beach_to_home_speed_hypothesis!= beach_to_home_speed_premise:
    # check if the average speed from the beach to home in the hypothesis contradicts the average speed from the beach to home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
