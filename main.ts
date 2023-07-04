function auto_beallitas (auto: game.LedSprite) {
    auto.set(LedSpriteProperty.X, oszlopok.shift())
    auto.set(LedSpriteProperty.Y, 0)
    auto.set(LedSpriteProperty.Brightness, 10)
}
function autotleptett (auto2: game.LedSprite) {
    if (auto2.get(LedSpriteProperty.Y) == 4) {
        if (oszlopok.length == 0) {
            oszlop_beallitas()
            pontszam += 1
        }
        auto_beallitas(auto2)
    } else {
        auto2.change(LedSpriteProperty.Y, 1)
        auto2.set(LedSpriteProperty.Brightness, auto2.get(LedSpriteProperty.Y) * 50 + 10)
    }
    if (ember.isTouching(auto2)) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Wawawawaa), music.PlaybackMode.InBackground)
        game.setScore(pontszam)
        game.gameOver()
    }
}
input.onButtonPressed(Button.A, function () {
    ember.change(LedSpriteProperty.X, -1)
    music.play(music.createSoundExpression(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
function oszlop_beallitas () {
    oszlopok = [
    0,
    1,
    2,
    3,
    4
    ]
    ures_oszlop = randint(0, oszlopok.length - 1)
    oszlopok.removeAt(ures_oszlop)
}
input.onButtonPressed(Button.B, function () {
    ember.change(LedSpriteProperty.X, 1)
    music.play(music.createSoundExpression(WaveShape.Square, 400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
let ures_oszlop = 0
let ember: game.LedSprite = null
let oszlopok: number[] = []
let pontszam = 0
pontszam = 0
oszlopok = []
ember = game.createSprite(2, 4)
ember.set(LedSpriteProperty.Blink, 300)
game.setLife(1)
oszlop_beallitas()
let auto1 = game.createSprite(0, 0)
auto_beallitas(auto1)
let auto22 = game.createSprite(0, 0)
auto_beallitas(auto22)
let auto3 = game.createSprite(0, 0)
auto_beallitas(auto3)
let auto4 = game.createSprite(0, 0)
auto_beallitas(auto4)
let szunet = 200
basic.pause(szunet)
basic.forever(function () {
    autotleptett(auto1)
    basic.pause(50)
    autotleptett(auto22)
    basic.pause(50)
    autotleptett(auto3)
    basic.pause(50)
    autotleptett(auto4)
    basic.pause(szunet)
})
