"""
Check if a value is a natural number.

@param value: Value to check
@param includeZero: Whether or not to consider 0 a natural number.
@return: True or False
"""
def isNaturalNumber(value, includeZero=False):
	if( includeZero == True ):
		return int(value) >= 0
	else:
		return int(value) >= 1

