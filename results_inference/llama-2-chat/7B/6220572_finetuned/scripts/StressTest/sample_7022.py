car_percentage_premise = 0.20
car_percentage_hypothesis = 0.50

# the hypothesis talks about the percentage of students with cars, also referenced in the premise
if car_percentage_hypothesis!= car_percentage_premise:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage greater than 'car_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
