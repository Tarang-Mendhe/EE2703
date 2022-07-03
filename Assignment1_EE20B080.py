'''
ASSIGNMENT 1
 TARANG NARENDRA MENDHE(EE20B080)

26/1/2022

'''

# importing necessary libraries
import sys

# Defining Constants
CIRCUIT_START = ".circuit"
CIRCUIT_END = ".end"

# Extracting the Words(Tokens) from a Line

def Token_Create(Line):
    Words = Line.split()

    # For R, L, C, Independent Sources
    if(len(Words) == 4):
        elementName = Words[0]
        node1 = Words[1]
        node2 = Words[2]
        value = Words[3]
        return [elementName, node1, node2, value]

    # For CCVS & CCCS
    elif(len(Words) == 5):
        elementName = Words[0]
        node1 = Words[1]
        node2 = Words[2]
        voltageSource = Words[3]
        value = Words[4]
        return [elementName, node1, node2, voltageSource, value]

    # For VCVS & VCCS
    elif(len(Words) == 6):
        elementName = Words[0]
        node1 = Words[1]
        node2 = Words[2]
        voltageSourceNode1 = Words[3]
        voltageSourceNode2 = Words[4]
        value = Words[5]
        return [elementName, node1, node2, voltageSourceNode1, voltageSourceNode2, value]

    else:
        return []

def Ckt_Print(SPICELinesTokens):

    for x in SPICELinesTokens[::-1]:
        for y in x[::-1]:
            print(y, end=' ')
        print('')
    print('')
    return

if __name__ == "__main__":

    # checking number of command line arguments
    if len(sys.argv)!=2 :
        sys.exit("Invalid number of arguments! Pass the netlist file as the second argument.")
    else:
        try:
            Ckt_File = sys.argv[1]

            # checking if given netlist file is of correct type
            
            if (not Ckt_File.endswith(".netlist")):
                print("Wrong file type!")
            else:
                with open (Ckt_File, "r") as f:
                    SPICELines = []
                    for line in f.readlines():
                        SPICELines.append(line.split('#')[0].split('\n')[0])
                    try:
                        # finding the location of the identifiers
                        identifier1 = SPICELines.index(CIRCUIT_START)
                        identifier2 = SPICELines.index(CIRCUIT_END)

                        SPICELinesActual = SPICELines[identifier1+1:identifier2]
                        SPICELinesTokens = [Token_Create(line) for line in SPICELinesActual]

                        # Printing Circuitin Reverse Order
                        Ckt_Print(SPICELinesTokens)
                    except ValueError:
                    
                        print("Netlist does not abide to given format! Make sure to have .circuit and .end lines in the file.")
                        
        except FileNotFoundError:
        
            print("Given file does not exist! Please check if you have entered the name of the netlist file properly.")
