people_class_premise = 100
people_class_hypothesis = 100

# the hypothesis refers to the number of people in the class, referenced also in the premise
if people_class_hypothesis!= people_class_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the class
    # any number of people in the class greater than 'people_class_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
