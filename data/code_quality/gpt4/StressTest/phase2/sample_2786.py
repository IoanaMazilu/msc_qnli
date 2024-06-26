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
