total_amount_premise = 6600
total_amount_hypothesis = 6600

# the hypothesis talks about the total amount shared by John, Jose and Binoy, referenced also in the premise
if total_amount_hypothesis < total_amount_premise:
    # check if the hypothesis value contradicts the total amount mentioned in the premise
    label = "contradiction"
elif total_amount_hypothesis > total_amount_premise:
    # check if the hypothesis value contradicts the total amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
