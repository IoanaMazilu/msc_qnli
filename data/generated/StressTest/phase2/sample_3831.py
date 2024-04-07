# Premise: If there are 10 peanuts in a box and Mary puts 8 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are less than 30 peanuts in a box and Mary puts 8 more peanuts inside, how many peanuts are in the box?
# Golden Label: entailment

peanuts_premise = 10
peanuts_added = 8
peanuts_hypothesis = 30

# the hypothesis speculates about a situation where there are less than 'peanuts_hypothesis' in a box and Mary adds 'peanuts_added'
total_peanuts_premise = peanuts_premise + peanuts_added

if total_peanuts_premise >= peanuts_hypothesis:
    # check if the total number of peanuts in the premise contradicts the estimate of less than 'peanuts_hypothesis'
    label = "contradiction"
elif peanuts_added != peanuts_added:
    # verify if the number of peanuts added by Mary in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

