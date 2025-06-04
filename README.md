
# Jogo Dino Jump

Dino Jump é um jogo de corrida infinita 2D simples desenvolvido usando Pygame. O objetivo é fazer seu dinossauro pular sobre os obstáculos (pedras) que se aproximam e marcar o máximo de pontos possível.

---

## Funcionalidades

* **Mecânica Clássica de Pulo:** Controle um dinossauro que pula para evitar obstáculos.
* **Jogabilidade Infinita:** O jogo continua enquanto você evitar colisões, com a pontuação aumentando.
* **Tela de Fim de Jogo:** Exibe "Game Over!" e permite reiniciar ou sair.
* **Pontuação:** Acompanha sua pontuação atual durante o jogo.

---

## Instalação

Para rodar este jogo, você precisará ter Python e a biblioteca Pygame instalados em seu sistema.

### Pré-requisitos

* Python 3.x
* Biblioteca Pygame

### Passos

1.  **Instalar Python:** Se você não tem Python instalado, faça o download no site oficial: [python.org](https://www.python.org/downloads/)
2.  **Instalar Pygame:** Abra seu terminal ou prompt de comando e execute o seguinte comando:

    ```bash
    pip install pygame
    ```
3.  **Baixar o Jogo:** Salve o código Python fornecido como um arquivo `.py` (ex: `dino_jump.py`) em seu computador.

---

## Como Jogar

1.  **Rodar o Jogo:** Abra seu terminal ou prompt de comando, navegue até o diretório onde você salvou `dino_jump.py` e execute o jogo usando:

    ```bash
    python dino_jump.py
    ```
2.  **Começar a Jogar:** A janela do jogo será aberta, e seu dinossauro começará a correr automaticamente.
3.  **Pular:** Pressione a **BARRA DE ESPAÇO** para fazer seu dinossauro pular sobre as pedras que se aproximam.
4.  **Pontuação:** Você ganha pontos por cada pedra que você passa com sucesso.
5.  **Fim de Jogo:** Se seu dinossauro colidir com uma pedra, o jogo terminará, e uma mensagem "Game Over!" aparecerá.
6.  **Reiniciar:** Para jogar novamente, pressione a tecla **R** na tela de "Game Over!".
7.  **Sair:** Para sair do jogo a qualquer momento (incluindo a tela de "Game Over!"), pressione a tecla **ESC** ou feche a janela do jogo.

---

## Mecânicas do Jogo

* **Dinossauro:** Um quadrado vermelho que se move continuamente para a direita.
* **Pedras:** Obstáculos de quadrado preto que aparecem no lado direito da tela e se movem em direção ao dinossauro.
* **Pulo:** Ao pressionar a BARRA DE ESPAÇO, o dinossauro pula com uma velocidade inicial para cima, e a gravidade o puxa de volta para baixo.
* **Detecção de Colisão:** O jogo verifica colisões entre o dinossauro e as pedras. Uma colisão resulta em "Game Over".
* **Pontuação:** Cada pedra desviada com sucesso (ou seja, que sai da tela para a esquerda) adiciona um ponto à sua pontuação.

---
