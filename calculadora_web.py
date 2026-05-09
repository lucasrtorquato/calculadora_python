import streamlit as st
import math

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Calculadora Web",
    page_icon="🧮",
    layout="centered"
)

# ==========================================
# ESTILO PERSONALIZADO
# ==========================================
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
        }

        .titulo {
            text-align: center;
            color: white;
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .subtitulo {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 30px;
        }

        .resultado {
            background-color: #1e293b;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: #38bdf8;
            font-size: 28px;
            font-weight: bold;
            margin-top: 30px;
            border: 1px solid #334155;
        }

        .stButton>button {
            width: 100%;
            height: 50px;
            border-radius: 12px;
            background-color: #2563eb;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
        }

        .stButton>button:hover {
            background-color: #1d4ed8;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# TÍTULO
# ==========================================
st.markdown(
    '<div class="titulo">🧮 Calculadora Web</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Calculadora moderna usando Streamlit</div>',
    unsafe_allow_html=True
)

# ==========================================
# CAMPOS
# ==========================================
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input(
        "Primeiro número",
        value=0.0,
        format="%.2f"
    )

with col2:
    num2 = st.number_input(
        "Segundo número",
        value=0.0,
        format="%.2f"
    )

# ==========================================
# OPERAÇÕES
# ==========================================
operacao = st.selectbox(
    "Selecione a operação",
    [
        "Adição",
        "Subtração",
        "Multiplicação",
        "Divisão",
        "Exponenciação",
        "Módulo",
        "Raiz Quadrada",
        "Porcentagem"
    ]
)

# ==========================================
# CÁLCULO
# ==========================================
resultado = None

if st.button("CALCULAR"):

    try:

        if operacao == "Adição":
            resultado = num1 + num2

        elif operacao == "Subtração":
            resultado = num1 - num2

        elif operacao == "Multiplicação":
            resultado = num1 * num2

        elif operacao == "Divisão":
            if num2 == 0:
                st.error("❌ Divisão por zero!")
            else:
                resultado = num1 / num2

        elif operacao == "Exponenciação":
            resultado = num1 ** num2

        elif operacao == "Módulo":
            if num2 == 0:
                st.error("❌ Módulo por zero!")
            else:
                resultado = num1 % num2

        elif operacao == "Raiz Quadrada":
            if num1 < 0:
                st.error("❌ Número negativo!")
            else:
                resultado = math.sqrt(num1)

        elif operacao == "Porcentagem":
            resultado = (num1 * num2) / 100

        # Mostrar resultado
        if resultado is not None:
            st.markdown(
                f'''
                <div class="resultado">
                    Resultado:<br>{resultado}
                </div>
                ''',
                unsafe_allow_html=True
            )

    except Exception as erro:
        st.error(f"Erro: {erro}")

# ==========================================
# RODAPÉ
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)

st.caption("Desenvolvido com Python + Streamlit")