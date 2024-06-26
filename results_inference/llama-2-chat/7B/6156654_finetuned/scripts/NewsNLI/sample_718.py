total_raised_premise = 350000
total_raised_hypothesis = 350000

# the hypothesis mentions the amount of money raised by the Jordan Thomas Foundation, which is also mentioned in the premise
if total_raised_hypothesis!= total_raised_premise:
    # check if the amount of money raised in the hypothesis contradicts the amount of money raised in the premise
    label = "contradiction"
else:
    # if the amounts are the same, it is an entailment
    label = "entailment"

print(label)
