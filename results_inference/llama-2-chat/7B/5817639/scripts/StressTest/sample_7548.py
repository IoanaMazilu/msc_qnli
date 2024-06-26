saving_amount_premise = float(input("Premise: "))
saving_amount_hypothesis = float(input("Hypothesis: "))

# the hypothesis talks about the decrease in saving amount, which is also mentioned in the premise
if saving_amount_hypothesis <= saving_amount_premise:
    # check if the hypothesis value contradicts the estimate of decrease in saving amount in the premise
    label = "contradiction"
elif saving_amount_hypothesis / saving_amount_premise < 0.8:
    # check if the ratio of decrease in hypothesis to decrease in premise is less than 0.8, which is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
