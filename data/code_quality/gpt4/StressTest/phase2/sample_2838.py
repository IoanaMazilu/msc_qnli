class_size_premise = 16
class_size_hypothesis = 66

# the hypothesis talks about the size of Jill's class, referenced also in the premise
if class_size_hypothesis < class_size_premise:
    # check if the hypothesis value contradicts the precise class size given in the premise
    label = "contradiction"
else:
    # the hypothesis value is greater than the premise one
    # it doesn't contradict the premise but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
