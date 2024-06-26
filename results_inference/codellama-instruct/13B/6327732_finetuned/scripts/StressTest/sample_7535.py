# define variables for the numerical entities in the premise and hypothesis
leo_gain_premise = 10
leo_gain_hypothesis = 80
kendra_weight_premise = 50
kendra_weight_hypothesis = 50

# the hypothesis refers to the number of pounds Leo gains and the weight of his sister Kendra
if leo_gain_hypothesis <= leo_gain_premise:
    # check if the estimate of 'leo_gain_hypothesis' contradicts the number of pounds gained in the premise
    label = "contradiction"
elif kendra_weight_hypothesis!= kendra_weight_premise:
    # check if the weight of Kendra in the hypothesis contradicts the weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
