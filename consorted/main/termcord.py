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
        login: list[str] = None, 
        dual: bool = True, 
        simple: bool = False, 
        panels: bool = True, 
        hyprefix: str = None) -> int: 
  if panels: import tkinter; 
  result_: int = 0; 
  
  def initialize_UI(user,) -> int: 
    if not simple: 
      ## Regular Mode 
    else: 
      ## Simple Mode 
  
  def initialize_tn(token: str) -> int: 
    result_i: int = 0; 
    
    user = None; 
    print("[OK] Login Initialized..."); 
    initialize_UI(user); 
    return result_i; 
  
  def initialize_login(eml: str, 
                      pswd: str, 
                      token: str = None) -> int: 
    result_i: int = 0; 
    
    user = None; 
    print("[OK] Login Initialized..."); 
    initialize_UI(user); 
    return result_i; 
  
  if token != None: 
    if login != None: result_=initialize_login(login[0], 
                                  login[1], 
                                  token=token); 
    else: result_ = initialize_tn(token); 
  else: print("Error (-3): Improper Or No Token Has Been Passed. "); return result_:= -3; 
  return result_; 
