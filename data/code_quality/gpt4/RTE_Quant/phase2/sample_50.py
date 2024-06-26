increase_army_premise = 65000
total_army_premise = 547000
increase_marines_premise = 27000
total_marines_premise = 202000

total_army_hypothesis = 547000

# the hypothesis refers to the total number of army troops as suggested by the Defense Secretary, which is also given in the premise
# no other values from the hypothesis need to be compared with the premise

if total_army_hypothesis != total_army_premise:
    # check if the total number of army troops in the hypothesis contradicts the total number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
