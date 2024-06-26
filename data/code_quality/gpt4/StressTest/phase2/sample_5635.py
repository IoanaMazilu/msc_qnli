local_science_students_premise = 20
local_science_students_hypothesis = 50
total_science_students = 200

local_commerce_students_premise = 85
local_commerce_students_hypothesis = 85
total_commerce_students = 120

# the hypothesis refers to the percentage of local students among science and commerce students mentioned in the premise
if local_science_students_hypothesis <= local_science_students_premise:
    # check if the estimate of 'local_science_students_hypothesis' contradicts the percentage of local science students in the premise
    label = "contradiction"
elif local_commerce_students_hypothesis != local_commerce_students_premise:
    # check if the percentage of local commerce students in the hypothesis contradicts the percentage of local commerce students reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of local science students
    # any percentage of local science students greater than 'local_science_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
