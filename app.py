from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf import Form



app = Flask(__name__)# instentiates Flask app and allows python to access static and template folders



@app.route('/index', methods=["GET", "POST"]) 

def index():
    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("index.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("index.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("index.html")


@app.route('/about', methods=["GET", "POST"]) 

def about():
    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/About/about.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/About/about.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/About/about.html")


@app.route('/our_work', methods=["GET", "POST"]) 

def our_work():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Our work/our_work.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Our work/our_work.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML
    
    return render_template("/Pages/Our work/our_work.html")


@app.route('/data_cabling', methods=["GET", "POST"]) 

def data_cabling():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Services/data_cabling.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Services/data_cabling.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/Services/data_cabling.html")


@app.route('/CCTV', methods=["GET", "POST"]) 

def CCTV():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Services/CCTV.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Services/CCTV.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/Services/CCTV.html")


@app.route('/rewiring', methods=["GET", "POST"]) 

def rewiring():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Services/rewiring.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Services/rewiring.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/Services/rewiring.html")


@app.route('/maintenance', methods=["GET", "POST"])

def maintenance():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Services/maintenance.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Services/maintenance.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/Services/maintenance.html")


@app.route('/refurbishment', methods=["GET", "POST"])

def refurbishment():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Services/refurbishment.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Services/refurbishment.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/Services/refurbishment.html")



@app.route('/IT', methods=["GET", "POST"])

def IT():

    #note: the HTML dropdown for language selection is hidden with CSS
    if request.method == "POST" and "translate" in request.form:#checks the method and whether the 
        #passed value is translate upon clicking a button to translate the web page
        operation = request.form["operation"]
        if operation == "russian":#if option's value in the HTML file is "russian"
            language1 = "russian"
            return render_template("/Pages/Services/IT.html", a=language1)#"a" variable used for jinja to react 
            #on the function to choose russian version of HTML
    
        elif operation == "english":#if option's value in the HTML file is "english"
            language2 = "english"
            return render_template("/Pages/Services/IT.html", b=language2)#"b" variable used for jinja to react 
            #on the function to choose english version of HTML

    return render_template("/Pages/Services/IT.html")

if __name__ == '__main__': #The statement is saying: Is this file being run directly 
#by python or is it being imported? Python assigns the name "__main__" to the script 
# when the script is executed. If the script is imported from another script, the 
# script keeps it given name (e.g. hello.py). In our case we are executing the script. 
# Therefore, __name__ will be equal to "__main__". That means the if conditional 
# statement is satisfied and the app.run() method will be executed. This technique 
# allows the programmer to have control over script’s behavior.

    app.run(debug=True)#Notice also that we are setting the debug parameter to true. That will print out 
    #possible Python errors on the web page helping us trace the errors. However, in a production environment, 
    # you would want to set it to False as to avoid any security issues.