from flask import Flask, request, render_template #Flask é o nome do "motor" que faz o site funcionar. Request é o que o usuário digita. Render_template é o que "desenha" a página.
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from src.pipeline.predict_pipeline import CustomData, PredictPipeline 

application = Flask(__name__) #Aqui criamos o "site" em memória.

app = application

@app.route('/') #Isso é como dizer: "Quando alguém entrar no endereço principal do site, execute a função index".
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST']) #Isso diz: "Crie uma página que funcione quando o usuário clicar em 'Enviar' (POST) ou se alguém tentar acessá-la diretamente (GET)".
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),#Pega o valor do campo 'gender' do formulário HTML.
            race_ethnicity=request.form.get('race_ethnicity'),#Mesma lógica do passo anterior
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),#Converte o valor para inteiro.
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) #Debug=True faz com que o site reinicie automaticamente toda vez que salvamos o código.
