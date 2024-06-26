friends_premise = 8
friends_hypothesis = 4
car_capacity_premise = 3
car_capacity_hypothesis = 3

# The hypothesis talks about the number of John's friends who want to ride in his car and the car's capacity, both referenced in the premise
if friends_hypothesis >= friends_premise:
    # Check if the number of friends in the hypothesis contradicts the estimate of less than 'friends_premise'
    label = "contradiction"
elif car_capacity_hypothesis != car_capacity_premise:
    # Check if the car's capacity in the hypothesis contradicts the car's capacity mentioned in the premise
    label = "contradiction"
else:
    # The premise gives an estimate for the number of friends, 
    # any number less than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
