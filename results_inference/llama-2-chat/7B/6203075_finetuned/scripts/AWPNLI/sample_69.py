pennies_premise = 100.0
quarters_premise = 783.0
borrowed_quarters = 271.0
quarters_now_hypothesis = 513.0

# the hypothesis refers to the number of quarters, which are also mentioned in the premise
# compute the total number of quarters in the premise
total_quarters_premise = pennies_premise + quarters_premise

# compute the number of quarters that were borrowed
borrowed_quarters_premise = borrowed_quarters

# compute the number of quarters now according to the hypothesis
quarters_now_hypothesis = total_quarters_premise - borrowed_quarters_premise

# check if the number of quarters now according to the hypothesis contradicts the number of quarters now in the premise
if quarters_now_hypothesis!= quarters_now_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
