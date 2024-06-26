car_percentage_premise = 0.18
car_percentage_hypothesis = 0.48

# the hypothesis refers to the percentage of students with cars, mentioned in the premise
if car_percentage_hypothesis <= car_percentage_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific percentage of students with cars
    # any percentage less than 'car_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
