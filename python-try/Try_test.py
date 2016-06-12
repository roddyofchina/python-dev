try:
    InputNumber = int(raw_input('input a number:'))
    if InputNumber > 10:
        print "input a number gt 10!!!"
    else:
        print "input a number lt 10!!!!"

except (ValueError,IndexError),error:
    print "ERROR!!!",error

else:
    print "OK"

finally:
    print "end"
