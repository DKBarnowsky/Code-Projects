print('==================================================================================')
print()
print('| Hello and thank you for chossing to shop at Macromart, lets get into spending.. |')
print()
print('==================================================================================')

item = ""
price = ""
catagorty = ['Place Item','Remove Item','Display Item','Scan Item','Exit']

items = []
prices = []
        
for catagories in catagorty:
    catagorty = item and price
   
print('[Place Item|Remove Item|Display Item|Scan Item|Exit]')
catagorty = input('What would you like to see: ')

    #===[Coding for the "place item" Command]======================================
while catagorty != "exit":
    if catagorty == "place item":
        
        print()
        print('===========================================')
        print(f'| The [{catagorty}] command is now active |')
        print('===========================================')
        print()
        
        item_placed = (input('\nOk then, insert desired item here: '))
        price = float(input('\nNow insert items price here: $'))
                
        for price in item_placed:
            item == True
        else:
            item == False
        
            print()
            print('==============================================')   
            print(f'| Your [{item_placed}] is now stored in the Display |')        
            print('==============================================')
            print()
                    
            print('Place Items|Remove Items|Display Items|Scan Items|Exit')
            catagorty = input('What would you like to see: ') 
            print()
              
    #===[Coding for the "remove item" Command]======================================               
    elif catagorty == "remove item":
        
        print()
        print('===========================================')
        print(f'| The [{catagorty}] command is now active |')
        print('===========================================')
        print()
        
        item_placed = int((input('Please Insert Unwanted item here: ')))
        item_removed = item_placed - 1
        items.pop(item_removed)
        prices.pop(item_removed)
        
        print()
        print('===================================================')
        print(f'| The [{item_removed}] is no longer stored in the Display |')  
        print('===================================================')
        print()
                
        print('Place Items|Remove Items|Display Items|Scan Items|Exit')
        catagorty = input('What would you like to see: ') 
        print()
          
                   
    #===[Coding for the "display item" Command]======================================
    elif catagorty == "display item":
        
        print()
        print('=========================================')
        print(f'The [{catagorty}] command is now active')
        print('=========================================')
        print()
        
        item_display = None
            
        for i, item_display in enumerate(catagories):
            items.append(item)
            prices.append(price)
        
         
            print('\n ==========================================================================')
            print('Heres an quick distplay of what you have Stocked: ')
            print(f'\n [{item}-${price}]',end="")
            print(f'\n [{items}-${prices}]',end="")
            print('\n ==========================================================================')
            
            
        print('\n Place Items|Remove Items|Display Items|Scan Items|Exit')
        catagorty = input('What would you like to see: ') 
        print()
        
        
    #===[Coding for the "scan item" Command]======================================            
    elif catagorty == "scan item":
        print()
        print('===========================================')
        print(f'| The [{catagorty}] command is now active |')
        print('===========================================')
        print()
        
        item_placed = []
        scan_cost = []
        full_cost = []
        
        for i in range(len(item_placed)):
            print(f"{items[i]} - ${prices[i]}")

            scan_cost += prices[i]

            full_cost = scan_cost / len(prices) # total amount of cash is displayed here.

        print(f"Total: ${scan_cost}")
        print(f"Average: ${full_cost}")
        print()
        print('===============================================')
        print(f'| as shown, ${full_cost} is your total amount |')
        print('===============================================')
        print()
        
        print('Place Items|Remove Items|Display Items|Scan Items|Exit')
        catagorty = input('What would you like to see: ') 
        print()
       
       
        
    elif catagorty == "print item": #Programming Shortcut
        str(print(f'The {item} cost ${price}!!'))
        print()
        
        print('========================================')
        print('| thank you for shopping at Macromart!! |')
        print('========================================')