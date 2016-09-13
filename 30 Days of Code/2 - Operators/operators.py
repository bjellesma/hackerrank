def calcCost(mealCost, tipPercent, taxPercent):
    tipCost = mealCost * (tipPercent/100.0)
    taxCost = mealCost * (taxPercent/100.0)
    return mealCost + tipCost + taxCost

mealCost = float(raw_input(''))
tipPercent = int(raw_input(''))
taxPercent = int(raw_input(''))

totalCost = calcCost(mealCost, tipPercent, taxPercent)

print 'The total meal cost is %s dollars.' % int(round(totalCost, 0))
