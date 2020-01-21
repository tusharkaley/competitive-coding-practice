def lattice(ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay

    # rotate 90
    rx = dy
    ry = -dx

    # reduce
    gc = abs(gcd(rx, ry))
    rx /= gc
    ry /= gc
    return (bx + rx, by + ry)
    
def gcd(x, y):
    if y == 0:
        return x 
    else:
        return gcd(y, x % y);
    
if __name__ == '__main__':
    print(gcd(15,12))
    print(lattice(-1,3,3,1))