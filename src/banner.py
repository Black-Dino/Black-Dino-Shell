from .styles.colors import colors

print(colors['RED'],)

def banner():
    title = colors ['YELLOW'] + "'Black Dino'"
    line = colors['GREEN'] + '------------------------------'
    temp = f"""
               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  {title}

{line}
      """

    print(colors['RED'],temp+colors['WHITE'],end='')