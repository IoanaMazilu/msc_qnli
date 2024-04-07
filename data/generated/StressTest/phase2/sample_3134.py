# Premise: Jill is dividing her 14-person class into two teams of equal size for a basketball game.
# Hypothesis: Jill is dividing her less than 14-person class into two teams of equal size for a basketball game.
# Golden Label: contradiction

class_size_premise = 14
class_size_hypothesis = 14

# The hypothesis refers to the size of Jill's class mentioned in the premise
if class_size_hypothesis < class_size_premise:
    # Check if the hypothesis value contradicts the class size in the premise
    label = "contradiction"
elif class_size_hypothesis == class_size_premise:
    # If the hypothesis value does not contradict the class size in the premise, we can infer entailment
    label = "entailment"
else:
    # Any other case is considered neutral
    label = "neutral"

print(label)

