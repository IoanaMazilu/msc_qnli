award_per_family_premise = 4000000
families_premise = 2
total_award_premise = award_per_family_premise * families_premise

award_per_family_hypothesis = 4000000
families_hypothesis = 2
total_award_hypothesis = award_per_family_hypothesis * families_hypothesis

# the hypothesis mentions the total award given to the two families, which is also referenced in the premise
if total_award_hypothesis != total_award_premise:
    # check if the total award in the hypothesis contradicts the total award reported in the premise
    label = "contradiction"
else:
    # if the awards values and numbers of families do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
