# Premise: On a business trip, more than 10 percent of 60 sales representatives will be given accommodations at Hotel XYZ and the remaining 70 percent will be given accommodations at Hotel ABC.
# Hypothesis: On a business trip, 30 percent of 60 sales representatives will be given accommodations at Hotel XYZ and the remaining 70 percent will be given accommodations at Hotel ABC.
# Golden Label: neutral

XYZ_premise = 10
XYZ_hypothesis = 30
ABC_premise = 70
ABC_hypothesis = 70
sales_representatives = 60

# the hypothesis talks about the percentage of sales representatives given accommodation at Hotels XYZ and ABC, referenced also in the premise
if XYZ_hypothesis <= XYZ_premise:
    # check if the hypothesis value contradicts the estimate of more than 'XYZ_premise'
    label = "contradiction"
elif ABC_hypothesis != ABC_premise:
    # check if the percentage of sales representatives given accommodation at Hotel ABC in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of sales representatives given accommodation at Hotel XYZ
    # any percentage greater than 'XYZ_premise' and equal to 'ABC_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

