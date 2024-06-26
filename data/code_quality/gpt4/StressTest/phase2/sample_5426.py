distance_travelled_premise = 1/2
distance_travelled_hypothesis = 3/2

# the hypothesis refers to the same car trip and the distance travelled by Maria mentioned in the premise
if distance_travelled_hypothesis > distance_travelled_premise:
    # check if the proportion of the total distance travelled in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # the premise and hypothesis talk about the same distance travelled
    # if the proportion of the total distance travelled in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
