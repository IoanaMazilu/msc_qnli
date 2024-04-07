# Premise: Series Problem like 4 12 x 44 46 132 134 begin of the Skype highlighting 44 46 132 134 end of the Skype highlighting.
# Hypothesis: Series Problem like 7 12 x 44 46 132 134 begin of the Skype highlighting 44 46 132 134 end of the Skype highlighting.
# Golden Label: contradiction

series_premise = 4
series_hypothesis = 7

# the hypothesis refers to the series problem mentioned in the premise
if series_premise != series_hypothesis:
    # check if the start of the series in the hypothesis contradicts the start of the series in the premise
    label = "contradiction"
else:
    # the premise and hypothesis describe the same series
    label = "entailment"

print(label)

