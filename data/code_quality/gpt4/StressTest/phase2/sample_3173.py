speed_arjun_premise = 30
speed_arjun_hypothesis = 30
speed_bhishma_premise = 20
speed_bhishma_hypothesis = 20

# the hypothesis refers to the speeds of Arjun and Bhishma mentioned in the premise
if speed_arjun_premise >= speed_arjun_hypothesis:
    # check if the speed of Arjun in the hypothesis contradicts the speed of Arjun in the premise
    label = "contradiction"
elif speed_bhishma_hypothesis != speed_bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
