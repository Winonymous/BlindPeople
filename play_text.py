from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
from playsound import playsound


class PlayText():
    def __init__(self) -> None:
        self.embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        self.speaker_embedding = torch.tensor(self.embeddings_dataset[7306]["xvector"]).unsqueeze(0) # type: ignore

        self.pipe = pipeline("text-to-speech", model="microsoft/speecht5_tts")

    def play_audio(self, audio_file = "speech.wav"):
        playsound(audio_file)
        # pass

    def generate_audio(self, text):
        # You can replace this embedding with your own as well.

        speech = self.pipe(text, forward_params={"speaker_embeddings": self.speaker_embedding})

        sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"]) # type: ignore

    def generate_play(self, text):
        self.generate_audio(text)
        self.play_audio()

def main():
    play_text = PlayText()
    text = "Hello, my dog is cooler than you!"
    print(text)

    play_text.generate_play(text)

if __name__ == "__main__":
   main()