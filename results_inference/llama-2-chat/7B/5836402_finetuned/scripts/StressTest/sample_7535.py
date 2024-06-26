leo_weight_increase_premise = 10
leo_weight_increase_hypothesis = 80

# the hypothesis talks about the weight increase of Leo, referenced also in the premise
if leo_weight_increase_hypothesis <= leo_weight_increase_premise:
    # check if the hypothesis value contradicts the estimate of 'leo_weight_increase_premise'
    label = "contradiction"
elif leo_weight_increase_hypothesis > leo_weight_increase_premise:
    # check if the weight increase in the hypothesis exceeds the weight increase in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
