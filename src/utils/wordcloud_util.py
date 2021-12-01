import base64
from PIL import Image 
from io import BytesIO 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS


def generate(word_list,
             width=300,
             height=300,
             background_color='white',
             mode='RGB',
             mask=None,
             max_words=100,
             stopwords=None,
             max_font_size=50,
             font_path=None,
             relative_scaling=0.6,
             random_state=10,
             scale=2):

    space_list = " ".join(x for x in word_list)
    wc = WordCloud(
        width=width,
        height=height,
        background_color=background_color,
        mode=mode,
        mask=mask,
        max_words=max_words,
        stopwords=stopwords,
        font_path=font_path,
        max_font_size=max_font_size,
        relative_scaling=relative_scaling,
        random_state=random_state,
        scale=scale
    ).generate(space_list)
    wc.to_file('test2_ciyun.jpg') 
    return wc
    

def convert_img_to_b64(wc):
    buffer = BytesIO()
    wc.to_image().save(buffer, format="png")
    return base64.b64encode(buffer.getvalue())


# if __name__ == '__main__':
#     word = ['''
#     Generally speaking, long holidays are good for us college students. On the one hand, we have a lot of time to study by ourselves and thus improve weaknesses and further develop strengths. On the other hand, we can take part-time jobs, which can make us realize responsibility and make ourselves better prepared for social life.
#     ''']
#     wc = generate(word)
#     s = convert_img_to_b64(wc)
#     print(s)
#     img = Image.open(BytesIO(base64.b64decode(s)))
#     plt.imshow(img)
#     plt.show()