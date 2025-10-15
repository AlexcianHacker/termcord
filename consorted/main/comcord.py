import asyncio; 
import aiohttp; 
import discord; 
from discord.ext import commands; 
import sys; 
import os; 
import requests; 
from itertools import cycle; 
import random; 


def main(token: str = None, 
        login: list[str] = None; 
        dual: bool = True; 
        panels: bool = True
        hyprefix: str = None) -> int: 
  if panels: import tkinter; 
  result_: int = 0; 
  
  def initialize_tn(token: str, 
                    prefix: str = None) -> int: 
    result_i: int = 0; 
    
    return result_i; 
  
  def initialize_login(eml: str, 
                      pswd: str, 
                      prefix: str = None, 
                      token: str = None) -> int: 
    result_i: int = 0; 
    
    return result_i; 
  
  if token != None: 
    if login != None: result_=initialize_login(login[0], 
                                  login[1], 
                                  prefix=hyprefix, 
                                  token=token); 
    else: result_ = initialize_tn(token, prefix=hyprefix); 
  else: print("Error (-3): Improper Or No Token Has Been Passed. "); return result_:= -3; 
  return result_; 
