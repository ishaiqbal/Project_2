from flask import Flask, render_template, redirect, jsonify 
import pandas as pd
import json 
#import sqlalchemy
#from sqlalchemy import create_engine
#from config import dbuser, dbpassword 

#rds_connection_string = f"{dbuser}:{dbpassword}@localhost:5432/viruses"
#engine = create_engine(f'postgresql://{rds_connection_string}')

app = Flask(__name__)

@app.route("/coronavirus")
def coronavirus():
  
    coronavirus_csv = "Final_Dataset/final_coronavirus.csv"
    coronavirus = pd.read_csv(coronavirus_csv) 

    #coronavirus.to_sql(name='coronavirus', con=engine, if_exists='replace', index=False)

    return coronavirus.to_json(orient='records')

@app.route("/ebola")
def ebola():
    ebola_csv = "Final_Dataset/final_ebola.csv"
    ebola = pd.read_csv(ebola_csv) 

    #ebola.to_sql(name='ebola', con=engine, if_exists='replace', index=False)

    return ebola.to_json(orient='records')

    json.dump(ebola, jsonfile)

@app.route("/sars")
def sars():
    sars_csv = "Final_Dataset/final_sars.csv"
    sars = pd.read_csv(sars_csv) 

    #sars.to_sql(name='sars', con=engine, if_exists='replace', index=False)

    return sars.to_json(orient='records')
    
    

if __name__=="__main__":
    app.run(debug=True)