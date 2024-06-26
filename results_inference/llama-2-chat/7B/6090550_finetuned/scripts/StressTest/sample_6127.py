people_visited_both_premise = 41
people_visited_both_hypothesis = 31

# the hypothesis talks about the number of people who have visited both Iceland and Norway, which is also mentioned in the premise
if people_visited_both_hypothesis >= people_visited_both_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif people_visited_both_hypothesis < people_visited_both_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
