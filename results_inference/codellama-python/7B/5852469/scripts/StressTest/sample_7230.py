people_class_premise = 100
people_class_hypothesis = 100

# the hypothesis refers to the number of people in the class
if people_class_hypothesis!= people_class_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of people in the class
    # any number of people in the class other than the one in the premise is inconsistent with the premise
    # any number of people in the class equal to the one in the premise is consistent with the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
