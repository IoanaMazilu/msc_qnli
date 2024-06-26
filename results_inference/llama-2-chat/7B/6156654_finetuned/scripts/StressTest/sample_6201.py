distance_traveled_premise = 200
distance_traveled_hypothesis = 300

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation, which is also mentioned in the premise
if distance_traveled_premise >= distance_traveled_hypothesis:
    # check if the distance traveled in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the distance traveled in the premise is less than the distance traveled in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
