leo_weight_increase_premise = 10
leo_weight_increase_hypothesis = 50

# the hypothesis talks about the weight increase of Leo, referenced also in the premise
if leo_weight_increase_hypothesis >= leo_weight_increase_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leo_weight_increase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight increase
    # any weight increase less than 'leo_weight_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
