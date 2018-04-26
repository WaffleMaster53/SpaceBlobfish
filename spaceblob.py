#Plan 
#buying/selling screen
#Text based
#items
#list of planets with variable prices for travelling depending on where you are
#
def move_cost(self):
    options = []
    print("Where would you like to go?\nDestination | Fuel Cost")
    for key, value in self.connections.items():
        print("("+str(list(self.connections.items()).index((key, value)))+")", end="")
        print(str(key)+"--"+str(value))
#Structure
#1 file for ships and stuff
#1 file for planets (with spaceports)
#1 file for main game and logic


#d = {key: value for (key, value) in iterable}
import random
goods=["mercury","uranium","carbon","iron","literal blobfish","bismuth","antimatter","sentient potato seeds"]


class Planet:
  def __init__(self, name, conns):
    self.name=name
    amounts = [random.randint(10,100) for i in goods]
    self.sellPrices = dict(zip(goods, amounts))
    amounts = [random.randint(self.sellPrices[i],100) for i in goods]
    self.buyPrices = dict(zip(goods, amounts))
    self.connections = conns
  
  def __str__(self):
    return self.name
  
  def display_menu(self,playere):
    print("LOCATION: "+self.name)
    print("FOR MARKET ENTER 1")
    print("FOR MOVE ENTER 2")
    print("FOR SELF-DESTRUCT ENTER 3")
    choice = input("")
    if choice=="1":
      display_buy_sell(self.name,self.sellPrices)
    elif choice=="2":
      pass
    elif choice=="3":
      pass
    else:
      print("\nInvalid choice, try again.")
      self.display_menu()
      
    def move_cost(self):
        options = {}
        print("Where would you like to go?\nDestination | Fuel Cost")
        for key, value in self.connections.items():
            num = list(self.connections.items()).index((key, value))
            dest = list(self.connections.items())[num][0]
            options[num] = dest
            print("("+str(list(self.connections.items()).index((key, value)))+")", end="")
            print(str(key)+"--"+str(value))
        choice = input("")
        if choice in options:
            return options[choice]
        else:
            print("Invalid choice")

class Ship:
    def __init__(self, name):
        self.name = name
        self.cargo_size = 10
        self.cargo = []
        self.location  = 0
        self.fuel = 100
        self.money = 10000
        
def display_buy_sell(planetname, item proces, playerE):
    buybool = input("Buy(b) or sell(s)")

    if(buybool == 'b'):
        buybool = True
    elif(buybool == 's'):
        buybool = False

    a =   "+-----------------------------+"
    print(a)
    if(buybool):
        print("|-------Buy--------------------|")
        print("|Goods          ||Prices       |")
        print(a)
        for i in range(len(goods)):
            print("|",goods[i],"    || ", goods[(goods[i])],"   |")
        print(a)
    
    elif(not buybool):
          print("|-------Sell-------------------|")
          print("|Goods          ||Prices      |")
          print(a)
          for i in range(len(goods)):
              print("| ", i, ":",goods[i],"    || ", planetname.prices[goods[i]],"  |")
              print(a)
  
    choice = int(input("Which item do you wish to purchase (please input associated number)"))
    playerE.money -= planetname.buyprices[goods[i]]
    playerE.cargo += goods[i]

  
if __name__ == "__main__":
    names=["earth","mars","jupiter","blobworld","pnf-404","reach", "tatooine"]
    paths = [{"jupiter":10, "mars":2, "blobworld":100}, {"earth":2, "pnf-404":30, "jupiter":9},{"reach":50, "earth":10, "mars":9},{"earth":100},{"mars":30},{"tatooine":50,"jupiter":50},{"reach":50}]
    planets = [Planet(names[i], paths[i]) for i in range(len(names))]
    player = Ship(input("What is your name?\n"))
    while True:
        planets[player.location].display_menu(player)
    #mainloopthing
    
    
