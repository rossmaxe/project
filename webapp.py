from flask import Flask, request, render_template
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/sydney") 
def sydney(name=None):         
	return render_template ('sydney.html', name=name)
@app.route("/newzealand") 
def newzealand(name=None): 
 return render_template ('newzealand.html', name=name)
	
@app.route("/thailand") 
def thailand(name=None): 
 return render_template ('thailand.html', name=name)
	
if __name__ == "__main__":     
	app.run()
