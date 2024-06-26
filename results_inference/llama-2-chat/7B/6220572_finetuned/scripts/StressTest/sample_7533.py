leo_weight_gain_premise = 10
leo_weight_gain_hypothesis = 50
kendra_weight_premise = 50
kendra_weight_hypothesis = 50

# the hypothesis talks about the weight gain of Leo, referenced also in the premise
if leo_weight_gain_hypothesis >= leo_weight_gain_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leo_weight_gain_premise'
    label = "contradiction"
elif kendra_weight_hypothesis!= kendra_weight_premise:
    # check if the weight of Kendra in the hypothesis contradicts the weight of Kendra reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
