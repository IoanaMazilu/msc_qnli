# Premise: The ages of Patrick and Michael are in the ratio of 3:5 and that of Michael and Monica are in the ratio of 3:5.
# Hypothesis: The ages of Patrick and Michael are in the ratio of less than 3:5 and that of Michael and Monica are in the ratio of 3:5.
# Golden Label: contradiction

patrick_michael_ratio_premise = 3 / 5
patrick_michael_ratio_hypothesis = 3 / 5
michael_monica_ratio_premise = 3 / 5
michael_monica_ratio_hypothesis = 3 / 5

# the hypothesis talks about the age ratios of Patrick and Michael, and of Michael and Monica, referenced also in the premise
if patrick_michael_ratio_hypothesis > patrick_michael_ratio_premise:
    # check if the 'patrick_michael_ratio_hypothesis' contradicts the ratio of Patrick and Michael's ages in the premise
    label = "contradiction"
elif michael_monica_ratio_hypothesis != michael_monica_ratio_premise:
    # check if the 'michael_monica_ratio_hypothesis' contradicts the ratio of Michael and Monica's ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

