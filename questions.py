import random
from fractions import Fraction

names = ["Robert", "John", "Billy", "Thomas", "Kristen", "Otto", "Lucy", "Trent", "Kelly", "Luis", "Brent", "Samantha", "Fernando", "Gabriel", "Mike", "Brandon", "Briana", "Diana"]


def simple_addition():

    #Generates a simple addition problem
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    q = (f"{num1}+{num2}=")
    ans = num1+num2
    
    return [q, ans]

def division_small_div_no_rem():

    #Generates a division problem with one single digit divisor and a triple digit dividend (No remainder)
    num1 = random.randint(10, 99)
    num2 = random.randint(2, 9)
    product = (num1*num2)
    q = (f"{product}/{num2}=")
    ans = num1
    
    return [q, ans]

def division_med_div_rem():

    #Generates a division problem with a two-digit divisor and a triple digit dividend (Remainder possible)
    num1 = random.randint(100, 500)
    num2 = random.randint(10, 99)
    quotient = (num1//num2)
    q = (f"{num1}/{num2}=")
    ans = (f"{quotient}r{num1%num2}")

    return [q, ans]

def division_small_div_rem():

    #Generates a division problem with a single digit divisor and a triple digit dividend (Remainder possible)
    num1 = random.randint(100, 999)
    num2 = random.randint(1, 9)
    quotient = (num1//num2)
    q = (f"{num1}/{num2}=")
    ans = (f"{quotient}r{num1%num2}")

    return [q, ans]

def division_big_div_rem():

    #Generates a division problem with a two-digit divisor and a triple digit dividend (Remainder possible) (#14)
    num1 = random.randint(100, 999)
    num2 = random.randint(10, 99)
    quotient = (num1/num2)
    q = (f"${num1}/{num2}=")
    ans = ("${:.2f}".format(quotient))

    return [q, ans]

def fraction_addition_easy():

    #Generates a fraction addition problem
    frac1 = Fraction(1, random.randint(2, 4))
    frac2 = Fraction(1, random.randint(2, 4))
    sum = (frac1+frac2)
    q = (f"{frac1}+{frac2}=")
    ans = (f"{sum}")
    
    return [q, ans]

def fraction_addition_hard():

    #Generates a fraction addition problem (#16)
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    frac1 = Fraction(min(num1,num2), max(num1,num2))
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    frac2 = Fraction(min(num1,num2), max(num1,num2))
    sum = (frac1+frac2)
    q = (f"{frac1}+{frac2}=")
    ans = (f"{sum}")
    
    return [q, ans]

def fraction_reduction():

    #Generates a fraction reduction problem (#17)
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(2, 5)
    frac1 = Fraction(min(num1,num2), max(num1,num2))
    q = (f"Reduce {num3*min(num1,num2)}/{num3*max(num1,num2)} to it's lowest terms.")
    ans = (f"{frac1}")
        
    return [q, ans]

def improper_to_mixed():

    #Generates an improper fraction and solves for the mixed number form (#18)
    num1 = random.randint(10, 20)
    num2 = random.randint(2, 9)
    frac1 = Fraction(num1, num2)
    whole_portion = num1//num2
    remainder = num1%num2
    q = (f"{num1}/{num2} is equal to what mixed number?")
    if remainder == 0:
        #print(f"{num1}/{num2} is equal to {whole_portion}")
        ans = (f"{whole_portion}")
    else:
        #print(f"{num1}/{num2} is equal to {whole_portion} and {remainder}/{num2}")
        ans = (f"{whole_portion} and {remainder}/{num2}")
        
    return [q, ans]

def find_smallest_fraction():

    #Generates 4 fractions and evaulates the smallest (#19)
    frac_list = []
    for i in range(4):
        num1 = random.randint(1, 9)
        num2 = random.randint(2, 9)
        frac = Fraction(min(num1,num2), max(num1,num2))
        frac_list.append(frac)
        #print(f"{frac_list[i]}")
    q = (f"Which is smallest out of {frac_list[0]}, {frac_list[1]}, {frac_list[2]}, {frac_list[3]}?")
    #print(min(frac_list))
    ans = (f"{min(frac_list)}")
        
    return [q, ans]

def fraction_addition_word():

    #Generates a fraction addition problem (#25)
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    frac1 = Fraction(min(num1,num2), max(num1,num2))
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    frac2 = Fraction(min(num1,num2), max(num1,num2))
    sum = (frac1+frac2)
    q = (f"It is {frac1} miles from b1 to b2, and {frac2} miles from b2 to b3. How many miles from b1 to b3?")
    ans = f"{sum}"
    
    return [q, ans]

def volume_box():
    
    #Generates a volume word problem (#26)
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    product = (num1*num2*num3)
    q = (f"How many cubic feet of sand is needed to fill a {num1}x{num2}x{num3} box?")
    ans = product
    
    return [q, ans]


def percent_increase():

    #Generates a percent increase word problem (#29)
    num1 = random.randint(10, 45)
    percent_increase = random.randint(10, 45)
    multiplier = round(1.0 + (percent_increase/100.0), 2)
    q = (f"Last year Company A made sales worth {num1} million. They're projected to make {percent_increase}% more this year. What is this years projected sales?")
    projected_sales = round(num1*multiplier, 2)
    ans = (f"{projected_sales} million ")
    
    return [q, ans]


def algebra_1_step():

    #Generates a simple one-step algebra problem (#30)
    num1 = 0
    while (num1 == 0):
        num1 = random.randint(-9, 9)
    num2 = random.randint(-25, 25)
    answer = (num2-num1)
    if (num1 > 0):
        q = (f"x + {num1} = {num2}")
    else:
        q = (f"x {num1} = {num2}")
    
    return [q, answer]

def algebra_2_step():
    
    #Generates a simple two-step algebra problem with 2 variables (#31)
    num1 = 0
    while (num1 == 0):
        num1 = random.randint(-9, 9)
    y = random.randint(2, 4)
    factor = (random.randint(1, 5))
    num2 = (factor*y)+num1
    answer = (factor)
    if (num1 > 0):
        q = (f"y*x + {num1} = {num2}; where y = {y}")
    else:
        q = (f"y*x {num1} = {num2}; where y = {y}")
    
    return [q, answer]

def algebra_2_step_2_var():

    #Generates a simple two-step algebra problem with 2 variables (#32)
    num1 = 0
    while (num1 == 0):
        num1 = random.randint(-9, 9)
    y = random.randint(2, 4)
    num2 = random.randint(2, 12)
    answer = (y*num2)-num1
    if (num1 > 0):
        q = (f"(x + {num1})/y = {num2}; where y = {y}")
    else:
        q = (f"(x {num1})/y = {num2}; where y = {y}")
    ans = (answer)
        
    return [q, ans]

def pythagorean_theorem():

    #Generates a simple pythagorean theorem problem (#33)
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    q = (f"(x^2)+(y^2) = {(x**2)+(y**2)}; where y = {y}")
    ans = x
    
    return [q, ans]


def percent_decrease_word():

    #Generates a percent decrease word problem (#34)
    num1 = random.randint(20000, 45000)
    percent_decrease = random.randint(5, 20)
    multiplier = round(1.0 - (percent_decrease/100.0), 2)
    name = random.choice(names)
    q = (f"{name} is purchasing a car at a {percent_decrease}% discount. If the sticker price is ${num1}, what is the price that {name} pays?")
    price_paid = round(num1*multiplier, 2)
    ans = (f"${price_paid}")

    return [q, ans]

def surface_area_t1():

    #Generates a surface area problem (#36)
    num1 = random.randint(2, 6)*2
    num2 = random.randint(2, 6)*2
    area = num1*num2
    q = (f"How many 2 sq. in. tiles will fit on a rectangle that is {num1} in wide by {num2} in long?")
    ans = (area/4)

    return [q, ans]

def surface_area_t2():

    #Generates a surface area problem (#39)
    num = random.randint(3, 12)
    q = f"What is the surface area of a {num}' cube?"
    ans = (num*num*6)

    return [q, ans]

def hypoteneuse():

    #Generates a hypoteneuse word problem (#40)
    num1 = random.randint(2, 9)
    total = round((num1)*1.41, 2)
    name = random.choice(names)
    q = (f"{name} is fitting pipe and must calculate the center to center distance of two 45s for an offset. If the rise is {num1} inches, what is the center to center distance?")
    ans = total

    return [q, ans]

def ratio_word():

    #Generates a multiplication word problem with multiple variables (#41)
    denom = random.randint(2, 4)
    frac1 = Fraction(1, denom)
    cups = random.randint(1, 9)
    answer = denom*cups
    q = (f"If each loaf of bread takes {frac1} cup of flour, how many loafs can be made with {cups} cups?")
    ans = (answer)
        
    return [q, ans]

def purchase_tax():

    #Generates 3 dollar amounts then adds tax (#42)
    item1_price = round(random.uniform(1, 3), 2)
    item2_price = round(random.uniform(5, 7), 2)
    item3_price = round(random.uniform(0, 2), 2)        
    tax = round(random.uniform(3, 12)) 
    name = random.choice(names)
    q = (f"{name} gets a soup at ${item1_price}, a sandwich at ${item2_price}, and a soda at ${item3_price}. The bill included {tax}% sales tax. What's the total bill?")
    sum = round(item3_price+item2_price+item1_price, 2)
    total = sum + round(sum*(tax/100.0), 2)
    ans = (f"${total}")
        
    return [q, ans]

def percent_markup():

    #Generates a percent increase word problem (#43)
    list_price = random.randint(3, 7)
    price_increase = random.randint(1, 3)
    name = random.choice(names)
    q = (f"{name} bought a car for ${list_price*1000}, then sold it for ${(list_price+price_increase)*1000}. What was the percent markup?")
    percent_increase = round((price_increase/list_price)*100, 2)
    ans = (f"{percent_increase}%")
        
    return [q, ans]

def percent_decrease():
        
    #Generates a percent decrease word problem (#44)
    list_price = random.randint(35, 45)
    sale_price = random.randint(20, 34)
    q = (f"A poster has a list price of ${list_price}, it was on sale for ${sale_price}. What percentage was the discount?")
    dollar_diff = (list_price - sale_price)/1.0
    percent_discount = round((dollar_diff/list_price)*100, 2)
    ans = (f"{percent_discount}%")
        
    return [q, ans]

def volume_cube():
        
    #Generates a volume of a cube problem (#45)
    num = random.randint(2, 5)
    q = (f"What is the volume of a {num}' cube?")
    ans = (num*num*num)
        
    return [q, ans]

def percent_product():
        
    #Generates a percent product problem (#46)
    num1 = random.randint(20, 50)
    percent = random.randint(5, 20)
    q = (f"What is {percent}% of ${num1}?")
    product = round(num1*(percent/100.0), 2)
    ans = (f"${product}")
        
    return [q, ans]

def evaluate_smallest_fraction():

    #Generates 4 fractions and evaulates the smallest (#47)
    frac_list = []
    for i in range(4):
        num1 = random.randint(1, 12)
        num2 = random.randint(2, 9)
        frac = Fraction(min(num1,num2), max(num1,num2))
        frac_list.append(frac)
    q = (f"Which is smallest out of {frac_list[0]}, {frac_list[1]}, {frac_list[2]}, {frac_list[3]}?")
    ans = (f"{min(frac_list)}")
        
    return [q, ans]

def fraction_division():

   #Generates a fraction division problem (#49)
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    frac1 = Fraction(min(num1,num2), max(num1,num2))
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    frac2 = Fraction(min(num1,num2), max(num1,num2))
    quotient = (frac1/frac2)
    q = (f"What is {frac1} divided by {frac2}?")
    ans = (f"{quotient}")
        
    return [q, ans]

def factoring_trinomials():

   #Generates a trinomial factoring problem (#49)
    num1 = 0
    while (num1 == 0):
        num1 = random.randint(-9, 9)
    num2 = 0
    while (num2 == 0):
        num2 = random.randint(-9, 9)
    if (num1 < num2):
        temp = num1
        num1 = num2 
        num2 = temp
    if (num1 > 0 and num2 > 0):
        q = (f"Factor: x^2+{num1+num2}x+{num1*num2}")
        ans = (f"(x+{num1})(x+{num2})")
    elif (num1 < 0 and num2 < 0):
        q = (f"Factor: x^2{num1+num2}x+{num1*num2}")
        ans = (f"(x{num1})(x{num2})")
    elif ((num1+num2) < 0):
        q = (f"Factor: x^2{num1+num2}x{num1*num2}")
        ans = (f"(x+{num1})(x{num2})")
    else:
        q = (f"Factor: x^2+{num1+num2}x{num1*num2}")
        ans = (f"(x+{num1})(x{num2})")
    return [q, ans, num1, num2]
