# Premise: Veena ranks 65 rd from the top in a class of 182.
# Hypothesis: Veena ranks more than 15 rd from the top in a class of 182.
# Golden Label: entailment

veena_rank_premise = 65
veena_rank_hypothesis = 15
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis refers to Veena's rank and the class size mentioned in the premise
if veena_rank_hypothesis >= veena_rank_premise:
    # check if the hypothesis value contradicts Veena's rank in the premise
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

