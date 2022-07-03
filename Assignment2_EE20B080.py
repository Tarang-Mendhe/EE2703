'''
ASSIGNMENT 2
 TARANG NARENDRA MENDHE(EE20B080)

 11/2/2022

'''

#Importing necessory libraries

from sys import argv, exit

import numpy as np

import math as math 

np.set_printoptions(precision=5) 

#Defining global constants 
START = ".circuit"
END = ".end"

class resistor : 
    def __init__(self,name,node1,node2,value,dim):
        self.name=name
        if node1.strip() == "GND" :
            self.node1= 0 
        else :
            self.node1= int(node1)                
        if node2.strip() == "GND" :
            self.node2= 0         
        else :
            self.node2= int(node2)               
        self.value= float (value)
        self.dim= float (dim) 
        
    def matrix(self) :
        M=np.zeros((dim,dim),dtype='cfloat')        
        M[self.node1][self.node1]+=1/(float(self.value))
        M[self.node1][self.node2]-=1/(float(self.value))
        M[self.node2][self.node2]+=1/(float(self.value))
        M[self.node2][self.node1]-=1/(float(self.value))           
        return M  
        
class inductor : 
    def __init__(self,name,node1,node2,value,dim,frequency):
        self.name=name
        if node1.strip() == "GND" :
            self.node1= 0 
        else :
            self.node1= int(node1)                
        if node2.strip() == "GND" :
            self.node2= 0         
        else :
            self.node2= int(node2)
        self.value=value       
        self.frequency = frequency
        self.dim= float (dim) 
        
    def matrix(self):
        M=np.zeros((dim,dim),dtype='cfloat')
        impedance = 1/complex(0,2*math.pi*float(self.frequency)*float(self.value))
        M[self.node1][self.node1]+=impedance
        M[self.node1][self.node2]-=impedance
        M[self.node2][self.node2]+=impedance
        M[self.node2][self.node1]-=impedance
        return M

class capacitor : 
    def __init__(self,name,node1,node2,value,dim,frequency):
        self.name=name
        if node1.strip() == "GND" :
            self.node1= 0 
        else :
            self.node1= int(node1)                
        if node2.strip() == "GND" :
            self.node2= 0         
        else :
            self.node2= int(node2)
        self.value=value       
        self.frequency = frequency
        self.dim= float (dim) 
        
    def matrix(self):
        M=np.zeros((dim,dim),dtype='cfloat')
        impedance = complex(0,2*math.pi*float(self.frequency)*float(self.value))
        M[self.node1][self.node1]+=impedance
        M[self.node1][self.node2]-=impedance
        M[self.node2][self.node2]+=impedance
        M[self.node2][self.node1]-=impedance
        return M
        
class current_source :
    def __init__(self,name,node1,node2,vpp,phase,dim):
        self.name=name
        if node1.strip() == "GND" :
            self.node1= 0 
        else :
            self.node1= int(node1)                
        if node2.strip() == "GND" :
            self.node2= 0         
        else :
            self.node2= int(node2)
        self.value = float(vpp)
        self.vpp=vpp
        self.phase=phase
        self.dim = int(dim)
        
    def assign(self,flag):
        b = np.zeros(dim,dtype='cfloat')
        if flag ==1 :
         value_comp=(float(self.vpp)+0j)*complex(math.cos(float(self.phase)),math.sin(float(self.phase)))/2   
        else :       
         value_comp = self.value  
        b[self.node1]+=value_comp
        b[self.node2]-=value_comp
        return b
                
class voltage_source :
    def __init__(self,name,node1,node2,vpp,phase,dim):
        self.name=name
        if node1.strip() == "GND" :
            self.node1= 0 
        else :
            self.node1= int(node1)                
        if node2.strip() == "GND" :
            self.node2= 0         
        else :
            self.node2= int(node2)
        self.vpp=vpp
        self.value=float(vpp)
        self.phase=float (phase)
        self.dim = float(dim)
        
    def matrix(self,branch_pos,flag):
        M=np.zeros((dim,dim),dtype='cfloat') 
        b = np.zeros(dim,dtype='cfloat')
        if flag ==1 :
          value_comp=(float(self.vpp)+0j)*complex(math.cos(float(self.phase)),math.sin(float(self.phase)))/2
        else :
          value_comp= self.value
        M[self.node1][branch_pos]=1
        M[self.node2][branch_pos]=-1
        M[branch_pos][self.node1]=-1 
        M[branch_pos][self.node2]=1
        
        b[branch_pos]=value_comp
        return M,b        
        
#Function to Convert exponents to float 
def expo(exp) :               
       a = float(exp.split("e")[0]) * math.pow(10,float(exp.split("e")[1]))
       return a


#Function to Extract tokens
def Token_create(Line):
  tokens = Line.split()
                    
  Element = tokens[0]
  FromNode = tokens[1]
  ToNode = tokens[2]
                  
  if(len(tokens) ==4 ):  #For R,L,C and Independent sources
    Value = tokens[3]
    return[Element,FromNode,ToNode,Value]
                    
  elif(len(tokens) ==5 ):  #For CCVS and CCCS
    VoltageSource = Words[3]
    Value = Words[4] 
    return[Element,FromNode,ToNode,VoltageSource,Value]
                   
  elif(len(tokens) ==6 ):  #For VCVS and VCVS
    VoltageSourceNode1 = Words[3]
    VoltageSourceNode2 = Words[4]
    Value = Words[5]
    return[Element,FromNode,ToNode,VoltageNode1,VoltageNode2,Value]
                   
  else : 
    return[]    
    
    


   

#Checking if number of arguments are correct
if len(argv) != 2 :
   print (' please enter only two arguments as %s <circuit_file>.netlist '% argv[0])
   
else :

  #Checking if given arguments are valid    
   try : 
       
      with open(argv[1]) as f:
            lines = f.readlines()     
            corrected_lines=[]
      try:
            for line in lines :
             corrected_lines.append(line.split('#')[0].split('\n')[0])  
        
            #checking if given circuit file has correct identifiers            

            index1 = corrected_lines.index(START)  
            index2 = corrected_lines.index(END)
              
            circuit_part = corrected_lines[index1+1: index2]  
            
            try :
             if corrected_lines[index2+1].split()[0] == ".ac" :
               
               freq = corrected_lines[index2+1].split()[2] 
               ac_flag=1
               
             else :
               ac_flag=0 
               freq = 1e-20  # very small freq for dc  
            except IndexError: 
               ac_flag=0 
               freq = 1e-20               
            
            
            #finding the dimension of matrix 
            nodes= []
            source = [] 
            node_no = 0
            sources = 0 
            for x in circuit_part :  
            
             nodes.append (x.split()[1])
            
            nodes = list(set(nodes)) 
            nodes_no= len(nodes) 
            
            for x in circuit_part :
             if list(x)[0]=='V':
              sources+=1 
              source = x.split()[0]         #single source 
             
            dim = nodes_no + sources
            
            M=np.zeros((dim,dim),dtype='cfloat') 
            M1=np.zeros((dim,dim),dtype='cfloat') 
            b = np.zeros(dim,dtype='cfloat')
            b1 = np.zeros(dim,dtype='cfloat')
                
            for x in circuit_part :           	
            	if (list(x)[0]) == 'R' :      		
            		y=x.split()             		
            		R=resistor(y[0],y[1],y[2],y[3],dim)
            		M1=R.matrix() 
            		  
            		M+=M1
            		          		
            	elif (list(x)[0])== 'C':
                       y=x.split()
                       C=capacitor(y[0],y[1],y[2],y[3],dim,freq)
                       M1 =C.matrix() 
                       
                       M+= M1 		
            	elif (list(x)[0])== 'L':
            		y=x.split()
            		L=inductor(y[0],y[1],y[2],(y[3]),dim,freq)
            		M1=L.matrix() 
            		
            		M+= M1
            		 
            	elif (list(x)[0])== 'I':
            	       y= x.split() 
            	       I=current_source(y[0],y[1],y[2],y[4],y[5],dim)
            	       b1= I.matrix(ac_flag) 
            	       b+=b1
            	elif (list(x)[0])=='V':
            	       y=x.split() 
            	       if (ac_flag==1) :
            	         V= voltage_source (y[0],y[1],y[2],y[4],y[5],dim)
            	       else :
            	         V= voltage_source (y[0],y[1],y[2],y[3],'0',dim)  
            	       M1,b1= V.matrix(nodes_no,ac_flag) 
            	       
            	       M+=M1
            	       b+=b1        
            	                  		
            M[0][0] = 1                       #nodal analysis equation of V0 changed to V0=0
            for i in range(1,6) :
               M[0][i] = 0
                            
            x = np.linalg.solve(M, b) 
            l= nodes_no + 1
            NODE_matrix = list(range(nodes_no))
            
            print (" Nodes in the circuit are",NODE_matrix," whose values are \n",x[0:nodes_no],"respectively \n Current through voltage source",source,"is",x[-1] ) 
      except ValueError :
             print (" Circuit is Invalid " )      
   except IOError :
         print ('Enter second argument as <circuit_file>.netlist ' ) 
         



	 	
	 	
	 	
	 
	 
	 	
	 	
	 	
	 	
	 	


 
