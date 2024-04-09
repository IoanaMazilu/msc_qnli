cindy_thinking_number_premise = 0
cindy_thinking_number_hypothesis = 4

# the hypothesis talks about the number Cindy is thinking of, which is referenced in the premise
if cindy_thinking_number_hypothesis <= cindy_thinking_number_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cindy_thinking_number_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number Cindy is thinking of
    # any number less than 'cindy_thinking_number_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
