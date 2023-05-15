import math

ang = float(input("\n Digite o angulo em graus: "))
rang = ang * math.pi / 180 
if ((rang > math.pi/2 and rang <= math.pi) or (rang > 3 * math.pi / 2 and rang <= 2 * math.pi)):
    print ("\n Seno: ", math.sin(rang))
else:
    print ("\n Co-seno: ", math.cos(rang))
     
