seats_premise = 14.0
seat_capacity_premise = 6.0
people_hypothesis = 85.0

# compute the total number of people that can ride the Ferris wheel based on the premise
total_people_premise = seats_premise * seat_capacity_premise

if people_hypothesis > total_people_premise:
    # check if the number of people in the hypothesis contradicts the estimate of the premise
    label = "contradiction"
elif people_hypothesis == total_people_premise:
    # if the number of people in the hypothesis is equal to the estimate of the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of people in the hypothesis is less than the estimate of the premise, we can infer neutrality
    label = "neutral"

print(label)
