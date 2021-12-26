from flask import Flask
import random
app = Flask(__name__)
rand_number = random.randint(1,9)
print(rand_number)
starting_gif = '<center><img src = "https://media1.giphy.com/media/lpNYYtdY4mTkYYaeJZ/200w.webp?cid=ecf05e47i6j3y27of02xk853waea4vcsl75qtu55e6pwnjly&rid=200w.webp&ct=g"</img></center>'

@app.route('/')
def start_screen():
    return '<center><img src = "https://media1.giphy.com/media/lpNYYtdY4mTkYYaeJZ/200w.webp?cid=ecf05e47i6j3y27of02xk853waea4vcsl75qtu55e6pwnjly&rid=200w.webp&ct=g"</img></center>' \
           '<h1 style="text-align: center">Guess a number between 0 and 9<h1> ' \
           '<h2 style="text-align: center""> Place in the search-bar w/ a slash (i.e. 127.0.0.1:5000/5) <h2>'



@app.route('/<int:guess>')
def check_guess(guess):
    if guess == rand_number:
        return '<center><em><b><h1 style="color: green">YOU WON!!!</h1></em></b>' \
               '<img src= "https://media4.giphy.com/media/kyhua8yakRdRRRM6yI/200w.webp?cid=ecf05e47yi659zsnly48qnwmgtuyii67y9lkfpb8iplf7kf0&rid=200w.webp&ct=g" width=50%></center>'
    elif guess < rand_number:
        return '<center><h1 style="color: red">Too low! </h1>' \
               '<img src= "https://media4.giphy.com/media/P8jmgo10wMngFsPG2V/200w.webp?cid=ecf05e47txm49rfnad15f3bs9mp3baus32upr2ggkr5snj33&rid=200w.webp&ct=g" >' \
               '<h2>Guess again.</h2></center> '
    elif guess > rand_number:
        return '<center><h1 style="color: purple">Too high</h1>' \
               '<img src= "https://media0.giphy.com/media/3HzccMZXz2x84V0bU2/giphy.webp?cid=ecf05e473yb0a3gdrhuptico9fpkb165g4683ajwdmz4yl0h&rid=giphy.webp&ct=g" height=70%>' \
               '<h2>Guess again.</h2></center> '


if __name__ == '__main__':
    app.run(debug=True)  #s saves & reloads code.
