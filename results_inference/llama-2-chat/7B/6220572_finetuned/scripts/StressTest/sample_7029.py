routes_premise = 0
routes_hypothesis = 7

# the hypothesis refers to the number of possible routes in the premise
if routes_hypothesis <= routes_premise:
    # check if the hypothesis estimate contradicts the number of possible routes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of possible routes
    # any number of possible routes greater than 'routes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
