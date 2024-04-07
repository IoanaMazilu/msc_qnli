# Premise: Jill is dividing her 16-person class into two teams of equal size for a basketball game.
# Hypothesis: Jill is dividing her 66-person class into two teams of equal size for a basketball game.
# Golden Label: contradiction

class_size_premise = 16
class_size_hypothesis = 66

# the hypothesis refers to the size of the class mentioned in the premise
if class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

