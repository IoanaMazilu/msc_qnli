class_size_premise = 59
class_size_hypothesis = 19

# the hypothesis refers to the number of members in the class, which is also mentioned in the premise
if class_size_hypothesis <= class_size_premise:
    # check if the estimate of 'class_size_hypothesis' contradicts the number of members in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members in the class
    # any number of members greater than 'class_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
