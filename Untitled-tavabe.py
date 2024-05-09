def mostatil(tool,arz):
    return tool*arz

def dayere(shoa):
    return shoa*shoa*3.14

def is_even(adad):
    if adad%2 == 0:
        return True
    else :
        return False

def main():
    adad = int(input('adad ra vared knid: '))
    if is_even(adad):
        print(dayere(adad))
    else :
        print(mostatil(adad,5))
    
main()
