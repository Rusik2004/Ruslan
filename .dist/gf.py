def double_score(mylist):
    for k in range(len(mylist)):
        mylist[k] = 2 * mylist[k] 

if __name__ == '__main__':
    scorelist = [78, 56, 67, 95, 82]
    double_score(scorelist)
    print('scorelist =', scorelist)
