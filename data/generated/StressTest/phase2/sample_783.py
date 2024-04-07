# Premise: Veena ranks 44 rd from the top in a class of 182.
# Hypothesis: Veena ranks less than 84 rd from the top in a class of 182.
# Golden Label: entailment

veena_rank_premise = 44
veena_rank_hypothesis = 84
class_size_premise = 182
class_size_hypothesis = 182

# the hypothesis refers to Veena's rank and the class size mentioned in the premise
if veena_rank_premise > veena_rank_hypothesis:
    # check if Veena's rank from the hypothesis contradicts her rank in the premise
    label = "contradiction"
elif class_size_premise != class_size_hypothesis:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

