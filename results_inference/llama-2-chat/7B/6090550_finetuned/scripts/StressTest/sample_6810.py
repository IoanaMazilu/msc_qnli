ys_premise = 300
ys_hypothesis = 500

# the hypothesis refers to the number of seniors at Morse High School and the percentage of seniors with cars, both mentioned in the premise
if ys_hypothesis <= ys_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif ys_hypothesis > ys_premise:
    # check if the number of seniors in the hypothesis is less than the number of seniors in the premise
    label = "entailment"
else:
    # if the number of seniors in the hypothesis is equal to the number of seniors in the premise, we can infer neutral
    label = "neutral"

print(label)
