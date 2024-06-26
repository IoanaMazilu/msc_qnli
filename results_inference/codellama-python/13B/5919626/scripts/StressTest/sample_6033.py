people_city_premise = 40
people_city_hypothesis = 70

# the hypothesis talks about the number of people in a city, referenced also in the premise
if people_city_hypothesis <= people_city_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_city_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in a city
    # any number of people greater than 'people_city_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
