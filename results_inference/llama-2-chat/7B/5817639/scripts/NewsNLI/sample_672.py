snow_premise = 3.9
snow_hypothesis = 5.5

# compare the snowfall amounts in the hypothesis with the premise
if snow_hypothesis!= snow_premise:
    # if the snowfall amount in the hypothesis is greater than the premise, it contradicts
    label = "contradiction"
else:
    # if the snowfall amount in the hypothesis is equal to or less than the premise, it entails
    label = "entailment"

print(label)
