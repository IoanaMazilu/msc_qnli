rate_borrowed_premise = 6
rate_borrowed_hypothesis = 8

# the hypothesis talks about the rate of borrowing money, which is also mentioned in the premise
if rate_borrowed_hypothesis!= rate_borrowed_premise:
    # check if the rate of borrowing money in the hypothesis contradicts the rate of borrowing money in the premise
    label = "contradiction"
else:
    # if the hypothesis rate matches the premise rate, it is entailed by the premise
    label = "entailment"

print(label)
