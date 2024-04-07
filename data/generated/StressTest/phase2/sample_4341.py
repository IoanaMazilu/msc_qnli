# Premise: Pooja is selling her books at puzzles land at a strange price as * she sells her book '' Vanity'' at $30 * she sells her book '' Sybil'' at $25 * she sells her book '' xmen'' at $20 At what price does she sell her book '' twilight''?
# Hypothesis: Pooja is selling her books at puzzles land at a strange price as * she sells her book '' Vanity'' at $more than 10 * she sells her book '' Sybil'' at $25 * she sells her book '' xmen'' at $20 At what price does she sell her book '' twilight''?
# Golden Label: entailment

vanity_price_premise = 30
vanity_price_hypothesis = 10
sybil_price_premise = 25
sybil_price_hypothesis = 25
xmen_price_premise = 20
xmen_price_hypothesis = 20

# the hypothesis refers to the prices of the books that Pooja sells at puzzles land mentioned in the premise
if vanity_price_premise <= vanity_price_hypothesis:
    # check if the estimate of 'vanity_price_hypothesis' contradicts the price of Vanity book in the premise
    label = "contradiction"
elif sybil_price_hypothesis != sybil_price_premise:
    # check if the price of Sybil book in the hypothesis contradicts the price of Sybil book reported in the premise
    label = "contradiction"
elif xmen_price_hypothesis != xmen_price_premise:
    # check if the price of Xmen book in the hypothesis contradicts the price of Xmen book reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

