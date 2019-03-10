sh, sm = map(int, input().split(':'))
eh, em = map(int, input().split(':'))
r = ((sh*60 + sm) + (eh*60+em))//2
print('{:02d}:{:02d}'.format(r//60, r%60))
