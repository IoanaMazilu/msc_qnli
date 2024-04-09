family_moved_premise = "Bahamas"
family_moved_hypothesis = "Japan"
money_premise = 6359.0
money_hypothesis = 2870.0
spent_money_premise = 3485.0

# the premise mentions the country of origin and the initial amount of money, which are also referred to in the hypothesis
# compute the total amount of money the family had after moving
total_money_premise = money_premise + spent_money_premise

# check if the hypothesis contradicts the total amount of money from the premise
if total_money_hypothesis!= total_money_premise:
    label = "contradiction"
elif money_hypothesis < money_premise:
    # check if the amount of money in the hypothesis is less than the amount of money in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
