socks_tina_premise = 5
socks_tina_hypothesis = 2
shoes_tina_premise = 3
shoes_tina_hypothesis = 3

if socks_tina_hypothesis!= socks_tina_premise:
    label = "contradiction"
elif shoes_tina_hypothesis!= shoes_tina_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
