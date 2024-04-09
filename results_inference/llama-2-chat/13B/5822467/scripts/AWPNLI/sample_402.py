pears_premise = 42.0
pears_sold_premise = 17.0
pears_left_hypothesis = 25.0

# compute the difference between the number of pears left in the premise and the number of pears left in the hypothesis
difference = pears_left_hypothesis - pears_left_premise

if difference > 0:
    # if the number of pears left in the hypothesis is greater than the number of pears left in the premise, we have entailment
    label = "entailment"
elif difference < 0:
    # if the number of pears left in the hypothesis is less than the number of pears left in the premise, we have contradiction
    label = "contradiction"
else:
    # if the difference is zero, we have neutrality
    label = "neutrality"

print(label)
