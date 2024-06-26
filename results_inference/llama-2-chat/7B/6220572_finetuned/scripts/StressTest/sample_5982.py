percentage_cars_premise = 25
percentage_cars_hypothesis = 35

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if percentage_cars_hypothesis >= percentage_cars_premise:
    # check if the estimate of 'percentage_cars_hypothesis' contradicts the percentage of students with cars in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of students with cars
    # any percentage of students with cars less than 'percentage_cars_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
