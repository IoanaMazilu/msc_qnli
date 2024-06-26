traveled_miles_premise = 200
traveled_miles_hypothesis = 200

# the hypothesis refers to the number of miles traveled by Louisa on the first day of her vacation, mentioned in the premise
if traveled_miles_hypothesis <= traveled_miles_premise:
    # check if the hypothesis value contradicts the number of miles traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the number of miles traveled in the premise, it is neutral
    label = "neutral"

print(label)
