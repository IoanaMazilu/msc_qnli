pears_keith_picked = 47.0
pears_mike_picked = 12.0
pears_given_away = 46.0
pears_left_mike = 13.0

# the hypothesis refers to the number of pears left with Mike, which can be calculated from the premise
# the premise gives the total number of pears picked by Keith and the number of pears given away
# the hypothesis refers to the number of pears left with Mike, which can be calculated from the premise

if pears_left_mike!= pears_mike_picked + pears_given_away:
    # check if the number of pears left with Mike in the hypothesis contradicts the number of pears left with Mike in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values match, we can infer entailment
    label = "entailment"

print(label)
