print """Default configuration of this machine is as follows :- 1st-->5(r1) , 2nd-->6(r2) , 3rd-->7(r3) \n
Enter the message and settings in capital letters and the message should NOT contain spaces"""
#r1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   #5 Spokes
#r2 = "BACEDFHGIKJLNMOQPRTSUWVXZY"   #6 Spokes
#r3 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"   #7 Spokes

r_input = raw_input("Enter the setting : ")
rotors = {"5" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ","6" : "BACEDFHGIKJLNMOQPRTSUWVXZY","7" : "ZYXWVUTSRQPONMLKJIHGFEDCBA"}
r1 = rotors[r_input[0]]
r2 = rotors[r_input[1]]
r3 = rotors[r_input[2]]
s1 = r_input[3]
s2 = r_input[4]
s3 = r_input[5]

def encryption(msg):
    emsg = []
    for i in range(0,26):
        if s1==r1[i]:
            for m in range(0,len(msg)):
                    if m%2 == 0:
                            for n in range(0,26):
                                    if msg[m] == r1[n]:
                                            diff = n-i
                                            #print diff
                                            for p in range(0,26):
                                                    if s3==r3[p]:
                                                            #print p
                                                            encrypted_msg = p+diff
                                                            #print encrypted_msg
                                                            if encrypted_msg >= 26:
                                                                    emsg.append(r3[encrypted_msg-26])
                                                            else:
                                                                    emsg.append(r3[encrypted_msg])
                                                    else:
                                                         pass
                                    else:
                                            pass
                    else:
                            for a in range(0,26):
                                    if msg[m] == r1[a]:
                                            diff = a-i
                                            #print diff
                                            for b in range(0,26):
                                                    if s2==r2[b]:
                                                            #print b
                                                            encrypted_msg = b-diff
                                                            #print encrypted_msg
                                                            if encrypted_msg >= 26:
                                                                    emsg.append(r2[encrypted_msg-26])
                                                            else:
                                                                    emsg.append(r2[encrypted_msg])
                                                    else:
                                                         pass
                                    else:
                                            pass
        else:
                pass
    print ''.join(emsg)

    
def decryption(msg):
    dmsg = []
    for i in range(0,26):
        if s3==r3[i]:
            for m in range(0,len(msg)):
                    if m%2 == 0:
                            for n in range(0,26):
                                    if msg[m] == r3[n]:
                                            diff = n-i
                                            #print diff
                                            for p in range(0,26):
                                                    if s1==r1[p]:
                                                            #print p
                                                            decrypted_msg = p+diff
                                                            #print encrypted_msg
                                                            if decrypted_msg >= 26:
                                                                    dmsg.append(r1[decrypted_msg-26])
                                                            else:
                                                                    dmsg.append(r1[decrypted_msg])
                                                    else:
                                                         pass
                                    else:
                                            pass
                    else:
                            for z in range(0,26):
                                if s2==r2[z]:
                                    for a in range(0,26):
                                            if msg[m] == r2[a]:
                                                    diff = a-z
                                                    #print diff
                                                    for b in range(0,26):
                                                            if s1==r1[b]:
                                                                    #print b
                                                                    decrypted_msg = b-diff
                                                                    #print decrypted_msg
                                                                    if decrypted_msg >= 26:
                                                                            dmsg.append(r1[decrypted_msg-26])
                                                                    else:
                                                                            dmsg.append(r1[decrypted_msg])
                                                            else:
                                                                 pass
                                            else:
                                                    pass
                                else:
                                    pass
        else:
                pass
    print ''.join(dmsg)
encryption("ATTACKATDAWN")
