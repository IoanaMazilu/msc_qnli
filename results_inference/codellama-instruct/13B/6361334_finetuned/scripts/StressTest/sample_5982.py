percentage_cars_premise = 25
percentage_cars_hypothesis = 35

# the hypothesis refers to the percentage of students with cars at Morse, which is also mentioned in the premise
if percentage_cars_hypothesis >= percentage_cars_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars at Morse
    # any percentage of students with cars less than 'percentage_cars_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
