max_digit_premise = 7
max_digit_hypothesis = 5

# the hypothesis is talking about the maximum value of the digits A and B, which is also referenced in the premise
if max_digit_hypothesis > max_digit_premise:
    # check if the maximum value of the digits in the hypothesis contradicts the maximum value of the digits in the premise
    label = "contradiction"
elif max_digit_hypothesis < max_digit_premise:
    # if the maximum value of the digits in the hypothesis is less than the maximum value in the premise, we can infer entailment
    label = "entailment"
else:
    # if the maximum value of the digits in the hypothesis is equal to the maximum value in the premise, we can infer neutrality
    label = "neutral"

print(label)
