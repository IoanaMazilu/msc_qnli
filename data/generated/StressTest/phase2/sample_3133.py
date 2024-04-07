# Premise: Jill is dividing her less than 44-person class into two teams of equal size for a basketball game.
# Hypothesis: Jill is dividing her 14-person class into two teams of equal size for a basketball game.
# Golden Label: neutral

class_size_premise = 44
class_size_hypothesis = 14

# the hypothesis talks about the size of Jill's class, which is also mentioned in the premise
if class_size_hypothesis >= class_size_premise:
    # check if the hypothesis value contradicts the estimate of less than 'class_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the class
    # any size less than 'class_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

