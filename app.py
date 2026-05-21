import streamlit as st
st.title('LS Drive - Aluguel de carros')
st.sidebar.title('Escolha o seu modelo')
st.sidebar.image('logo.png')

carros = ['BMW', 'Mustang', 'Porsche', 'Jaguar', 'Chevrolet','Fiat', 'Corsa 97' ,'Civic' ,'Parati' ] 

opçao = st.sidebar.selectbox('Escolha o carro que foi alugado' , carros)
# st.sidebar.image('BMW.png')
# st.sidebar.image('Mustang.png')
# st.sidebar.image('Porsche.png')
# st.sidebar.image('Jaguar.png')
# st.sidebar.image('Chevrolet.png')
# st.sidebar.image('Fiat.png')
# st.sidebar.image('Corsa 97.png')
# st.sidebar.image('Civic.png')
# st.sidebar.image('Parati.png')
st.image(f'{opçao}.png')
st.markdown(f'## Você alugou o modelo: {opçao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opçao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opçao}?')

if opçao =='BMW':
    diaria = 500

elif opçao == 'Mustang':
    diaria = 460

elif opçao == 'Porsche':
    diaria = 550

elif opçao == 'Jaguar':
    diaria = 550

elif opçao == 'Chevrolet':
    diaria = 350

elif opçao == 'Fiat':
    diaria = 350

elif opçao == 'Corsa 97':
    diaria = 300

elif opçao == 'Civic':
    diaria = 400

elif opçao == 'Parati':
    diaria = 250

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.50
    aluguel_total  = total_dias+total_km


st.warning(f'Voce alugou o {opçao} por {dias} dias e rodou {km} km. O valor total a pagar é R$ {aluguel_total:.2f}')