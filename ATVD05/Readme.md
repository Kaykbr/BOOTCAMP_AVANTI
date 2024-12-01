/*
# ATVD05 - Aplicação de Classificação de Imagens

## Descrição
Este projeto é uma aplicação de classificação de imagens desenvolvida como parte do Bootcamp de Machine Learning da Atlântico Avanti. A aplicação permite o pré-processamento de imagens, segmentação e classificação utilizando modelos de machine learning.

## Funcionalidades
1. **Pré-processamento de Imagens**:
    - Redimensionamento
    - Conversão para escala de cinza
    - Ajuste de brilho e contraste
    - Filtros de suavização
    - Normalização

2. **Segmentação de Imagens**:
    - Thresholding (Limiarização)
    - Detecção de bordas
    - Segmentação por cor
    - Detecção de contornos
    - Watershed (Segmentação por bacias)

3. **Classificação de Imagens**:
    - Carregamento de imagens
    - Verificação de integridade e tamanho da imagem
    - Predição de classes utilizando modelos treinados

## Tecnologias Utilizadas
- ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
- ![Streamlit](https://img.shields.io/badge/Streamlit-0.84.0-red?logo=streamlit&logoColor=white)
- ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.5-orange?logo=tensorflow&logoColor=white)
- ![NumPy](https://img.shields.io/badge/NumPy-1.21-blue?logo=numpy&logoColor=white)
- ![Pillow](https://img.shields.io/badge/Pillow-8.2-green?logo=pillow&logoColor=white)
- ![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-yellow?logo=opencv&logoColor=white)

## Estrutura do Projeto
- `app.py`: Script principal da aplicação.
- `assets/`: Diretório contendo imagens e outros recursos utilizados na aplicação.

## Como Executar
1. **Pré-requisitos**:
    - Python 3.x instalado
    - Instalar as dependências:
      ```bash
      pip install streamlit tensorflow numpy pillow opencv-python
      ```

2. **Executar a Aplicação**:
    ```bash
    streamlit run app.py
    ```

## Dificuldades Enfrentadas
- Integração de diferentes bibliotecas de processamento de imagem e deep learning.
- Tratamento de imagens de baixa qualidade ou com formatos não suportados.
- Otimização do desempenho da aplicação para garantir uma experiência de usuário fluida.
- Implementação de técnicas avançadas de segmentação e classificação.
- Garantir a compatibilidade entre diferentes versões de bibliotecas e frameworks.
- Manutenção da precisão e velocidade do modelo de classificação.
- Desenvolvimento de uma interface de usuário intuitiva.

## Imagens do Projeto
![Intro](assets/intro.jpeg)
![Pré-processamento01](assets/preprocessaemnto01.jpeg)
![Pré-processamento02](assets/preprocessamento02.jpeg)
![Segmentacao01](assets/segmentacao01.jpeg)
![Segmentacao02](assets/segmentacao02.jpeg)
![Classificação01](assets/classificacao01.jpeg)
![Classificação02](assets/classificacao02.jpeg)

## Conclusão
Este projeto proporcionou uma experiência prática no desenvolvimento de uma aplicação completa de machine learning, desde o pré-processamento de dados até a classificação de imagens. As dificuldades enfrentadas contribuíram para um aprendizado significativo na área de visão computacional e desenvolvimento de aplicações interativas.
