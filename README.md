# aed-cripto

## Python code
### uses haslib library to generate sha256 hash and compare to the given hash \(chave2\)
## enc\*.py
### **encrypt** function  
#### *hash*\_*str* is used on *sha256\(\)* function  
#### *sha256\(\)* haslib function to generate sha256 hash  
#### *encode\("base64"\)* is to convert the output hash to the same format of chave2 hash \(AKCkKOEHZuUPfCLbS0ye8WFnXoDEgw9RFYXlw293vbY\= this is base64 format\)

### **alphabet**  
#### a\:z \+ A\:Z \+ 0\:9

### **rightHash**    
#### hash generated from chave2

### **fors**  
#### Iterates the whole *alphabet* for each position of the key.  
#### In word sizes 7 and 8, calls *encrypt* function, with the generated word as a parameter to the function.  
#### Compares the generated hash with *rightHash*. If it's the same, print the word. If it's not, try the next possible keys. 

### The code was divided in 4 parts, each one has a different range in the alphabet. 
