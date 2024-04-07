# Premise: Shawn invested one half of his savings in a bond that paid simple interest for less than 5 years (20% per anum) and received $600 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for 2 years (20% per anum) and received $600 as interest.
# Golden Label: neutral

interest_premise = 600
interest_hypothesis = 600
interest_rate = 20/100
years_premise = 5
years_hypothesis = 2

# the hypothesis refers to the duration of investment and interest received, as mentioned in the premise
if interest_hypothesis != interest_premise:
    # check if the interest received in the hypothesis contradicts the interest received reported in the premise
    label = "contradiction"
elif years_hypothesis >= years_premise:
    # check if the duration of investment in the hypothesis contradicts the duration of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
