import pygame, random
pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = win.get_size()
NAME= "Radu"
S= 26
font = pygame.font.SysFont("courier", S, 1)
#the name written big becomes a mask
big = pygame.font.SysFont("arial", 400, 1)
mask, mv = big.render(NAME, 1, "white"), W - 80
mh = mask.get_height() * mv // mask.get_width()
mask = pygame.transform.scale(mask, (mv, mh))
top = H // 2 - mh // 2 +120
found = set()
cols = [random.randint(-80, 0)
        for _ in range(W // S)]
fade = pygame.Surface((W, H))
fade.set_alpha(40)

while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            raise SystemExit
    win.blit(fade, (0, 0))
    for i, j in enumerate(cols):
        x, y = i * S - 40, j * S - top
        if 0<= x < mv and 0<= y < mh:
            if mask.get_at((x, y)).a > 128:
                found.add((i, j)) #a letter!
        c = random.choice(CH)
        img = font.render(c, 1, "green")
        win.blit(img, (i * S, j * S))
        cols[i] = j +1 if j * S < H else -20
    for i, j in found: # letter stay lit
        c = random.choice(CH)#
        img = font.render(c, 1, (190,255,200))
        win.blit(img, (i * S, j * S))
    pygame.display.flip()
    pygame.time.wait(30)