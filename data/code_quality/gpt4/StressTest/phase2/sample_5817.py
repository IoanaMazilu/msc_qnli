people_premise = 6
people_hypothesis = 8

# the hypothesis refers to the number of people Akash will arrange for photograph mentioned in the premise
if people_premise >= people_hypothesis:
    # check if the number of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis is less than the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
