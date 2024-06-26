y_premise = 80
y_hypothesis = 30

# the hypothesis talks about the number of hours Harry works per week, which is also mentioned in the premise
if y_hypothesis >= y_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
elif y_hypothesis < y_premise:
    # if the number of hours in the hypothesis is less than the number of hours in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of hours in the hypothesis is equal to the number of hours in the premise, we can infer neutrality
    label = "neutral"

print(label)
