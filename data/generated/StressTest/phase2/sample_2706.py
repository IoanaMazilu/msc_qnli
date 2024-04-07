# Premise: Kishore saved 10% of his monthly salary.
# Hypothesis: Kishore saved less than 20% of his monthly salary.
# Golden Label: entailment

saving_rate_premise = 10
saving_rate_hypothesis = 20

# the hypothesis refers to the saving rate mentioned in the premise
if saving_rate_hypothesis <= saving_rate_premise:
    # check if the estimate of 'saving_rate_hypothesis' contradicts the saving rate in the premise
    label = "contradiction"
elif saving_rate_premise >= saving_rate_hypothesis:
    # check if the saving rate in the premise contradicts the estimate of 'saving_rate_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

