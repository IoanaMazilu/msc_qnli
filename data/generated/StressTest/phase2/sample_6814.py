# Premise: If less than 48% of all the students at Morse have cars, how many students are in the three lower grades?
# Hypothesis: If 18% of all the students at Morse have cars, how many students are in the three lower grades?
# Golden Label: neutral

car_students_premise = 48
car_students_hypothesis = 18

# the hypothesis talks about the percentage of students at Morse who have cars
if car_students_hypothesis >= car_students_premise:
    # check if the hypothesis value contradicts the given premise of less than 'car_students_premise'%
    label = "contradiction"
elif car_students_hypothesis < car_students_premise:
    # premise only gives an estimate of the percentage of students at Morse who have cars
    # any percentage less than 'car_students_premise'% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

