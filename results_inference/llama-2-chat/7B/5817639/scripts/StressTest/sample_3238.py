students_with_cars_premise = 50
students_with_cars_hypothesis = 20

# the hypothesis talks about the percentage of students with cars at Morse, referenced also in the premise
if students_with_cars_hypothesis <= students_with_cars_premise:
    # check if the hypothesis value contradicts the estimate of less than'students_with_cars_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of students with cars,
    # any percentage of students with cars greater than'students_with_cars_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
