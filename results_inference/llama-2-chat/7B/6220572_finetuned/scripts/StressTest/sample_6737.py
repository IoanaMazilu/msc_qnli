days_rohit_premise = 12
days_rohan_premise = 6
days_rohit_hypothesis = 62
days_rohan_hypothesis = 6

# the hypothesis talks about the time taken by Rohit and Rohan to complete a work, referenced also in the premise
if days_rohit_hypothesis <= days_rohit_premise:
    # check if the hypothesis value contradicts the time taken by Rohit in the premise
    label = "contradiction"
elif days_rohan_hypothesis!= days_rohan_premise:
    # check if the time taken by Rohan in the hypothesis contradicts the time taken by Rohan reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Rohan
    # any time greater than 'days_rohan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
