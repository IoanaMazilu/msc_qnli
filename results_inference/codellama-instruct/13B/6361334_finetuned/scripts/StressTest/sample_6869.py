num_people_premise = 5
num_people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench
# the premise mentions a specific number of people that cannot be seated on the middle seat or at either end
if num_people_hypothesis <= num_people_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of people that cannot be seated on the middle seat or at either end
    # any number of people greater than 'num_people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
