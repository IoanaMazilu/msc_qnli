number_premise = 8
number_hypothesis = 4

# the hypothesis talks about the number Cindy is thinking of, which is also referenced in the premise
if number_hypothesis >= number_premise:
    # check if the hypothesis value contradicts the estimate of less than 'number_premise'
    label = "contradiction"
elif number_hypothesis < number_premise:
    # if the hypothesis value is less than the premise, it is entailed
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
