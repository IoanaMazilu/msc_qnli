city_a_to_city_b_premise = 1
city_a_to_city_b_hypothesis = 0.5

# the hypothesis refers to the time taken by Andrew to drive from city A to city B
if city_a_to_city_b_hypothesis <= city_a_to_city_b_premise:
    # check if the estimate of 'city_a_to_city_b_hypothesis' contradicts the time taken by Andrew to drive from city A to city B in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Andrew to drive from city A to city B
    # any time taken by Andrew to drive from city A to city B greater than 'city_a_to_city_b_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
