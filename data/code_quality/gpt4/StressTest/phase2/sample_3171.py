arjun_speed_premise = 30
bhishma_speed_premise = 20
arjun_speed_hypothesis = 40
bhishma_speed_hypothesis = 20

# the hypothesis talks about the speed of Arjun and Bhishma, which are also mentioned in the premise
if arjun_speed_hypothesis < arjun_speed_premise:
    # check if the hypothesis value for Arjun's speed contradicts the one in the premise
    label = "contradiction"
elif bhishma_speed_hypothesis != bhishma_speed_premise:
    # check if the hypothesis value for Bhishma's speed contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
