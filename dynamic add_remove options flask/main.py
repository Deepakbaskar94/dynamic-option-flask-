from flask import Flask, render_template, jsonify, request
# import psycopg2 #pip install psycopg2 
# import psycopg2.extras
    
app = Flask(__name__)
    
app.secret_key = "caircocoders-ednalan"
    
# DB_HOST = "localhost"
# DB_NAME = "sampledb"
# DB_USER = "postgres"
# DB_PASS = "admin"
        
# conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/postskill",methods=["POST","GET"])
def postskill():
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        skills = request.form.getlist('skill[]')
        for value in skills:  
            print(value)
        #     cur.execute("INSERT INTO skills (skillname) VALUES (%s)",[value])
        #     conn.commit()       
        # cur.close()
        msg = 'New record created successfully'    
    return jsonify(msg)


if __name__=="__main__":
    app.debug = True
    app.run(host ="0.0.0.0", port=5000 )
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)