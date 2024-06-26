years_future_premise = 65
years_future_hypothesis = 15

# the hypothesis refers to a future time when Lyn the Lion will be half as old as Ele the Elephant
# the premise also refers to a future time when Lyn the Lion will be half as old as Ele the Elephant

if years_future_hypothesis >= years_future_premise:
    # check if the hypothesis time contradicts the premise time which is less than 'years_future_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the future time 
    # the hypothesis time is less than 'years_future_premise' which is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
