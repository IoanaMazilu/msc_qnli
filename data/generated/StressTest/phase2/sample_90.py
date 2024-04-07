# Premise: John was thrice as old as Tom 6 yrs back.
# Hypothesis: John was thrice as old as Tom more than 3 yrs back.
# Golden Label: entailment

years_back_premise = 6
years_back_hypothesis = 3

# the hypothesis refers to the same age relationship between John and Tom as the premise, but the number of years back differs
if years_back_hypothesis >= years_back_premise:
    # check if the 'years_back_hypothesis' contradicts the 'years_back_premise'
    label = "contradiction"
else:
    # the premise clearly states the number of 'years_back_premise'
    # any number of years less than 'years_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

