percentage_given_back_premise = 3
percentage_given_back_hypothesis = 3

# the hypothesis concerns the percentage of the amount Dana gives back each month, which is also discussed in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the hypothesis contradicts the premise's statement of giving back 'percentage_given_back_premise' %
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we cannot infer entailment or contradiction
    # as the premise does not provide a specific amount that Dana owes her parents after four years of college
    label = "neutral"

print(label)
