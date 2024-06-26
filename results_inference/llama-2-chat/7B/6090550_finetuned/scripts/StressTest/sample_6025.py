percentage_given_back_premise = 6
percentage_given_back_hypothesis = 4

# the hypothesis talks about the percentage of the amount that Dana gives back to her parents each month, which is also mentioned in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis is less than the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
