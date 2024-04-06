# Premise: Mrs. Hilt saw a rollercoaster and 7.0 students rode the rollercoaster every 5.0 minutes.
# Hypothesis: 21.0 students rode the rollercoaster in 15.0 minutes.
# Golden Label: entailment

students_per_five_minutes_premise = 7.0
students_hypothesis = 21.0
time_hypothesis = 15.0

# the hypothesis refers to the number of students that rode the rollercoaster which is also mentioned in the premise
# compute the total number of students who rode the rollercoaster in the premise
students_per_fifteen_minutes_premise = students_per_five_minutes_premise * (time_hypothesis/5.0)
if students_hypothesis != students_per_fifteen_minutes_premise:
    # check if the number of students in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

