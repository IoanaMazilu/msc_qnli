maddie_apples_premise = 18
maddie_apples_hypothesis = 58
given_apples_mike_premise = 12
given_apples_mike_hypothesis = 12

# the hypothesis refers to the number of apples Maddie has left after giving some to Mike
# the hypothesis also refers to the number of apples Maddie gives to Mike

# compute the total number of apples Maddie has after giving some to Mike
total_apples_maddie_premise = maddie_apples_premise - given_apples_mike_premise
total_apples_maddie_hypothesis = maddie_apples_hypothesis - given_apples_mike_hypothesis

# check if the number of apples Maddie has left in the hypothesis contradicts the number of apples Maddie has left in the premise
if total_apples_maddie_hypothesis!= total_apples_maddie_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
