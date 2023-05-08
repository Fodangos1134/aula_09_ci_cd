import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sub():
    # given two numbers
    numero1 = 2
    numero2 = 5

    #when we calculate subtraction
    output = methods.subtraction(numero1, numero2)

    #then show the subtraction
    assert output == -3

def test_add():
    # given two numbers
    numero1 = 2
    numero2 = 5

    #when we calculate addition
    output = methods.addition(numero1, numero2)
    #then show the addition
    assert output == 7

def test_mult():
    # given two numbers
    numero1 = 2
    numero2 = 5

    #when we calculate multiplication
    output = methods.mult(numero1, numero2)

    #then show the multiplication
    assert output == 10

def test_divide(numero1 = 2, numero2 = 5):
    # given two numbers
    numero1 = 2
    numero2 = 5

    #when we calculate multiplication
    output = methods.divide(numero1, numero2)

    #then show the multiplication
    assert output == 0.4
        
