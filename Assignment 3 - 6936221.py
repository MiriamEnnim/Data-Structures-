#my github account is MiriamEnnim
#https://github.com/MiriamEnnim
"MIRIAM ENNIM"
"CIVIL ENGINEERING 2"
"COMPUTER APPLICATIONS IN CIVIL ENGINEERING"
"6936221"
#Selling cars to prospective buyer
print()
CarsAvailable=['SUV', 'Sedan', 'Minivan', 'Pickup truck', 'Crossover', 'Hatchback']
print('These are the kind of cars available: {0}, {1}, {2}, {3}, {4}, {5}'.format('SUV', 'Sedan', 'Minivan', 'Pickup truck', 'Crossover', 'Hatchback'))
#the different brands available for each kind of car saved in a dictionary
BrandsAvailable = {'SUV':'Toyota RAV4, Jeep Grand Cherokee, Honda HR-V, Nissan Pathfinder, Jeep Cherokee', 'Sedan':'Hyundai accent, Honda Accord, Mercedes Benz, BMW 4 series 430i, Toyota Camry', 'Minivan':'Toyota Sienna, Honda Odyssey, Dodge Caravan, Kia Carnival, Chrysler Pacifica', 'Pickup truck':'Ford F-150, RAM 1500, Toyota Tundra, Chevrolet Silverado, Nissan Frontier', 'Crossover':'Kia Sportage, Mazda CX-5, Hyundai Tucson, Nissan Rogue, Honda CR-V', 'Hatchback':'Ford fiesta, Honda civic, Toyota Yaris, Kia rio, Suzuki celerio'}
#prices of the various cars saved in a dictionary
prices = {'Toyota RAV4':'$27,600','Jeep Grand Cherokee':'$42,900','Honda HR-V':'$23,650','Nissan Pathfinder':'$37,820','Jeep Cherokee':'$39,300','Hyundai accent':'$17,000','Honda Accord':'$28,400','Mercedes Benz':'$45,900','BMW 4 series 430i':'$55,300','Toyota Camry':'$26,300','Toyota Sienna':'$37,400','Honda Odyssey':'$38,900','Dodge Caravan':'$29,025','Kia Carnival':'$34,500','Chrysler Pacifica':'$37,020','Ford F-150':'$35,700','RAM 1500':'$39,300','Toyota Tundra':'$36,000','Chevrolet Silverado':'$34,600','Nissan Frontier':'$28,690','Kia Sportage':'$25,990','Mazda CX-5':'$27,350','Hyundai Tucson':'$26,450','Nissan Rogue':'$27,360','Honda CR-V':'$31,110','Ford fiesta':'$15,000','Honda civic':'$24,650','Toyota Yaris':'$27,600','Kia rio':'$17,490','Suzuki celerio':'$12,350'}
Choose=input('What kind of car do you want?: ')
print()
#conditional loop to provide the necessary information to buyer based the choices made
if Choose in CarsAvailable:
    print('These are the brands available: '+ BrandsAvailable[Choose])
else: print('Sorry, we do not have that.')
specify=input('Which brand would you want: ')
if specify in BrandsAvailable[Choose]:
    print('The car costs '+prices[specify])
else: print('Sorry, we do not have that.')