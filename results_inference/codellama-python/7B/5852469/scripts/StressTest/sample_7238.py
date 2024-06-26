people_class_premise = 20
people_class_hypothesis = 20

# the hypothesis and the premise refer to the same number of people
if people_class_hypothesis!= people_class_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of people in the class
    # any number of people in the class is consistent with the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
