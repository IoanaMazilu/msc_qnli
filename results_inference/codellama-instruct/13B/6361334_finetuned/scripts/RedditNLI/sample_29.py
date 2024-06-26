president_bush_premise = 2002
president_bush_hypothesis = 2002

# the hypothesis and premise mention the same president and year
if president_bush_premise!= president_bush_hypothesis:
    # check if the president and year in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of homeowners
    # any estimate of the number of homeowners in the hypothesis greater or equal to '5.5 million' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
