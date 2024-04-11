# Sobre
Isso é pra brincar mesmo ok? Nada sério fiz em uma hora.

# Instalando obviamente Apenas Linux
Acho e deve ser a mesma coisa pra Windows mas o ROCm(placas AMD ainda não funcionam pra ele)

## Criando um ambiente virtual:
Isso vai criar uma pasta venv no seu diretório é aonde vamos instalar os pacotes
```sh
python -m venv venv
```

```sh
source /venv/bin/activate
```

## Torch
Primeiro temos de instalar o torch pro negócio funcionar
### AMD porque a força vermelha vem antes:

#### ROCm estável
Provavelmente compatível com modelos mais antigos
``` sh
pip3 install torch --index-url https://download.pytorch.org/whl/rocm5.7
```

#### ROCm instável
É a versão que eu usei pra testar os códigos.
```sh
pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/rocm6.0
```

Mais informações em [no site oficial do pytorch](https://pytorch.org/get-started/locally/)

### Nvidia
Não sei qual é a parada com a nvidia ter versões CUDA 11.8 e 12.1
```sh
pip install torch
```

### CPU

```
pip3 install torch --index-url https://download.pytorch.org/whl/cpu
```


## Instalando os requisitos
Depois de instalar o torch podemos instalar os outros requisitos do sistema, se eles forem instalados antes, provavelmente eles vão instalar juntos o torch pra Nvidia

```sh
pip install -r requirements.txt
```

Prontinho, depois disso você pode usar o modelo com os código que fiz.

# Comandos básico

Vai mostrar os argumentos, a maioria ainda não funciona, eu só adicionei pra dps qual é, fiz em uma hora
```sh
python src/main.py -h
```

## rodando o modelo

```sh
python src/main.py --path="caminho/do/arquivo.avi" \
--gpu=amd \
--extension=srt
```

```sh
python src/main.py --path="caminho/do/arquivo.mkv" \
--gpu=amd \
--extension=txt \
--task=translate
```

### Dicas:
Dá pra "enganar" o modelo passando o idioma que você quer a tradução do arquivo:

```sh
python src/main.py --path="caminho/do/arquivo.mp4" \
--gpu=amd \
--extension=srt \
--task=translate \
--language=portuguese
```
Se o arquivo estiver em inglês, ele vai traduzir pra português, ou tentar né, e se o arquivo estiver em português ele vai tentar traduzir pra inglês.


Por enquanto só funciona isso. Novamente fiz isso em uma hora.