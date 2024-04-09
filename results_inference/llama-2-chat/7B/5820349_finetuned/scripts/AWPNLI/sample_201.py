seats_premise = 14.0
people_per_seat_premise = 6.0
total_people_hypothesis = 85.0

# the hypothesis refers to the total number of people that can ride the Ferris wheel, which is related to the number of seats and people per seat in the premise
# compute the total number of people that can ride the Ferris wheel in the premise
total_people_premise = seats_premise * people_per_seat_premise
if total_people_hypothesis!= total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
