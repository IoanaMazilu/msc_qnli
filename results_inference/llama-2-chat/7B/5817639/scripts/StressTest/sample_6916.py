gumballs_premise = 87
gumballs_hypothesis = 17
gumballs_lew = 12
gumballs_carey = 0

# the hypothesis talks about the number of gumballs bought by Carolyn, Lew, and Carey
if gumballs_hypothesis <= gumballs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'gumballs_premise'
    label = "contradiction"
elif gumballs_hypothesis - gumballs_lew!= 0:
    # check if the number of gumballs bought by Carolyn contradicts the number of gumballs bought by Lew
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
