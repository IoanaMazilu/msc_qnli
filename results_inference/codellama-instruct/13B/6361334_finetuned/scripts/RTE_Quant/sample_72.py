# define variables for the numerical entities in the premise
denmark_opted_not_to_join_euro_premise = 1
sweden_adopted_euro_premise = 0
britain_adopted_euro_premise = 0

# define variables for the numerical entities in the hypothesis
sweden_adopted_euro_hypothesis = 1

# check if the number of countries that opted not to join the euro in the premise contradicts the number of countries in the hypothesis
if denmark_opted_not_to_join_euro_premise!= 1:
    label = "contradiction"
elif sweden_adopted_euro_premise!= sweden_adopted_euro_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
