leo_weight_premise = 0
leo_weight_hypothesis = 10
kendra_weight_premise = 0
kendra_weight_hypothesis = 0

# the hypothesis talks about the weight of Leo and Kendra, referenced also in the premise
if leo_weight_hypothesis <= leo_weight_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leo_weight_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of Leo
    # any weight greater than 'leo_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

if kendra_weight_hypothesis!= kendra_weight_premise:
    # check if the estimate of Kendra's weight in the hypothesis contradicts the estimate of Kendra's weight in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of Kendra
    # any weight greater than 'kendra_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
