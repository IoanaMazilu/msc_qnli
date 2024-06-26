crayons_birthday_premise = 479.0
crayons_end_school_year_premise = 134.0
crayons_lost_or_given_away_hypothesis = 345.0

# the hypothesis refers to the number of crayons that were lost or given away, which are also mentioned in the premise
# compute the total number of crayons that were lost or given away
total_crayons_lost_or_given_away = crayons_birthday_premise - crayons_end_school_year_premise
if total_crayons_lost_or_given_away!= crayons_lost_or_given_away_hypothesis:
    # check if the number of crayons that were lost or given away in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
