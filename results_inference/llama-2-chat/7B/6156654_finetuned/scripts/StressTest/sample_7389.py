rosy_efficiency_premise = 0.10
mary_efficiency_premise = 0.10
rosy_efficiency_hypothesis = 0.30
mary_efficiency_hypothesis = 0.10

# the hypothesis refers to the efficiency of Rosy and Mary, as mentioned in the premise
if rosy_efficiency_hypothesis <= rosy_efficiency_premise:
    # check if the hypothesis value contradicts the premise value of Rosy's efficiency
    label = "contradiction"
elif mary_efficiency_hypothesis!= mary_efficiency_premise:
    # check if the efficiency of Mary in the hypothesis contradicts the efficiency of Mary in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
