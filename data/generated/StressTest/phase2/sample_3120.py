# Premise: John was thrice as old as Tom 6 yrs back.
# Hypothesis: John was thrice as old as Tom less than 7 yrs back.
# Golden Label: entailment

years_back_premise = 6
years_back_hypothesis = 7

# the hypothesis talks about the time period when John was thrice as old as Tom, also mentioned in the premise
if years_back_hypothesis > years_back_premise:
    # check if the hypothesis value contradicts the premise's claim of 'years_back_premise'
    label = "contradiction"
elif years_back_hypothesis == years_back_premise:
    # if the time period in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # any time period less than 'years_back_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

