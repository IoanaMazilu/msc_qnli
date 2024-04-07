# Premise: Series Problem like 4 12 x 44 46 132 134 begin of the Skype highlighting 44 46 132 134 end of the Skype highlighting.
# Hypothesis: Series Problem like 3 12 x 44 46 132 134 begin of the Skype highlighting 44 46 132 134 end of the Skype highlighting.
# Golden Label: contradiction

series_premise = 4
series_hypothesis = 3

# the hypothesis refers to the series problem mentioned in the premise
if series_hypothesis != series_premise:
    # check if the series problem in the hypothesis contradicts the series problem reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

