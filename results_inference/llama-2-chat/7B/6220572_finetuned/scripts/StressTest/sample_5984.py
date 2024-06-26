car_percentage_premise = 25
car_percentage_hypothesis = 85

# the hypothesis talks about the percentage of students with cars, referenced also in the premise
if car_percentage_hypothesis <= car_percentage_premise:
    # check if the hypothesis value contradicts the estimate of 'car_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage of students with cars greater than 'car_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
