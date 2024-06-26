tom_departure_premise = 8
tom_departure_hypothesis = 6

# the hypothesis refers to the time Tom departs, which is also mentioned in the premise
if tom_departure_hypothesis >= tom_departure_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise gives the exact time Tom departs
    # any time less than 'tom_departure_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
