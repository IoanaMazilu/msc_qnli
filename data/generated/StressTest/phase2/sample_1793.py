# Premise: Jill is dividing her 12-person class into two teams of equal size for a basketball game.
# Hypothesis: Jill is dividing her 62-person class into two teams of equal size for a basketball game.
# Golden Label: contradiction

class_size_premise = 12
class_size_hypothesis = 62

# the hypothesis talks about the size of the class Jill is dividing, referenced also in the premise
if class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

