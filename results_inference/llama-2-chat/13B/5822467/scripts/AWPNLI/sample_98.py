students_premise = 14.0
seats_premise = 2.0
buses_hypothesis = 7.0

# compute the total number of seats needed for the trip
total_seats_needed = seats_premise * buses_hypothesis

if total_seats_needed!= students_premise:
    # check if the number of seats needed in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
