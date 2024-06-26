veena_rank_premise = 43
veena_rank_hypothesis = 73
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis talks about Veena's rank and class size, both referenced in the premise
if veena_rank_hypothesis <= veena_rank_premise:
    # check if the hypothesis rank contradicts the estimate of more than 'veena_rank_premise'
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's rank
    # any rank greater than 'veena_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
