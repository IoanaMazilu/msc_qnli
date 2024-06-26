people_premise = 5
people_hypothesis = 5

# The hypothesis refers to the number of people that can be seated on a bench, also mentioned in the premise
if people_hypothesis >= people_premise:
    # Check if the 'people_hypothesis' contradicts the premise, which mentions exactly 'people_premise' people
    label = "contradiction"
else:
    # The premise specifies a number of people
    # Any number less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
