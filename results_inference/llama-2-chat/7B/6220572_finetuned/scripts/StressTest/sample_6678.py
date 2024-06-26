aswin_sachin_sumesh_premise = 93
aswin_sachin_sumesh_hypothesis = 43

# the hypothesis refers to the sum of ages of Aswin, Sachin and Sumesh mentioned in the premise
if aswin_sachin_sumesh_hypothesis <= aswin_sachin_sumesh_premise:
    # check if the hypothesis value contradicts the estimate of more than 'aswin_sachin_sumesh_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the sum of ages
    # any sum of ages greater than 'aswin_sachin_sumesh_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
