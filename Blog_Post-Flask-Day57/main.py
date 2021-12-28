from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    global all_my_posts
    pottery_blog_url = 'https://api.npoint.io/b6f6a4965365e636ea29'
    response = requests.get(pottery_blog_url)
    all_posts = response.json()
    all_my_posts = all_posts
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def get_blog(num):
    for info in all_my_posts:
        if info['id'] == num:
            pass_info = info
    return render_template("post.html", num=id, blog_data=pass_info)

if __name__ == "__main__":
    app.run(debug=True)
