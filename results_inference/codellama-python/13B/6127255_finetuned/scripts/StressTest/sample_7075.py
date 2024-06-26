rank_premise = 15
rank_hypothesis = 65
class_size = 182

# the hypothesis talks about Veena's rank in the class, referenced also in the premise
if rank_hypothesis <= rank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's rank
    # any rank greater than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
