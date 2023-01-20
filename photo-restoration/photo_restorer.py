from dotenv import load_dotenv
load_dotenv()

import replicate

model = replicate.models.get("tencentarc/gfpgan")
version = model.versions.get("9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3")

def predict_image(filename):
    # https://replicate.com/tencentarc/gfpgan/versions/9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3#input
    inputs = {
        # Input
        'img': open(filename, "rb"),

        # GFPGAN version. v1.3: better quality. v1.4: more details and better
        # identity.
        'version': "v1.4",

        # Rescaling factor
        'scale': 2,
    }
    print(inputs)

    # https://replicate.com/tencentarc/gfpgan/versions/9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3#output-schema
    output = version.predict(**inputs)
    print(output)
    return output