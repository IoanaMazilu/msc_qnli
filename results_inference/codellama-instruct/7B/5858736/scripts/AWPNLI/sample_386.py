# define variables with representative names for the numerical entities in both inputs
keith_pears_premise = 47.0
mike_pears_premise = 12.0
keith_gave_away_pears_premise = 46.0
mike_pears_hypothesis = 13.0

# extract all quantities as valid numbers (integers or floats)
total_pears_premise = keith_pears_premise + mike_pears_premise
total_pears_given_away_premise = keith_gave_away_pears_premise

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments
if total_pears_hypothesis >= total_pears_given_away_premise:
    # check if the total pears from the hypothesis is greater than or equal to the total pears given away in the premise
    label = "entailment"
elif mike_pears_hypothesis!= (total_pears_premise - total_pears_given_away_premise):
    # check if the number of pears from the hypothesis contradicts the estimate of the total pears in the premise minus the total pears given away
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
