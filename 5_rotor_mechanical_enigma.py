print """Default configuration of this machine is as follows :- r1 rotor takes the input and r5 rotor gives the first output,then r4,r3,r2 and again it repeats from r5 \n
Enter the message and settings in capital letters and the message should NOT contain spaces"""
r1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r2 = "AITDNFMHSGQKPVWYZRXBLCOJUE"
r3 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
r4 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
r5 = "ADCBEHGFILKJMPNOQTSRUXWVZY"
s1 = raw_input("Enter setting for 1st(input) rotor: ")
s2 = raw_input("Enter setting for 2nd rotor: ")
s3 = raw_input("Enter setting for 3rd rotor: ")
s4 = raw_input("Enter setting for 4th rotor: ")
s5 = raw_input("Enter setting for 5th rotor: ")
def encryption(msg):
    emsg = []
    for i in range(0,26):
        if s1==r1[i]:
            for m in range(0,len(msg)):
                    if m in range(0,len(msg),4):
                            for n in range(0,26):
                                    if msg[m] == r1[n]:
                                            diff = n-i
                                            #print diff
                                            for p in range(0,26):
                                                    if s5==r5[p]:
                                                            #print p
                                                            encrypted_msg = p+diff
                                                            #print encrypted_msg
                                                            if encrypted_msg >= 26:
                                                                    emsg.append(r5[encrypted_msg-26])
                                                            else:
                                                                    emsg.append(r5[encrypted_msg])
                                                    else:
                                                         pass
                                    else:
                                            pass
                    elif m in range(1,len(msg),4):
                            for a in range(0,26):
                                    if msg[m] == r1[a]:
                                            diff = a-i
                                            #print diff
                                            for b in range(0,26):
                                                    if s4==r4[b]:
                                                            #print b
                                                            encrypted_msg = b-diff
                                                            #print encrypted_msg
                                                            if encrypted_msg >= 26:
                                                                    emsg.append(r4[encrypted_msg-26])
                                                            else:
                                                                    emsg.append(r4[encrypted_msg])
                                                    else:
                                                         pass
                                    else:
                                            pass

                    elif m in range(2,len(msg),4):
                            for a in range(0,26):
                                    if msg[m] == r1[a]:
                                            diff = a-i
                                            #print diff
                                            for b in range(0,26):
                                                    if s3==r3[b]:
                                                            #print b
                                                            encrypted_msg = b+diff
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
        if s5==r5[i]:
            for m in range(0,len(msg)):
                    if m in range(0,len(msg),4):
                            for n in range(0,26):
                                    if msg[m] == r5[n]:
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
                    elif m in range(1,len(msg),4):
                            for z in range(0,26):
                                if s4==r4[z]:
                                    for a in range(0,26):
                                            if msg[m] == r4[a]:
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
                    elif m in range(2,len(msg),4):
                            for z in range(0,26):
                                if s3==r3[z]:
                                    for a in range(0,26):
                                            if msg[m] == r3[a]:
                                                    diff = a-z
                                                    #print diff
                                                    for b in range(0,26):
                                                            if s1==r1[b]:
                                                                    #print b
                                                                    decrypted_msg = b+diff
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
decryption("ATTACKATDAWN")
