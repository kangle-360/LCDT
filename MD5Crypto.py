# -*- coding: utf-8 -*-
global T_count  
def MD5(string):
    import math
    if string == '':
        return 
	#链接常量以及单位常量
    A = '0x67452301'
    B = '0xefcdab89'
    C = '0x98badcfe'
    D = '0x10325476'
	
    SINGLE_BIT = '0x80'
    BITS = 8
    BLOCK_SIZE = 512
    MOD_SIZE = 448
    APP_SIZE = 64

    #线性函数
    F = lambda x,y,z:((x&y)|((~x)&z))  
    G = lambda x,y,z:((x&z)|(y&(~z)))  
    H = lambda x,y,z:(x^y^z)  
    I = lambda x,y,z:(y^(x|(~z)))  
    ROTATE_LEFT = lambda x,n:(((x<<n)|(x>>(32-n)))&(0xffffffff))
	#每轮循环左移的位数
    shi_1 = (7,12,17,22) * 4
    shi_2 = (5,9,14,20) * 4
    shi_3 = (4,11,16,23) * 4
    shi_4 = (6,10,15,21) * 4 
    
    #每轮mj的次序
    m_1 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    m_2 = (1,6,11,0,5,10,15,4,9,14,3,8,13,2,7,12)
    m_3 = (5,8,11,14,1,4,7,10,13,0,3,6,9,12,15,2)
    m_4 = (0,7,14,5,12,3,10,1,8,15,6,13,4,11,2,9)  
	
    
    def reverse_hex(hex_str):  
        hex_str = hex_str[2:]  
        hex_str_list = []  
        
        for i in range(0,len(hex_str),2):  
            hex_str_list.append(hex_str[i:i+2])  
        hex_str_list.reverse()  
        hex_str_result = '0x' + ''.join(hex_str_list)  
        
        return hex_str_result  
    

    def add_padding(string):
        mes_length = len(string)*BITS
        ascii_list = list(map(hex,map(ord,list(string))))
        ascii_list.append(SINGLE_BIT)
        
        while (len(ascii_list) * BITS + APP_SIZE) % BLOCK_SIZE != 0:
            ascii_list.append('0x00')
        append_message_0x = hex(mes_length)[2:]
        append_message_0x = '0x' + append_message_0x.rjust(16,'0') 
        append_message = reverse_hex(append_message_0x)[2:]  
        append_tempt = []

        for i in range(0,len(append_message),2):
            append_tempt.append('0x' + append_message[i:i+2])
        ascii_list.extend(append_tempt)
        return ascii_list
        
 
    def T(i):
        result = (int(4294967296*abs(math.sin(i))))&0xffffffff  
        return result
    
    def show_result(f_list):  
        result = ''  
        f_list1 = [0]*4  
        for i in f_list:  
            f_list1[f_list.index(i)] = reverse_hex(i)[2:]  
            result = result + f_list1[f_list.index(i)]  
        return result  
    

    def genM16(order,ascii_list,f_offset):  
        ii = 0  
        m16 = [0]*16
        f_offset = f_offset*64
        for i in order:  
            i = i*4   
            m16[ii] = '0x'+''.join((ascii_list[i+f_offset]+ascii_list[i+1+f_offset]+ascii_list[i+2+f_offset]+ascii_list[i+3+f_offset]).split('0x')) 
            ii += 1 
        for c in m16:  
            ind = m16.index(c)  
            m16[ind] = reverse_hex(c)
        return m16  


    def shift(shift_list):  
        shift_list = [shift_list[3],shift_list[0],shift_list[1],shift_list[2]]  
        return shift_list

    
    def fun(fun_list,f,m,shi): 
        count = 0
        global T_count 
        while count < 16 :  
            xx = int(fun_list[0],16)+f(int(fun_list[1],16),int(fun_list[2],16),int(fun_list[3],16))+ T(T_count) + int(m[count],16)
            xx = xx&0xffffffff
            ll = ROTATE_LEFT(xx,shi[count])
            fun_list[0]= hex((int(fun_list[1],16) + ll)&(0xffffffff)) 
            fun_list = shift(fun_list) 
            count += 1
            T_count += 1 
        return fun_list 
    
    
    abcd_list = [A,B,C,D]
    abcd_tempt = [0] * 4
    T_count = 1
    
    fun_string = add_padding(string)

    for i in range(0,int(len(fun_string) / 64)):
        global T_count
        aa,bb,cc,dd = abcd_list

        order_1 = genM16(m_1,fun_string,i)
        order_2 = genM16(m_2,fun_string,i)
        order_3 = genM16(m_3,fun_string,i)
        order_4 = genM16(m_4,fun_string,i)

        abcd_list = fun(abcd_list,F,order_1,shi_1)  
        abcd_list = fun(abcd_list,G,order_2,shi_2)
        abcd_list = fun(abcd_list,H,order_3,shi_3) 
        abcd_list = fun(abcd_list,I,order_4,shi_4)     

        if i == ( int(len(fun_string) / 64) - 1 ):
            abcd_tempt = [abcd_list[0],abcd_list[1],abcd_list[2],abcd_list[3]]

        output_a = hex((int(abcd_list[0],16)+int(aa,16))&0xffffffff)  
        output_b = hex((int(abcd_list[1],16)+int(bb,16))&0xffffffff)  
        output_c = hex((int(abcd_list[2],16)+int(cc,16))&0xffffffff)  
        output_d = hex((int(abcd_list[3],16)+int(dd,16))&0xffffffff)  

        abcd_list = [output_a,output_b,output_c,output_d] 

        T_count = 1

    abcd_tempt[0] = hex((int(abcd_tempt[0],16)+int(A,16))&0xffffffff)  
    abcd_tempt[1] = hex((int(abcd_tempt[1],16)+int(B,16))&0xffffffff)  
    abcd_tempt[2] = hex((int(abcd_tempt[2],16)+int(C,16))&0xffffffff)  
    abcd_tempt[3] = hex((int(abcd_tempt[3],16)+int(D,16))&0xffffffff)  


    return show_result(abcd_tempt)

