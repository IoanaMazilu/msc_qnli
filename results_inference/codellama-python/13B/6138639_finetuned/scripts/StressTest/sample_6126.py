people_visited_both_premise = 31
people_visited_both_hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway, mentioned in the premise
if people_visited_both_hypothesis <= people_visited_both_premise:
    # check if the estimate of 'people_visited_both_hypothesis' contradicts the number of people who have visited both countries in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both countries
    # any number of people greater than 'people_visited_both_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
