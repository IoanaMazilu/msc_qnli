# Premise: Veena ranks 73 rd from the top in a class of 198.
# Hypothesis: Veena ranks less than 73 rd from the top in a class of 198.
# Golden Label: contradiction

veena_rank_premise = 73
veena_rank_hypothesis = 73
class_size_premise = 198
class_size_hypothesis = 198

# the hypothesis refers to Veena's rank and class size mentioned in the premise
if veena_rank_hypothesis >= veena_rank_premise:
    # check if the hypothesis rank contradicts the rank mentioned in the premise
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
