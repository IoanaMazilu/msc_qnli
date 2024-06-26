# the premise gives a percentage of decrease in saving amount
percentage_decrease_premise = 80
# the hypothesis gives a percentage of decrease in saving amount
percentage_decrease_hypothesis = 30

if percentage_decrease_hypothesis >= percentage_decrease_premise:
    # check if the percentage of decrease in hypothesis contradicts the percentage of decrease in premise
    label = "contradiction"
else:
    # if the percentage of decrease in hypothesis is less than the percentage of decrease in premise, we can infer neutrality
    label = "neutral"

print(label)
