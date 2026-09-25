import time
import winsound
import os

# Notes for "Happy Birthday" (frequency in Hz)
notes = [
    (264, 400), (264, 400), (297, 800), (264, 800), (352, 800), (330, 1600),  # Happy birthday to you
    (264, 400), (264, 400), (297, 800), (264, 800), (396, 800), (352, 1600),  # Happy birthday to you
    (264, 400), (264, 400), (528, 800), (440, 800), (352, 800), (330, 800), (297, 1600),  # Happy birthday dear Mom
    (466, 400), (466, 400), (440, 800), (352, 800), (396, 800), (352, 1600)   # Happy birthday to you
]

lyrics = [
    "Happy birthday to you",
    "Happy birthday to you",
    "Happy birthday to ..... oops, I don't know your name!",
    "Happy birthday to you",
]

cake_body = [
    "   | | |   ",
    "  =======  ",
    "  |     |  ",
    "  |     |  ",
    "  |_____|  "
]

def draw_cake(candle_direction=">"):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   " + candle_direction + " " + candle_direction + " " + candle_direction)
    for line in cake_body:
        print(line)

try:
    while True:
        # Flicker candles
        draw_cake(">")
        time.sleep(0.5)
        draw_cake("<")
        time.sleep(0.5)

        # Print lyrics
        for line in lyrics:
            print(line)
            time.sleep(0.5)

        # Play the tune
        for freq, dur in notes:
            winsound.Beep(freq, dur)
            time.sleep(0.05)

except KeyboardInterrupt:
    # Finale message when you stop with Ctrl+C
    draw_cake(">")
    print("\n🎂 The cake is ready! 🎂")
