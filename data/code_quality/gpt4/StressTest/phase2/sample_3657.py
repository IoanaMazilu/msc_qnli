visited_both_premise = 51
visited_both_hypothesis = 71

# the hypothesis refers to the number of people who have visited both Iceland and Norway, as mentioned in the premise
if visited_both_hypothesis < visited_both_premise:
    # check if the hypothesis value contradicts the number of people who visited both countries in the premise
    label = "contradiction"
elif visited_both_hypothesis > visited_both_premise:
    # check if the hypothesis value entails the number of people who visited both countries in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutrality
    label = "neutral"

print(label)
