from z3 import *

def func(i1, i2, i3, i4,i6, G1, G2,G3,G4, GG1, GG2,key1,key2,key3,key4,key5,key6,key7):
    op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11,op12,op13,op14,op15,op16 = Ints('op1 op2 op3 op4 op5 op6 op7 op8 op9 op10 op11 op12 op13 op14 op15 op16')
    op17,op18,op19,op20,op21,op22,op23,op24,op25,op26,op27,op28 = Ints('op17 op18 op19 op20 op21 op22 op23 op24 op25 op26 op27 op28')
    o1,o2,o3,o4=Ints('o1 o2 o3 o4')
    t1,t2=Bools('t1 t2')

    op1 = GG1 * i1
    op2 = GG2 * i2
    op3 = G1 * i2
    op4 = G2 * i1

    t1=If(G1>10,True,False)

    op5=If(t1,G1*i3,i3*i4)
    op5=If(t1,op5 + GG1,op5)
    op6=If(t1,op5 - op4,op5-op3)

    t2=Xor((op5<op4),key7)

    op6=If(t2,G2*i4,op6)
    op6=If(t2,op6-i3,op6)
    op17=If(t2,op6 - G2,op2 - op4)
    op2=If(t2,op2,op4 - op17)
    op17=If(t2,op17,op17 - op2)

    op7 = G1 * i4
    op8 = G2 * i3

    op9 = op1 + op2
    op10 = op3 + op4
    op11 = op4 + op6
    op12 = op7 + op8

    op13 = op11 + G1
    o1 = op13 + key1
    op14 = i6 + op12
    o2 = op14 / key2
    op15 = G1 * op14
    op16 = op13 * G2

    op17=If(op13==op14,op17 * op11,op17)
    op14=If(op13==op14,op14 - op17,op13 * G1)
    op15=If(op13 == op14,op15 + op17,op15)

    op18 = op14 * G2
    op19 = op15 * op16
    op20 = op17 + op18
    op21 = G1 * op20
    op22 = If(key6 ,op19 * G2,op14 * G1)
    op23 = op19 * G1
    op24 = If(key5 ,op20 + G1,op20 * G2)
    op25 = op21 + op22
    op26 = op23 + op24
    op27 = op9 + op25+key3
    o3 = op27
    op28 = op10 + op26
    o4 = op28 +key4

    return o1,o2,o3,o4

if __name__ == "__main__":
    i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2 = Ints("i1 i2 i3 i4 i6 G1 G2 G3 G4 GG1 GG2")
    key1_1, key2_1, key3_1, key4_1 = Ints("key1_1 key2_1 key3_1 key4_1")
    key5_1, key6_1, key7_1 = Bools("key5_1 key6_1 key7_1")
    key1_2, key2_2, key3_2, key4_2 = Ints("key1_2 key2_2 key3_2 key4_2")
    key5_2, key6_2, key7_2 = Bools("key5_2 key6_2 key7_2")
    out1, out2, out3, out4, out5, out6, out7, out8 = Ints("out1 out2 out3 out4 out5 out6 out7 out8")

    s = Solver()

    #Adding constraints for finding key1 and key7 related to output1 
    s.add(out1 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, key1_1, key2_1, key3_1, key4_1, key5_1, key6_1, key7_1)[0])
    s.add(out2 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, key1_2, key2_2, key3_2, key4_2, key5_2, key6_2, key7_2)[0])

    s.add(224238 == func(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, key1_1, key2_1, key3_1, key4_1, key5_1, key6_1, key7_1)[0])
    s.add(224238 == func(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, key1_2, key2_2, key3_2, key4_2, key5_2, key6_2, key7_2)[0])

    s.add(176397 == func(-218764, -225683, 139603, 218709, 0, -134550, 762, 0, 0, 18616885482, 0, key1_1, key2_1, key3_1, key4_1, key5_1, key6_1, key7_1)[0])
    s.add(176397 == func(-218764, -225683, 139603, 218709, 0, -134550, 762, 0, 0, 18616885482, 0, key1_2, key2_2, key3_2, key4_2, key5_2, key6_2, key7_2)[0])

    #Adding constraints for finding key2 related to output2 
    s.add(key2_1 != 0)  # adding this constraint because of this line o2 = op14 / key2
    s.add(key2_2 != 0)

    s.add(out3 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, 224238, key2_1, key3_1, key4_1, key5_1, key6_1, False)[1])
    s.add(out4 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, 224238, key2_2, key3_2, key4_2, key5_2, key6_2, False)[1])

    s.add(1 == func(0, 0, 0, 0, 6, -224238, 0, 0, 0, 0, 0, 224238, key2_1, key3_1, key4_1, key5_1, key6_1, False)[1])
    s.add(1 == func(0, 0, 0, 0, 6, -224238, 0, 0, 0, 0, 0, 224238, key2_2, key3_2, key4_2, key5_2, key6_2, False)[1])

    s.add(1 == func(0, 0, 0, 0, 4, -224238, 0, 0, 0, 0, 0, 224238, key2_1, key3_1, key4_1, key5_1, key6_1, False)[1])
    s.add(1 == func(0, 0, 0, 0, 4, -224238, 0, 0, 0, 0, 0, 224238, key2_2, key3_2, key4_2, key5_2, key6_2, False)[1])
    
    #Adding constraints for finding key3 and key6 related to output3 
    s.add(out5 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, 224238, 4, key3_1, key4_1, key5_1, key6_1, False)[2])
    s.add(out6 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, 224238, 4, key3_2, key4_2, key5_2, key6_2, False)[2])

    s.add(-43224 == func(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224238, 4, key3_1, key4_1, key5_1, key6_1, False)[2])
    s.add(-43224 == func(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 224238, 4, key3_2, key4_2, key5_2, key6_2, False)[2])
    
    s.add(-43226 == func(-1, -1, 1, 0, 0, 1, -1, 0, 0, 1, -1, 224238, 4, key3_1, key4_1, key5_1, key6_1, False)[2])
    s.add(-43226 == func(-1, -1, 1, 0, 0, 1, -1, 0, 0, 1, -1, 224238, 4, key3_2, key4_2, key5_2, key6_2, False)[2])

    #Adding constraints for finding key4 and key5 related to output4 
    s.add(out7 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, 224238, 4, -43224, key4_1, key5_1, True, False)[3])
    s.add(out8 == func(i1, i2, i3, i4, i6, G1, G2, G3, G4, GG1, GG2, 224238, 4, -43224, key4_2, key5_2, True, False)[3])

    s.add(26729 == func(-2, -1, 1, 10, -113, 11, -2, 0, 0, -9, 3, 224238, 4, -43224, key4_1, key5_1, True, False)[3])
    s.add(26729 == func(-2, -1, 1, 10, -113, 11, -2, 0, 0, -9, 3, 224238, 4, -43224, key4_2, key5_2, True, False)[3])
    
    s.add(33996 == func(0, 2, 3, 1, 1, 3, -2, 0, 0, 0, 29, 224238, 4, -43224, key4_1, key5_1, True, False)[3])
    s.add(33996 == func(0, 2, 3, 1, 1, 3, -2, 0, 0, 0, 29, 224238, 4, -43224, key4_2, key5_2, True , False)[3])


    s.add(out1 == out2)
    s.add(out3 == out4)
    s.add(out5 == out6)
    s.add(out7 == out8)
   

    if s.check() == sat:
        print(s.model())
    else:
        print("unsat")


#Keys obtained after SAT attack
#key1 = 224238
#key2 = 4
#key3 = -43224
#key4 = 34222
#key5 = False
#key6 = True
#key7 = False