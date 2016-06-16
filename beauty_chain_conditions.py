mark = 75

# from
if   mark >=  0 and mark < 50: print 'failed'
elif mark >= 50 and mark < 60: print 'grade C'
elif mark >= 60 and mark < 75: print 'grade B'
else:                          print 'grade A'

# to chain conditions
if    0 <= mark < 50: print 'failed'
elif 50 <= mark < 60: print 'grade C'
elif 60 <= mark < 75: print 'grade B'
else:                 print 'grade A'
