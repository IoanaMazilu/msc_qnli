ponies_with_horseshoes_premise = 5/7
ponies_with_horseshoes_hypothesis = 8/7
ponies_from_iceland_premise = 2/3
ponies_from_iceland_hypothesis = 2/3

# the hypothesis refers to the number of ponies with horseshoes and the number coming from Iceland, mentioned in the premise
if ponies_with_horseshoes_hypothesis >= ponies_with_horseshoes_premise:
    # check if the hypothesis value contradicts the precise number 'ponies_with_horseshoes_premise'
    label = "contradiction"
elif ponies_from_iceland_hypothesis != ponies_from_iceland_premise:
    # check if the number of ponies from Iceland in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
