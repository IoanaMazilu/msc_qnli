# Premise: In a certain province in France there are 15 cities.
# Hypothesis: In a certain province in France there are less than 25 cities.
# Golden Label: entailment

cities_premise = 15
cities_hypothesis = 25

# the hypothesis talks about the number of cities in a certain province in France, also mentioned in the premise
if cities_premise >= cities_hypothesis:
    # check if the number of cities in the premise contradicts the estimate of less than 'cities_hypothesis'
    label = "contradiction"
elif cities_premise == cities_hypothesis - 1:
    # check if the number of cities in the premise can be fully and explicitly entailed from the hypothesis
    label = "entailment"
else:
    # the hypothesis gives only an estimate for the number of cities
    # any number of cities less than 'cities_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

