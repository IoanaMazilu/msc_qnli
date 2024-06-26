people_class_premise = 20
people_class_hypothesis = 20

# the hypothesis refers to the same number of people in the class as the premise
if people_class_hypothesis!= people_class_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the class
    # any number of people greater than 'people_class_premise' is consistent with the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
