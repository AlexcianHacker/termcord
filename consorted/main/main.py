from termcord import main; 
import sys; 


if __name__=="__main__": 
  print("Would You Like To Allow GUI (Y/N)?: "); 
  result: int; 
  pans: bool = True; 
  if 'Y' in sys.stdin.readline(): pans = True; 
  else: pans = False; 
  print("Would You Like To Run In Hybrid Mode [Bot Commands Included] (Y/N)?: "); 
  hybrid: bool = True; 
  if 'Y' in sys.stdin.readline(): hybrid = True; 
  else: hybrid = False; 
  print("Would You Like To Use Simple Mode? (Y/N): "); 
  simple_m: bool = False; 
  if 'Y' in sys.stdin.readline(): simple_m = True; 
  print("Booting Discord.... "); 
  result = main(dual=hybrid, simple=simple_m, panels=pans); 
  del pans, hybrid; 
  print("Program Exited With Exit Code ", result, ". "); 
  
