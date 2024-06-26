people_visited_both_premise = 41
people_visited_both_hypothesis = 31

# the hypothesis refers to the number of people who have visited both countries, mentioned in the premise
if people_visited_both_hypothesis >= people_visited_both_premise:
    # check if the number of people in the hypothesis contradicts the estimate of less than 'people_visited_both_premise'
    label = "contradiction"
elif people_visited_both_hypothesis < people_visited_both_premise:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_visited_both_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
