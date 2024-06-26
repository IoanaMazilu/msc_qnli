friends_premise = 6
friends_hypothesis = 5
car_capacity = 5

# the hypothesis refers to the number of John's friends and car capacity mentioned in the premise
if friends_hypothesis > car_capacity:
    # check if the number of friends in the hypothesis exceeds the car capacity
    label = "contradiction"
elif friends_hypothesis < friends_premise:
    # if the number of friends in the hypothesis is less than the number of friends in the premise, we infer entailment
    label = "entailment"
else:
    # if neither contradiction nor entailment is determined, we infer neutrality
    label = "neutral"

print(label)
