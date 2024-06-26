sophie_germain_premise = 3
sophie_germain_hypothesis = 2

# the hypothesis refers to the condition for a prime number to be a Sophie Germain prime
if sophie_germain_hypothesis <= sophie_germain_premise:
    # check if the hypothesis value contradicts the estimate of'sophie_germain_premise'
    label = "contradiction"
elif 2 * sophie_germain_hypothesis + 1!= sophie_germain_premise:
    # check if the hypothesis value contradicts the condition reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
