people_visited_both_premise = 71
people_visited_both_hypothesis = 61

# the hypothesis refers to the number of people who visited both countries mentioned in the premise
if people_visited_both_hypothesis >= people_visited_both_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_visited_both_premise'
    label = "contradiction"
elif people_visited_both_hypothesis < people_visited_both_premise:
    # check if the hypothesis value is less than 'people_visited_both_premise'
    # if it is, then it doesn't contradict the premise and can be entailed from it
    label = "entailment"

print(label)
