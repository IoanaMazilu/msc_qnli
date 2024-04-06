# Premise: Mrs. Hilt saw a rollercoaster and 7.0 students rode the rollercoaster every 5.0 minutes.
# Hypothesis: 22.0 students rode the rollercoaster in 15.0 minutes.
# Golden Label: contradiction

students_per_ride_premise = 7.0
ride_duration_premise = 5.0
students_hypothesis = 22.0
duration_hypothesis = 15.0

# the hypothesis refers to the number of students that rode the rollercoaster in a certain duration
# which are also mentioned in the premise
# compute the total number of students in the premise
total_students_premise = (duration_hypothesis / ride_duration_premise) * students_per_ride_premise
if total_students_premise != students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

