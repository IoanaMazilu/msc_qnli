ranks_premise = 65
ranks_hypothesis = 25
class_size_premise = 182

# the hypothesis talks about Veena's rank in a class of 182 students
if ranks_hypothesis <= ranks_premise:
    # check if the hypothesis value contradicts the estimate of 'ranks_premise'
    label = "contradiction"
elif ranks_hypothesis > ranks_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for Veena's rank
    # any rank value greater than 'ranks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
