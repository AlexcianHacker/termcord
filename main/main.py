from comcord import main; 
import sys; 


if __name__=="__main__": 
  print("Would You Like To Allow GUI (Y/N)?: "); 
  result: int; 
  if 'Y' in sys.stdin.readline(): 
    print("Booting Discord.... "); 
    result = main(); 
  else: 
    print("Booting Discord.... "); 
    result = main(panels=False); 
  
