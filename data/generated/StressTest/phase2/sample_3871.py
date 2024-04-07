# Premise: Veena ranks less than 83 rd from the top in a class of 182.
# Hypothesis: Veena ranks 73 rd from the top in a class of 182.
# Golden Label: neutral

veena_rank_premise = 83
veena_rank_hypothesis = 73
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis refers to Veena's rank and the class size, both also mentioned in the premise
if class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size in the premise
    label = "contradiction"
elif veena_rank_hypothesis >= veena_rank_premise:
    # check if Veena's rank in the hypothesis contradicts the estimate of less than 'veena_rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Veena's rank
    # a rank less than 'veena_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

