class_size_premise = 59
class_size_hypothesis = 19

# the hypothesis refers to the number of class members, also mentioned in the premise
if class_size_premise <= class_size_hypothesis:
    # check if the estimate of 'class_size_hypothesis' contradicts the number of class members in the premise
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the number of class members in the hypothesis contradicts the number of class members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
