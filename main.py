def auto_beallitas(auto: game.LedSprite):
    auto.set(LedSpriteProperty.X, oszlopok.shift())
    auto.set(LedSpriteProperty.Y, 0)
    auto.set(LedSpriteProperty.BRIGHTNESS, 10)
def autotleptett(auto2: game.LedSprite):
    global pontszam
    if auto2.get(LedSpriteProperty.Y) == 4:
        if len(oszlopok) == 0:
            oszlop_beallitas()
            pontszam += 1
        auto_beallitas(auto2)
    else:
        auto2.change(LedSpriteProperty.Y, 1)
        auto2.set(LedSpriteProperty.BRIGHTNESS,
            auto2.get(LedSpriteProperty.Y) * 50 + 10)
    if ember.is_touching(auto2):
        music._play_default_background(music.built_in_playable_melody(Melodies.WAWAWAWAA),
            music.PlaybackMode.IN_BACKGROUND)
        game.set_score(pontszam)
        game.game_over()

def on_button_pressed_a():
    ember.change(LedSpriteProperty.X, -1)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            400,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def oszlop_beallitas():
    global oszlopok, ures_oszlop
    oszlopok = [0, 1, 2, 3, 4]
    ures_oszlop = randint(0, len(oszlopok) - 1)
    oszlopok.remove_at(ures_oszlop)

def on_button_pressed_b():
    ember.change(LedSpriteProperty.X, 1)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            400,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

ures_oszlop = 0
ember: game.LedSprite = None
oszlopok: List[number] = []
pontszam = 0
pontszam = 0
oszlopok = []
ember = game.create_sprite(2, 4)
ember.set(LedSpriteProperty.BLINK, 300)
game.set_life(1)
oszlop_beallitas()
auto1 = game.create_sprite(0, 0)
auto_beallitas(auto1)
auto22 = game.create_sprite(0, 0)
auto_beallitas(auto22)
auto3 = game.create_sprite(0, 0)
auto_beallitas(auto3)
auto4 = game.create_sprite(0, 0)
auto_beallitas(auto4)
szunet = 200
basic.pause(szunet)

def on_forever():
    autotleptett(auto1)
    basic.pause(50)
    autotleptett(auto22)
    basic.pause(50)
    autotleptett(auto3)
    basic.pause(50)
    autotleptett(auto4)
    basic.pause(szunet)
basic.forever(on_forever)
