people_visited_both_premise = 11
people_visited_both_hypothesis = 41

# the hypothesis talks about the number of people who have visited both Iceland and Norway, referenced also in the premise
if people_visited_both_hypothesis <= people_visited_both_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_visited_both_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who visited both countries
    # any number of people greater than 'people_visited_both_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
