# Premise: Jill is dividing her less than 66-person class into two teams of equal size for a basketball game.
# Hypothesis: Jill is dividing her 16-person class into two teams of equal size for a basketball game.
# Golden Label: neutral

class_size_premise = 66
class_size_hypothesis = 16

# the hypothesis refers to the size of Jill's class mentioned in the premise
if class_size_hypothesis >= class_size_premise:
    # check if the class size in the hypothesis contradicts the estimate of less than 'class_size_premise' in the premise
    label = "contradiction"
elif class_size_hypothesis < class_size_premise:
    # the premise provides only an estimate for the class size, any class size less than 'class_size_premise' is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

