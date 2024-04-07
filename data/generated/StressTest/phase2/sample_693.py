# Premise: John was thrice as old as Tom 6 yrs back.
# Hypothesis: John was thrice as old as Tom more than 4 yrs back.
# Golden Label: entailment

years_back_premise = 6
years_back_hypothesis = 4

# the hypothesis talks about the number of years back, referenced also in the premise
if years_back_hypothesis >= years_back_premise:
    # check if the hypothesis value contradicts the premise 
    label = "contradiction"
else:
    # the premise gives only an exact number of years back
    # any number of years less than 'years_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

