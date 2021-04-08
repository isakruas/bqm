## 1. Informações gerais

Esta plataforma foi desenvolvida por Isak Paulo de Andrade Ruas, sob orientação do Prof. Dr. Josué Antunes de Macêdo.

Esta plataforma origina-se do projeto "Desenvolvimento de um sistema hipermídia para elaboração de avaliações de matemática", desenvolvido com bolsa do Programa
Institucional de Bolsas de Iniciação em Desenvolvimento Tecnológico e Inovação (PIBITI) do Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq).

Atualmente, a plataforma encontra-se na versão de código 1.0.0

## 2. Objetivo

Ser um sistema disponibilizado on-line na internet de forma gratuita, destinado a auxiliar professores e professoras de matemática dos anos finais do ensino 
fundamental e ensino médio a elaborarem suas atividades avaliativas, com um banco de dados de questões de matemática organizadas conforme eixo temático, objeto de 
conhecimento, ciclo de ensino e nível de dificuldade.

## 3. Desenvolvimento e manutenção

Esta plataforma é de código aberto e gratuita, ou seja, qualquer pessoa poderá acessar, copiar, distribuir ou fazer novas versões, desde que respeitem os termos
previstos na General Public License (GNU) versão 3 de 29 junho de 2007.

O repositório oficial desta plataforma encontra-se disponível no Github e recebe constantemente atualizações de voluntários. Abaixo relacionamos os principais
colaboradores, como forma de agradecimento:

- [Jeferson Lopes Coutinho (desenvolvimento da versão mobile)](https://github.com/jeferson-BSI/bqm-mobile-)

## 3. Instalação para desenvolvimento 
```sh
mkdir dev
cd dev
python3 -m venv env
cd env/bin/
source ./activate
cd ../../
git clone https://github.com/isakruas/bqm.git
chmod -R 777 bqm
cd bqm
pip install -r requirements.txt
python manage.py migrate
python manage.py shell
exec(open('db.py').read())
# Ctrl+D para sair do shell
python manage.py runserver
```
