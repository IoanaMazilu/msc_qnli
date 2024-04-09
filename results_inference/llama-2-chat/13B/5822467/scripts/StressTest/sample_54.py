bruce_speed_premise = 30
bhishma_speed_premise = 20
bruce_speed_hypothesis = 60

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if bruce_speed_premise <= bruce_speed_hypothesis and bhishma_speed_premise == bhishma_speed_hypothesis:
    # check if the estimate of 'bruce_speed_hypothesis' and 'bhishma_speed_hypothesis' do not contradict the premise
    label = "entailment"
elif bruce_speed_hypothesis < bhishma_speed_premise:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
