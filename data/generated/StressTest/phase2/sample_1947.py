# Premise: In a certain province in France there are 19 cities.
# Hypothesis: In a certain province in France there are less than 89 cities.
# Golden Label: entailment

cities_premise = 19
cities_hypothesis = 89

# the hypothesis talks about the number of cities in a province, referenced also in the premise
if cities_premise >= cities_hypothesis:
    # check if the premise value contradicts the hypothesis of less than 'cities_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an upper limit for the number of cities
    # the number of cities from the premise is less than 'cities_hypothesis', consistent with the hypothesis, but the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

