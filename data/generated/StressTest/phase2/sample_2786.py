# Premise: If 21 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If less than 21 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: contradiction

visited_both_premise = 21
visited_both_hypothesis = 21

# the hypothesis talks about the number of people who visited both Iceland and Norway, referenced also in the premise
if visited_both_hypothesis < visited_both_premise:
    # check if the hypothesis value contradicts the exact number of 'visited_both_premise' people
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise, but also does not add new information, so it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

