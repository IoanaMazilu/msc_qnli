car_percentage_premise = 20
car_percentage_hypothesis = 50

# the hypothesis refers to the percentage of students with cars, mentioned in the premise
if car_percentage_hypothesis >= car_percentage_premise:
    # check if the estimate of 'car_percentage_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # any percentage of students with cars less than 'car_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
