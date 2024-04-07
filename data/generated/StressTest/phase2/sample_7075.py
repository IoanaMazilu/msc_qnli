# Premise: Veena ranks more than 15 rd from the top in a class of 182.
# Hypothesis: Veena ranks 65 rd from the top in a class of 182.
# Golden Label: neutral

veena_rank_premise = 15
veena_rank_hypothesis = 65
class_size = 182

# the hypothesis talks about Veena's rank in the class, referenced also in the premise
if veena_rank_hypothesis <= veena_rank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'veena_rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's rank
    # any rank greater than 'veena_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

