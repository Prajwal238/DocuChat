import os
from io import BytesIO
from PIL import Image


class ImageLoader():
    
    def __init__(self, filePath):
        self.images = os.listdir(filePath)

    def load_images(self, path, opts={}):
        
        images      = self.images
        image_data  = []
        # df          = opts.get("df")
        pd          = opts.get("pd")

        for image in images:

            img_path = path + image
            with open(img_path, "rb") as file:
                img_bytes       = BytesIO(file.read())
                extracted_img   = Image.open(img_bytes).resize((256,256))
                
                image_data.append([extracted_img])
                
                new_row = {'chunk_data': img_path,
                   'media_type': "image",
                   'embeddings': ""}
                opts["df"]      = pd.concat([opts["df"], pd.DataFrame([new_row])], ignore_index=True)

        return image_data