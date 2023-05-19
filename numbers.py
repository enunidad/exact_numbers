class Fraction:
    '''
    The Fraction class
    This class adds, subtracts, multiplies, divides, and does comparisons
    with others of its class but by default will always deal with numerators
    and denominators, never the decimal representation of a fraction, unless
    stated by the user
    '''
    def __init__(self, numerator, denominator):
        '''
        Initialization method of class Fraction
        Parameters
        ----------
            numerator: int
                        the numerator of the fraction
            denominator: int
                        the denominator of the fraction
        
        Returns:
        ----------
            None
        '''
        self.numerator = numerator
        self.denominator = denominator
        assert self.denominator != 0, 'The denominator of a fraction cannot be zero'
        assert isinstance(self.numerator, int), 'The numerator of a fraction must be an integer'
        assert isinstance(self.denominator, int), 'The denominator of a fraction must be an integer'
        self.simplify()
    
    def __repr__(self):
        '''
        The string representation of class Fraction
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: str
                        the string representation of this class
        '''
        to_return = f'Fraction(numerator={self.numerator}, denominator={self.denominator})'
        return to_return
    
    def __str__(self):
        '''
        The string representation of the fraction
        
        Parameters:
        ----------
            None
        
        Returns
        ----------
            to_return: str
                        the string representation of the fraction
        '''
        to_return = f'{self.numerator}/{self.denominator}'
        return to_return
    
    @property
    def is_negative(self):
        '''
        A boolean to express if the fraction is less than 0
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: bool
                        True if this Fraction is less than 0, False otherwise
        '''
        to_return = (-1)**(int(self.numerator*self.denominator < 0))
        return to_return
    
    @property
    def decimal(self):
        '''
        Returns the decimal representation of this fraction.
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: float
        '''
        to_return = self.numerator/self.denominator
        return to_return
    
    def simplify(self):
        '''
        Fractions must always be in lowest terms.
        Resets the numerator and denominator attributes to their
        lowest terms.
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            None
        '''
        import math
        g = math.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = self.is_negative*int(abs(self.numerator)/g)
        self.denominator = int(abs(self.denominator)/g)
        
    def __add__(self, other):
        '''
        The addition function for class Fraction
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: Fraction
                        the result of the addition
        '''
        new_denom = self.denominator * other.denominator
        new_num = other.denominator*self.numerator + self.denominator*other.numerator
        to_return = Fraction(new_num, new_denom)
        return to_return
    
    def __sub__(self, other):
        '''
        The subtraction function for class Fraction
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: Fraction
                        the result of the subtraction
        '''
        new_denom = self.denominator*other.denominator
        new_num = other.denominator*self.numerator - self.denominator*other.numerator
        to_return = Fraction(new_num, new_denom)
        return to_return
    
    def __mul__(self, other):
        '''
        The multiplication function for class Fraction
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: Fraction
                        the result of the multiplication
        '''
        new_denom = self.denominator*other.denominator
        new_num = self.numerator*other.numerator
        to_return = Fraction(new_num, new_denom)
        return to_return
    
    def __truediv__(self, other):
        '''
        The division function for class Fraction
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: Fraction
                        the result of the division
        '''
        new_num = self.numerator*other.denominator
        new_denom = self.denominator*other.numerator
        to_return = Fraction(new_num, new_denom)
        return to_return
    
    def __eq__(self, other):
        '''
        Checks if two Fractions are equal
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: bool
                        True if the two Fractions are the same, False otherwise
        '''
        to_return = self.numerator==other.numerator and self.denominator==other.denominator
        return to_return
    
    def __lt__(self, other):
        '''
        Checks if the left Fraction is less than the right Fraction
        
        Parameters
        ----------
            None
        
        Returns:
            to_return: bool
                        True if the left Fraction is smaller than the right Fraction, False otherwise
        '''
        to_return = self.numerator*other.denominator < other.numerator*self.denominator
        return to_return
    
    def __gt__(self, other):
        '''
        Checks if the left Fraction is greater than the right Fraction
        
        Parameters
        ----------
            None
        
        Returns
        ----------
            to_return: bool
                        Tru is the left Fraction is bigger than the right Fraction, False otherwise
        '''
        to_return = not self.__eq__(other) and not self.__lt__(other)
        return to_return

class Integer(Fraction):
    '''
    Integers are basically fractions, but their denominators are always 1.
    This class is fairly simple as it can do everything a Fraction can, but always 
    with the denominator equal to 1
    '''
    def __init__(self, n):
        '''
        Initializes the parent class Fraction with a denominator 1.
        Creating this class only requires the numerator
        
        Parameters
        ----------
            n: int
                The integer to be stored
        
        Returns
        ----------
            None
        '''
        super().__init__(n, 1)

class Float(Fraction):
    '''
    A Float is simply a fraction in decimal form.
    This class will estimate the best it can the fraction equivalent
    of the given decimal number.
    '''
    def __init__(self, n, eps=1e-8):
        '''
        Initializes the Fraction class with the found approximation
        
        Parameters
        ----------
            n: float
                The floating point number ot be created as a Fraction
            eps: float(optional)
                 The accuracy of the approximation
                 Default: 1e-8 or 0.00000001
        
        Returns
        ----------
            None
        '''
        whole = int(n//1)
        part = self.farey(n-w, eps)
        new_int = Integer(whole)
        new_frac = new_int + part
        super().__init__(new_frac.numerator, new_frac.denominator)
    
    def farey(self, n, eps=1e-8):
        '''
        The Farey algorithm allows for "better" approximations. A binary search
        would always return fractions with denominators in powers of 2, this way
        the Fraction looks more "natural".
        
        Parameters
        ----------
            n: float
                n is the fractional portion of the number given. n should be between 1 and 0
            eps: float
                The accuracy of the approximation
                Default: 1e-8 or 0.00000001
        
        Returns:
          test: Fraction
                the approximation of the decimal portion of the float accurate to eps                
        '''
        assert n >= 0, 'The parameter n must be greater than 0'
        assert n < 1, 'The parameter n must be less than 1
        if n == 0 or n == 1:
            return Integer(n)
        left = Fraction(0, 1)
        right = Fraction(1, 1)
        test = Fraction(left.numerator+right.numerator, left.denominator+right.denominator)
        while abs(n-test.decimal) > eps:
            if n > test.decimal:
                left = test
            else:
                right = test
            test = Fraction(left.numerator+right.numerator, left.denominator+right.denominator)
        return test
