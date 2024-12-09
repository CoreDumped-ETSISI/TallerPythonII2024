# hay que instalar arcade antes con pip install arcade en la terminal

import arcade

# Constantes para la pantalla
SCREEN_WIDTH = # TODO
SCREEN_HEIGHT = # TODO
SCREEN_TITLE =  # TODO

# Constantes para escalar los sprites
CHARACTER_SCALING = 0.17
GROUND_SCALING = 0.20
CYLINDER_SCALING = 0.20

# Constantes del jugador
PLAYER_MOVEMENT_SPEED = 5
PLAYER_JUMP_SPEED = 20
GRAVITY = # TODO

# Límite para Game Over
GAME_OVER_THRESHOLD = -50

class MyGame(arcade.Window):
    """Clase principal del juego."""
    
    def __init__(self):
        """Inicializa el juego y sus variables."""
        # TODO: Llama al constructor de la clase padre y configura la ventana, tiene como argumentos el ancho, alto y título
        
        # Configura el color de fondo
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Listas de sprites
        self.wall_list = None
        self.player_list = None

        # Sprite del jugador
        self.player_sprite = None

        # Bandera para Game Over
        self.game_over = False

        # Variables para el scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """Configura los sprites y el estado inicial del juego."""
        # TODO: Inicializa las listas de sprites son de tipo arcade y son listas de sprites, no necesita ningún argumento
        # https://api.arcade.academy/en/2.6.15/api/sprite_list.html

        # self.player_list = ...
        # self.wall_list = ...
        
        # TODO: Configura el jugador (usar "mario.png" y CHARACTER_SCALING) con arcade.Sprite()
        # self.player_sprite = ...
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 93
        # agregar a la lista  el sprite del jugador

        # Crear el suelo
        for x in range(0, 1250, 64):
            wall = arcade.Sprite("ground.png", GROUND_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Crear obstáculos: es una lista de listas con coordenadas, la y debe ser 110
        # coordinate_list = 
        # poner los cilindros
            wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
            wall.position = # coordenada
            self.wall_list.append(wall)

        # TODO: Crear el motor de físicas: agregar el jugador, las paredes y la gravedad
        self.physics_engine = arcade.PhysicsEnginePlatformer(#)

    def on_draw(self):
        """Dibuja todo en la pantalla."""
        arcade.start_render()
        if self.game_over:
            arcade.draw_text("GAME OVER", self.view_left + SCREEN_WIDTH / 2, 
                             self.view_bottom + SCREEN_HEIGHT / 2, 
                             arcade.color.RED, font_size=50, anchor_x="center")
            arcade.draw_text("Presiona R para reiniciar", self.view_left + SCREEN_WIDTH / 2, 
                             self.view_bottom + SCREEN_HEIGHT / 2 - 60, 
                             arcade.color.WHITE, font_size=20, anchor_x="center")
        else:
            # TODO: Dibuja los sprites del jugador y las paredes con el método draw de las listas de sprites
            pass

    def on_key_press(self, key, modifiers):
        """Detecta cuándo se presiona una tecla."""
        if not self.game_over:
            # TODO: Movimiento del jugador: las teclas son del formato arcade.key.KEY
            if ##
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
            elif ##
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif ##
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        else:
            # TODO: Reinicia el juego al presionar R
            if key == arcade.key.R:
                pass

    def on_key_release(self, key, modifiers):
        """Detecta cuándo se libera una tecla."""
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Lógica del juego."""
        if not self.game_over:
            # TODO: Actualiza el motor de físicas con el método update
            pass

            # TODO: Detecta si el jugador ha caído fuera de los límites
            if self.player_sprite.bottom < GAME_OVER_THRESHOLD:
                pass
                
            # TODO: manejo del scrolling



    def handle_scrolling(self):
        """ Maneja el scrolling de la cámara """
        changed = False

        # Scroll a la izquierda
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll a la derecha
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll arriba
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll abajo
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                self.view_bottom, SCREEN_HEIGHT + self.view_bottom)


def main():
    """Punto de entrada del juego."""
    window = # objeto de la clase MyGame
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
