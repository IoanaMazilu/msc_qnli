# Premise: Jill is dividing her 14-person class into two teams of equal size for a basketball game.
# Hypothesis: Jill is dividing her less than 44-person class into two teams of equal size for a basketball game.
# Golden Label: entailment

class_size_premise = 14
class_size_hypothesis = 44

# the hypothesis refers to the size of the class mentioned in the premise
if class_size_premise >= class_size_hypothesis:
    # check if the class size in the premise contradicts the estimate of less than 'class_size_hypothesis'
    label = "contradiction"
else:
    # if the class size in the premise is less than 'class_size_hypothesis', we can infer entailment
    label = "entailment"

print(label)

