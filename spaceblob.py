#Plan 
#buying/selling screen
#Text based
#items
#list of planets with variable prices for travelling depending on where you are
#

#Structure
#1 file for ships and stuff
#1 file for planets (with spaceports)
#1 file for main game and logic


#d = {key: value for (key, value) in iterable}
import random
goods=["mercury","uranium","carbon","iron","literal blobfish","bismuth","antimatter","sentient potato seeds"]


class Planet:
  def __init__(self, name):
    self.name=name
    amounts = [random.randint(10,100) for i in goods]
    self.sellPrices = dict(zip(goods, amounts))
    amounts = [random.randint(self.sellPrices[i],100) for i in goods]
    self.buyPrices = dict(zip(goods, amounts))
    
  
class Ship:
    def __init__(self, name):
        self.name = name
        self.cargo_size = 10
        self.cargo = []
  
def display_buy_sell(planetname, goods)

	print("Buy(b) or sell(s)")
  buybool 
		
	a =   "+-----------------------------+"
  print(a)
  if(buybool):
    print("|-------Buy--------------------|")
  elif(not buybool):
    print("|-------Sell-------------------|")
  print("|Goods          ||Prices      |")
  print(a)
  for i in goods:
    print("|",i,"    || ", planetname.prices[i], "  |")
  print(a)

  
if __name__ == "__main__":
  money=10000
  names=["earth","mars","jupiter","blobworld","pnf-404","Reach", "Tatooine"]
  planets=[planet(i) for i in names]
  while True:
    #mainloopthing
