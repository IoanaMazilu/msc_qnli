fruit_premise = 10
fruit_hypothesis = 60
avg_price_premise = 54
avg_price_hypothesis = 54

# the hypothesis talks about the number of fruits and their average price mentioned in the premise
if fruit_hypothesis != fruit_premise:
    # check if the number of fruits in the hypothesis contradicts the number of fruits mentioned in the premise
    label = "contradiction"
elif avg_price_premise != avg_price_hypothesis:
    # check if the average price in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
