# rpi-phoneGUI-bluetooth
Useful code and instructions in order to receive commands issued py a phone via bluetooth.

## O que é

Este código é implementado via systemd na inicialização do Raspberry Pi.
O acionamento é feito usando o componente de Bluetooth Client do MIT App Inventor.
O celular foi inicialmente pareado manualmente com o Raspberry Pi - é possível parear programaticamente.

## setup

Para o setup do raspberry PI, a partir do Raspbian, foi instalado:
```shell
apt-get install bluetooth libbluetooth-dev blueman bluez python-bluetooth
pip install pybluez
```

## boas práticas

O código python é capaz de receber (recv) e mandar(send) comandos.
Para o 'send', o design pattern é padronizar os X primeiros bytes com o tamanho da mensagem em bytes, e a mensagem concatenada. por exemplo: "008Bom dia!".


## to do

Estou passando a GUI do app Android para o Android Studio 3. Quando estiver pronto, vou passar para cá os principais componentes Manifest, Kotlin e XML.
