visited_both_premise = 71
visited_both_hypothesis = 21

# the hypothesis is referring to the number of people who visited both countries, also mentioned in the premise
if visited_both_hypothesis >= visited_both_premise:
    # check if the hypothesis value contradicts the estimate of less than 'visited_both_premise'
    label = "contradiction"
elif visited_both_hypothesis < visited_both_premise:
    # the premise gives an estimate for the number of people who visited both countries
    # any number of people less than 'visited_both_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
