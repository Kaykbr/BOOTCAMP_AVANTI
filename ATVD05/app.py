import streamlit as st
import numpy as np
import cv2
try:
    from PIL import Image, ImageOps, ImageEnhance
except ImportError:
    st.error("Erro ao importar PIL. Execute: pip install Pillow>=10.0.0")
    st.stop()

# Tente importar TensorFlow de maneira alternativa
try:
    import tensorflow as tf
    if tf.__version__.startswith('2'):
        from tensorflow.keras import applications
        mobilenet = applications.MobileNetV2(weights='imagenet')
        preprocess_input = applications.mobilenet_v2.preprocess_input
        decode_predictions = applications.mobilenet_v2.decode_predictions
    else:
        st.error("Versão do TensorFlow incompatível. Por favor, instale a versão 2.17.1")
        st.stop()
except ImportError as e:
    st.error(f"Erro ao importar TensorFlow: {e}")
    st.error("Tente reinstalar o TensorFlow: pip install tensorflow==2.17.1")
    st.stop()

def app():
    st.set_page_config(page_title="Visão Computacional Demo", layout="wide")
    st.title("📷 Demonstração de Visão Computacional")
    
    # Menu lateral com opções
    menu = ["Introdução", "Pré-processamento", "Segmentação", "Classificação"]
    choice = st.sidebar.selectbox("Navegação", menu)
    
    if choice == "Introdução":
        mostrar_introducao()
    elif choice == "Pré-processamento":
        preprocessamento()
    elif choice == "Segmentação":
        segmentacao()
    elif choice == "Classificação":
        classificacao()

def mostrar_introducao():
    st.header("Introdução à Visão Computacional")
    st.write("""
    ### Bibliotecas Principais:
    - **OpenCV (cv2)**: Processamento de imagens e visão computacional
    - **PIL (Python Imaging Library)**: Manipulação de imagens
    - **TensorFlow/Keras**: Deep Learning para visão computacional
    - **NumPy**: Computação numérica e manipulação de arrays
    
    ### O que veremos:
    1. **Pré-processamento**: Técnicas básicas de manipulação de imagens
    2. **Segmentação**: Separação de objetos em imagens
    3. **Classificação**: Reconhecimento de objetos com Deep Learning
    """)

def preprocessamento():
    st.header("1. Pré-processamento de Imagens")
    
    # Área explicativa
    with st.expander("ℹ️ Sobre Pré-processamento"):
        st.write("""
        O pré-processamento é fundamental para preparar imagens para análise:
        - Redimensionamento
        - Conversão para escala de cinza
        - Ajuste de brilho e contraste
        - Filtros de suavização
        - Normalização
        """)
    
    uploaded_file = st.file_uploader("Carregar imagem", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        try:
            img = Image.open(uploaded_file).convert('RGB')  # Força conversão para RGB
            img_array = np.array(img)
            if len(img_array.shape) != 3:
                st.error("Por favor, carregue uma imagem colorida (RGB).")
                return
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(img, caption="Original", use_container_width=True)
            
            with col2:
                # Controles interativos
                opcao = st.selectbox(
                    "Escolha o tipo de processamento",
                    ["Escala de Cinza", "Blur", "Ajuste de Brilho", "Normalização"]
                )
                
                if opcao == "Escala de Cinza":
                    img_proc = img.convert('L')
                    st.image(img_proc, caption="Escala de Cinza", use_container_width=True)
                
                elif opcao == "Blur":
                    kernel_size = st.slider("Intensidade do Blur", 1, 99, 5, step=2)
                    img_array = np.array(img)
                    img_proc = cv2.GaussianBlur(img_array, (kernel_size, kernel_size), 0)
                    st.image(img_proc, caption="Imagem com Blur", use_container_width=True)
                
                elif opcao == "Ajuste de Brilho":
                    brilho = st.slider("Brilho", -100, 100, 0)
                    img_array = np.array(img)
                    img_proc = cv2.convertScaleAbs(img_array, alpha=1, beta=brilho)
                    st.image(img_proc, caption="Brilho Ajustado", use_container_width=True)
                
                elif opcao == "Normalização":
                    img_array = np.array(img).astype(float) / 255.0
                    st.image(img_array, caption="Normalizada", use_container_width=True)

        except Exception as e:
            st.error(f"Erro ao processar imagem: {str(e)}")
            return

def segmentacao():
    st.header("2. Segmentação de Imagens")
    
    with st.expander("ℹ️ Sobre Segmentação"):
        st.write("""
        A segmentação divide a imagem em regiões de interesse:
        - Thresholding (Limiarização)
        - Detecção de bordas
        - Segmentação por cor
        - Detecção de contornos
        - Watershed (Segmentação por bacias)
        """)
    
    uploaded_file = st.file_uploader("Carregar imagem", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        try:
            img = Image.open(uploaded_file).convert('RGB')
            img_array = np.array(img)
            if img_array.size == 0:
                st.error("Imagem inválida.")
                return
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(img, caption="Original", use_container_width=True)
            
            with col2:
                metodo = st.selectbox(
                    "Escolha o método de segmentação",
                    ["Threshold", "Canny Edge", "Color Segmentation", "Contours", "Watershed"]
                )
                
                if metodo == "Threshold":
                    thresh_type = st.selectbox("Tipo de Threshold", 
                                             ["Binary", "Binary Inv", "Adaptive Mean", "Otsu"])
                    thresh = st.slider("Valor do Threshold", 0, 255, 127)
                    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                    
                    if thresh_type == "Binary":
                        _, img_thresh = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
                    elif thresh_type == "Binary Inv":
                        _, img_thresh = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY_INV)
                    elif thresh_type == "Adaptive Mean":
                        block_size = st.slider("Tamanho do Bloco", 3, 99, 11, step=2)
                        C = st.slider("Constante C", -30, 30, 2)
                        img_thresh = cv2.adaptiveThreshold(img_gray, 255, 
                                                         cv2.ADAPTIVE_THRESH_MEAN_C,
                                                         cv2.THRESH_BINARY, block_size, C)
                    else:  # Otsu
                        _, img_thresh = cv2.threshold(img_gray, 0, 255, 
                                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    
                    st.image(img_thresh, caption=f"Threshold - {thresh_type}", 
                            use_container_width=True)
                
                elif metodo == "Canny Edge":
                    low = st.slider("Limiar Inferior", 0, 255, 100)
                    high = st.slider("Limiar Superior", 0, 255, 200)
                    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                    img_edges = cv2.Canny(img_gray, low, high)
                    st.image(img_edges, caption="Detecção de Bordas", use_container_width=True)
                
                elif metodo == "Color Segmentation":
                    hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
                    cor = st.color_picker("Escolha uma cor para segmentar", "#00ff00")
                    # Converter cor RGB para HSV
                    rgb = tuple(int(cor.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                    hsv_cor = cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2HSV)[0][0]
                    
                    lower = np.array([hsv_cor[0]-10, 100, 100])
                    upper = np.array([hsv_cor[0]+10, 255, 255])
                    mask = cv2.inRange(hsv, lower, upper)
                    st.image(mask, caption="Segmentação por Cor", use_container_width=True)
                
                elif metodo == "Contours":
                    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                    blur = cv2.GaussianBlur(img_gray, (5,5), 0)
                    thresh = st.slider("Threshold", 0, 255, 127)
                    _, binary = cv2.threshold(blur, thresh, 255, cv2.THRESH_BINARY)
                    
                    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, 
                                                 cv2.CHAIN_APPROX_SIMPLE)
                    
                    min_area = st.slider("Área Mínima", 0, 5000, 100)
                    img_contours = img_array.copy()
                    n_contours = 0
                    
                    for contour in contours:
                        area = cv2.contourArea(contour)
                        if area > min_area:
                            cv2.drawContours(img_contours, [contour], -1, (0,255,0), 2)
                            n_contours += 1
                    
                    st.image(img_contours, caption=f"Contornos Detectados: {n_contours}", 
                            use_container_width=True)
                
                elif metodo == "Watershed":
                    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                    _, thresh = cv2.threshold(img_gray, 0, 255, 
                                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                    
                    # Ruído de fundo
                    kernel = np.ones((3,3), np.uint8)
                    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
                    
                    # Área de fundo
                    sure_bg = cv2.dilate(opening, kernel, iterations=3)
                    
                    # Área de primeiro plano
                    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
                    _, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
                    sure_fg = np.uint8(sure_fg)
                    
                    # Região desconhecida
                    unknown = cv2.subtract(sure_bg, sure_fg)
                    
                    # Marcadores
                    _, markers = cv2.connectedComponents(sure_fg)
                    markers = markers + 1
                    markers[unknown == 255] = 0
                    
                    markers = cv2.watershed(img_array, markers)
                    img_array[markers == -1] = [255,0,0]
                    
                    st.image(img_array, caption="Watershed Segmentation", 
                            use_container_width=True)
                    
                    col_vis1, col_vis2 = st.columns(2)
                    with col_vis1:
                        st.image(sure_fg, caption="Primeiro Plano", use_container_width=True)
                    with col_vis2:
                        st.image(sure_bg, caption="Fundo", use_container_width=True)

        except Exception as e:
            st.error(f"Erro ao segmentar imagem: {str(e)}")
            return

@st.cache_resource(ttl=3600)  # Cache por 1 hora
def carregar_modelo():
    try:
        return mobilenet
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {str(e)}")
        return None

def classificacao():
    st.header("3. Classificação de Imagens")
    
    with st.expander("ℹ️ Sobre Classificação"):
        st.write("""
        Classificação de imagens usando deep learning:
        - Modelo: MobileNetV2 (pré-treinado no ImageNet)
        - 1000+ classes de objetos
        - Rápido e eficiente
        """)
    
    modelo = carregar_modelo()
    if modelo is None:
        st.error("Não foi possível carregar o modelo de classificação.")
        return
    
    uploaded_file = st.file_uploader("Carregar imagem", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        try:
            img = Image.open(uploaded_file).convert('RGB')
            st.image(img, caption="Imagem para classificação", width=300)
            
            # Verifica dimensões mínimas
            if img.size[0] < 224 or img.size[1] < 224:
                st.warning("A imagem é muito pequena. Recomenda-se imagens maiores que 224x224 pixels.")
            
            # Processamento com verificação de memória
            img = img.resize((224, 224), Image.Resampling.LANCZOS)
            x = np.array(img, dtype=np.float32)
            if x.size == 0:
                st.error("Erro ao processar a imagem.")
                return
                
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            
            # Predição
            with st.spinner('Classificando imagem...'):
                predictions = modelo.predict(x)
                decoded = decode_predictions(predictions, top=5)[0]
            
            # Resultados
            st.write("### Resultados:")
            for i, (id, label, prob) in enumerate(decoded):
                st.progress(float(prob))
                st.write(f"{i+1}. {label.title()}: {prob*100:.2f}%")

        except tf.errors.ResourceExhaustedError:
            st.error("Memória insuficiente para processar a imagem.")
        except Exception as e:
            st.error(f"Erro ao classificar imagem: {str(e)}")
            return

if __name__ == '__main__':
    app()
