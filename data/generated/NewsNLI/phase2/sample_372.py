# Premise: Overall, 2,500 delegates traveled to Davos from more than 100 countries.
# Hypothesis: Overall, 2,500 delegates traveled to Davos from more than 100 countries around the world.
# Golden Label: entailment

delegates_premise = 2500
delegates_hypothesis = 2500
countries_premise = 100
countries_hypothesis = 100

# the hypothesis mentions the number of delegates and the number of countries they came from, which are also mentioned in the premise
if delegates_hypothesis != delegates_premise:
    # check if the number of delegates in the hypothesis contradicts the number of delegates reported in the premise
    label = "contradiction"
elif countries_hypothesis != countries_premise:
    # check if the number of countries from the hypothesis contradicts the number of countries in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

