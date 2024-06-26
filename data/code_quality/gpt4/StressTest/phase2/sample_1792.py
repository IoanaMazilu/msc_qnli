class_size_premise = 42
class_size_hypothesis = 12

# the hypothesis talks about the size of Jill's class, referenced also in the premise
if class_size_hypothesis >= class_size_premise:
    # check if the hypothesis value contradicts the estimate of less than 'class_size_premise'
    label = "contradiction"
elif class_size_hypothesis < class_size_premise:
    # any class size less than 'class_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
