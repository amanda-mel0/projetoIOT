import pygame
import random
import sys
from screens.login_screen import LoginScreen
from screens.cadastro_screen import CadastroScreen
from screens.mapa_screen import MapaScreen
from screens.fase1_screen import Fase1Screen
from screens.fase2_screen import Fase2Screen
from screens.fase_screen import FaseScreen
from screens.perfil_screen import PerfilScreen

# ── Configurações gerais ──────────────────────────────────────────────────────
LARGURA, ALTURA = 1100, 700
FPS = 60
TITULO = "Ler Brincando"

# ── Paleta LEGO ───────────────────────────────────────────────────────────────
CORES = {
    "vermelho":   (220, 38,  38),
    "azul":       (37,  99, 235),
    "verde":      (34, 197,  94),
    "amarelo":    (234,179,   8),
    "laranja":    (249,115,  22),
    "roxo":       (147, 51, 234),
    "branco":     (255,255, 255),
    "preto":      (15,  15,  15),
    "cinza_esc":  (30,  30,  40),
    "cinza_med":  (60,  60,  75),
    "ceu":        (56, 182, 255),
    "terra":      (139, 90,  43),
}


def main():
    pygame.init()
    pygame.display.set_caption(TITULO)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    relogio = pygame.time.Clock()

    # Estado global compartilhado entre telas
    estado = {
        "usuario": None,   # dados do usuário logado
        "tela_atual": "login",
        "fase_atual": 1,
        "avatar_escolhido": "masculino",   # avatar padrão
    }

    telas = {
        "login":    LoginScreen(tela, LARGURA, ALTURA, CORES, estado),
        "cadastro": CadastroScreen(tela, LARGURA, ALTURA, CORES, estado),
        "perfil":   PerfilScreen(tela, LARGURA, ALTURA, CORES, estado),
        "mapa":     MapaScreen(tela, LARGURA, ALTURA, CORES, estado),
        "fase_1":   Fase1Screen(tela, LARGURA, ALTURA, CORES, estado),
        "fase_2":   Fase2Screen(tela, LARGURA, ALTURA, CORES, estado),
    }
    for i in range(3, 11):
        telas[f"fase_{i}"] = FaseScreen(tela, LARGURA, ALTURA, CORES, estado, i)

    rodando = True
    while rodando:
        eventos = pygame.event.get()
        for ev in eventos:
            if ev.type == pygame.QUIT:
                rodando = False

        tela_key = estado["tela_atual"]
        tela_obj = telas.get(tela_key)

        if tela_obj:
            tela_obj.handle_events(eventos)
            tela_obj.update()
            tela_obj.draw()

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
