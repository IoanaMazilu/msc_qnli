# Premise: Molly is the owner of the Wafting Pie Company and her employees used 816.0 eggs to bake pumpkin pies this morning, and 1339.0 eggs this afternoon.
# Hypothesis: 2155.0 eggs were used this day.
# Golden Label: entailment

eggs_morning_premise = 816.0
eggs_afternoon_premise = 1339.0
total_eggs_hypothesis = 2155.0

# the hypothesis refers to the total number of eggs used in a day, which are also mentioned in the premise
# compute the total number of eggs used in the premise
total_eggs_premise = eggs_morning_premise + eggs_afternoon_premise
if total_eggs_hypothesis != total_eggs_premise:
    # check if the total number of eggs in the hypothesis contradicts the total number of eggs from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

