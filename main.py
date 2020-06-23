from fastapi import FastAPI

from fastai.vision import load_learner, open_image

app = FastAPI()

defaults.device = torch.device('cpu')

trees = load_learner('export_learners', 'trees.pkl')


@app.get('/trees/{img}')
async def trees(img):
    image = open_image(img)
    return {
        'prediction': trees.predict(img)[0]
    }
