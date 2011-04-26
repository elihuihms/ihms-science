""" A library of often-used simple mathematical bits.
	Included functions:
	isNumber()
	frange()
"""

## {{{ http://code.activestate.com/recipes/66472/ (r1)
def frange(start, end=None, inc=None):
    """frange( start, end, step ) A range function that can accept float increments, analogous to range()"""

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L
## end of http://code.activestate.com/recipes/66472/ }}}

## http://stackoverflow.com/questions/354038/checking-if-string-is-a-number-python
def isNumber(s):
	"""isNumber( string ) : determines if passed <string> is convertable to a number """
	try:
		float (s)
		return True
	except ValueError:
		return False