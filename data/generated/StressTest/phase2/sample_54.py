# Premise: Speed of Bruce is 30 m/s and that of Bhishma is 20 m/s.
# Hypothesis: Speed of Bruce is less than 60 m/s and that of Bhishma is 20 m/s.
# Golden Label: entailment

bruce_speed_premise = 30
bhishma_speed_premise = 20
bruce_speed_hypothesis = 60
bhishma_speed_hypothesis = 20

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if bruce_speed_premise >= bruce_speed_hypothesis:
    # check if the estimate of 'bruce_speed_hypothesis' contradicts the speed of Bruce in the premise
    label = "contradiction"
elif bhishma_speed_hypothesis != bhishma_speed_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

