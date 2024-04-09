visited_both_premise = 31
visited_both_hypothesis = 41

# the hypothesis talks about the number of people who have visited both Iceland and Norway, referenced also in the premise
if visited_both_hypothesis <= visited_both_premise:
    # check if the hypothesis value contradicts the estimate of less than 'visited_both_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both countries
    # any number of people who have visited neither country is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
