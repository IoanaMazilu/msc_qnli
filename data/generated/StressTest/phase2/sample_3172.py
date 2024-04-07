# Premise: Speed of Arjun is less than 40 m/s and that of Bhishma is 20 m/s.
# Hypothesis: Speed of Arjun is 30 m/s and that of Bhishma is 20 m/s.
# Golden Label: neutral

speed_arjun_premise = 40
speed_arjun_hypothesis = 30
speed_bhishma_premise = 20
speed_bhishma_hypothesis = 20

# the hypothesis talks about the speed of Arjun and Bhishma, referenced also in the premise
if speed_arjun_hypothesis >= speed_arjun_premise:
    # check if the speed of Arjun in the hypothesis contradicts the estimate of less than 'speed_arjun_premise'
    label = "contradiction"
elif speed_bhishma_hypothesis != speed_bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

