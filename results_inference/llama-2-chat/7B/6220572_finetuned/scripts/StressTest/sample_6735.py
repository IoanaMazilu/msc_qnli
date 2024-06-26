days_rohit_premise = 12
days_rohan_premise = 6
days_rohit_hypothesis = 22
days_rohan_hypothesis = 6

# the hypothesis talks about the number of days Rohit and Rohan need to complete a work, referenced also in the premise
if days_rohit_hypothesis >= days_rohit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_rohit_premise'
    label = "contradiction"
elif days_rohan_hypothesis!= days_rohan_premise:
    # check if the number of days Rohan needs to complete a work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
