import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline

class DescribeScene():
    def __init__(self, model = "Salesforce/blip-image-captioning-large") -> None:
        self.pipe = pipeline("image-to-text", model=model)

    def caption(self, img):
        return self.pipe(img)[0]['generated_text'] # type: ignore

    
def main():
    img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
    raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

    desriptor = DescribeScene()

    print(desriptor.caption(raw_image))

if __name__ == '__main__':
    main()