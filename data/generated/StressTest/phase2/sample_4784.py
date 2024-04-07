# Premise: Shawn invested one half of his savings in a bond that paid simple interest for 2 years (20% per anum) and received $600 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for more than 2 years (20% per anum) and received $600 as interest.
# Golden Label: contradiction

savings_investment_premise = 0.5
savings_investment_hypothesis = 0.5
interest_years_premise = 2
interest_years_hypothesis = 2
interest_received_premise = 600
interest_received_hypothesis = 600

# the hypothesis talks about the same investment in the premise
if savings_investment_hypothesis != savings_investment_premise:
    # check if the savings investment in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif interest_received_hypothesis != interest_received_premise:
    # check if the received interest in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif interest_years_hypothesis <= interest_years_premise:
    # check if the years of interest in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # the number of years of interest in the hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

