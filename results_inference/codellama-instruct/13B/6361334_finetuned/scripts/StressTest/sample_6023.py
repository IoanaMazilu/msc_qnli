annual_borrowing_premise = 5000
annual_borrowing_hypothesis = 3000

# the hypothesis refers to the amount of money borrowed annually for college education, which is also mentioned in the premise
if annual_borrowing_hypothesis <= annual_borrowing_premise:
    # check if the estimate of 'annual_borrowing_hypothesis' contradicts the amount of money borrowed in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
