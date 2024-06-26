father_raj_premise = 2
father_raj_hypothesis = 4
mother_raj_premise = 2
mother_raj_hypothesis = 2

# the hypothesis refers to the years in which Raj's father and mother's age are twice as Raj's age
if father_raj_premise >= father_raj_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'father_raj_premise' 
    label = "contradiction"
elif mother_raj_hypothesis != mother_raj_premise:
    # check if the number of years ago mentioned for Raj's mother in the hypothesis contradicts the number of years ago reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in relation to Raj's father's age
    # any number of years greater than 'father_raj_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
