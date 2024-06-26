distance_cities_premise = 100
distance_cities_hypothesis = 100

# the premise and hypothesis refer to the same distance
if distance_cities_premise!= distance_cities_hypothesis:
    # check if the estimate of 'distance_cities_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same distance
    label = "entailment"

print(label)
