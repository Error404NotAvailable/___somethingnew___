from flask import Flask, jsonify
app = Flask(__name__)



@app.route("/quotes")
def index():
    return jsonify(
        {

            "id": '1',
            "quote": "I DON'T GIVE A SHIT ABOUT MONEY.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '2',
            "quote": "Hackers. We inherently trust no one, including each other.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '3',
            "quote": "I've never found it hard to hack most people. If you listen to them, watch them, their vulnerabilities are like a neon sign screwed into their heads.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '4',
            "quote": "I'm just playing my best move.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '5',
            "quote": "Trust yourself. You'll do what's right.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '6',
            "quote": "The World is a dangerous place, Elliot, not because of those who do evil, but because of those who look on and do nothing.",
            "speaker": "MR. ROBOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '7',
            "quote": "The devil is at his strongest while we're looking the other way, like a program running in the background silently, while we're busy doing other shit.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '8',
            "quote": "On the way there, I'd always pick the safest car ‘cause I looked forward to our trips to the city so much. Then on the way back, I'd pick the most dangerous ones… 'cause I hated going home.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '9',
            "quote": "World catastrophes like this, they aren't caused by lone wolves like you. They occur because men like me allow them. You just had to stumble onto one of them.",
            "speaker": "PHILLIP PRICE.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '10',
            "quote": "I’m good at reading people. My secret, I look for the worst in them.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '11',
            "quote": "Every relationship is a power struggle. Some of us need to be controlled.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '12',
            "quote": "Repeating the same tasks each day without ever having to think about them, isn't that what everybody does? Keep things on repeat to go along with their NCISes and Lexapro. Isn't that where it's comfortable? In the sameness?",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '13',
            "quote": "When you delete something, you're making a choice to destroy it. To never see it again.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '14',
            "quote": "A bug is never just a mistake. It represents something bigger. An error of thinking. That makes you who you are.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '15',
            "quote": "Hello, friend. Hello, friend. That's lame. Maybe I should give you a name. But that's a slippery slope. You're only in my head. We have to remember that.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '16',
            "quote": "I do see the beauty in the rules, the invisible code of chaos hiding behind the menacing face of order.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '17',
            "quote": "Deletion. When you make that decision, there's always that moment of hesitation. That annoying 'Are you sure?' dialogue box, and then you have to make a decision. Yes or no.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '18',
            "quote": "This is the world we live in. People relying on each other's mistakes to manipulate one another and use one another, even relate to one another. A warm, messy circle of humanity.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '19',
            "quote": "How do I take off a mask when it stops being a mask, when it's as much a part of me as I am?",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '20',
            "quote": "We're all living in each other's paranoia.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '21',
            "quote": "Life is so much easier when you're numb.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        },
        {
            "id": '22',
            "quote": "Annihilation is always the answer. We destroy parts of ourselves every day. We Photoshop our parts away. We edit the parts we hate about ourselves, modify the parts we think people hate. We curate our identity, carve it, distill it. Krista's wrong. Annihilation is all we are.",
            "speaker": "ELLIOT.",
            "pic": "https://www.pngjoy.com/pngm/627/8663279_rami-malek-elliot-alderson-transparent-png.png"
        }
    )


if __name__ == '__main__':
    app.run()
