import pygame

ascii_tanks ={
    "straight" : [
        "/--------\\",
        "|        |",
        "|        |",
        "|        |",
        "|        |",
        "|        |",
        "|        |",
        "\________/"],
    "straight" : [
        "                -",
        "             .      .",
        "          .             .",
        "|        |",
        "|        |",
        "|        |",
        "|        |",
        "\________/"],    
        
}

def render_ascii():
    for symbol in ascii_tanks["straight"]:
        print(symbol)

