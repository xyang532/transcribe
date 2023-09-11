import custom_speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
    print(f'Set minimum energy threshold to {r.energy_threshold}')
    while True:
        print("Say something!")
        with m as source:
            audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            print(f'You said {value}')
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print(f"Uh oh! Couldn't request results from Google Speech Recognition service; {e}")
except KeyboardInterrupt:
    pass
