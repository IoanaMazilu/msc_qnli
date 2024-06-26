efrida_home = 35
frazer_home = 35
efrida_frazer_apart = 15

# the hypothesis talks about the distance between Efrida and Frazer's homes
if efrida_frazer_apart <= efrida_home and efrida_frazer_apart <= frazer_home:
    # check if the hypothesis value contradicts the estimate of less than 'efrida_home' and 'frazer_home'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Efrida and Frazer's homes
    # any distance greater than 'efrida_home' and 'frazer_home' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
