# Premise: John was thrice as old as Tom less than 7 yrs back.
# Hypothesis: John was thrice as old as Tom 6 yrs back.
# Golden Label: neutral

years_back_premise = 7
years_back_hypothesis = 6

# the hypothesis talks about the time period in the past when John was three times as old as Tom, also mentioned in the premise
if years_back_hypothesis != years_back_premise:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
else:
    # if the time periods in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)

