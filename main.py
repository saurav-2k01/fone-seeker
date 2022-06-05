from flask import Flask, request,jsonify

app = Flask(__name__)
@app.route('/fone')
def fone():
    dial = request.args.get("dial-code", None)
    phone = request.args.get('phone', None)
    if (dial != None) and (phone != None):
        from Num_Seek import Num_Digger
        try:
            raw = jsonify(Num_Digger(dial, phone).Raw_Info())
            return raw
        except:
            print("Please enter a valid input.")
    else:
        pass
#"1","6108390872"

if __name__=="__main__":
    app.run(debug=True)
