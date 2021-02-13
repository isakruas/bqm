"""
pip3 freeze > requirements.txt
python3 manage.py collectstatic
python manage.py makemigrations inicio
python manage.py makemigrations usuario
python manage.py makemigrations questao
python manage.py makemigrations upload
python manage.py migrate
python manage.py shell

"""



from questao.models import NivelDeDificuldade
nivel_de_dificuldade_nome_1 = NivelDeDificuldade(nivel_de_dificuldade_nome= 'Fácil')
nivel_de_dificuldade_nome_1.save();
nivel_de_dificuldade_nome_2 = NivelDeDificuldade(nivel_de_dificuldade_nome= 'Médio')
nivel_de_dificuldade_nome_2.save();
nivel_de_dificuldade_nome_3 = NivelDeDificuldade(nivel_de_dificuldade_nome= 'Difícil')
nivel_de_dificuldade_nome_3.save();

from questao.models import Etapa
etapa_1 = Etapa(etapa_nome= 'Educação infantil - Bebês')
etapa_1.save();
etapa_2 = Etapa(etapa_nome= 'Educação infantil - Crianças bem pequenas')
etapa_2.save();
etapa_3 = Etapa(etapa_nome= 'Educação infantil - Crianças pequenas')
etapa_3.save();
etapa_4 = Etapa(etapa_nome= 'Ensino fundamental - Anos iniciais')
etapa_4.save();
etapa_5 = Etapa(etapa_nome= 'Ensino fundamental - Anos finais')
etapa_5.save();
etapa_6 = Etapa(etapa_nome= 'Ensino médio')
etapa_6.save();

from questao.models import ObjetoDeConhecimento
objeto_de_conhecimento_1 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 1,ano= 1,objeto_de_conhecimento_nome='Contagem de rotina; Contagem ascendente e descendente; Reconhecimento de números no contexto diário: indicação de quantidades, indicação de ordem ou indicação de código para a organização de informações.')
objeto_de_conhecimento_1.save();
objeto_de_conhecimento_2 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 1,ano= 1,objeto_de_conhecimento_nome='Quantificação de elementos de uma coleção: estimativas, contagem um a um, pareamento ou outros agrupamentos e comparação.')
objeto_de_conhecimento_2.save();
objeto_de_conhecimento_3 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 1,ano= 1,objeto_de_conhecimento_nome='Leitura, escrita e comparação de números naturais até 100); Reta numérica.')
objeto_de_conhecimento_3.save();
objeto_de_conhecimento_4 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 1,ano= 1,objeto_de_conhecimento_nome='Construção de fatos básicos da adição.')
objeto_de_conhecimento_4.save();
objeto_de_conhecimento_5 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 1,ano= 1,objeto_de_conhecimento_nome='Composição e decomposição de números naturais.')
objeto_de_conhecimento_5.save();
objeto_de_conhecimento_6 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 1,ano= 1,objeto_de_conhecimento_nome='Problemas envolvendo diferentes significados da adição e da subtração juntar, acrescentar, separar, retirar).')
objeto_de_conhecimento_6.save();
objeto_de_conhecimento_7 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 2,ano= 1,objeto_de_conhecimento_nome='Padrões figurais e numéricos: investigação de regularidades ou padrões em sequências.')
objeto_de_conhecimento_7.save();
objeto_de_conhecimento_8 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 2,ano= 1,objeto_de_conhecimento_nome='Sequências recursivas: observação de regras usadas utilizadas em seriações numéricas mais 1, mais 2, menos 1, menos 2, por exemplo).')
objeto_de_conhecimento_8.save();
objeto_de_conhecimento_9 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 3,ano= 1,objeto_de_conhecimento_nome='Localização de objetos e de pessoas no espaço, utilizando diversos pontos de referência e vocabulário apropriado.')
objeto_de_conhecimento_9.save();
objeto_de_conhecimento_10 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 3,ano= 1,objeto_de_conhecimento_nome='Figuras geométricas espaciais: reconhecimento e relações com objetos familiares do mundo físico.')
objeto_de_conhecimento_10.save();
objeto_de_conhecimento_11 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 3,ano= 1,objeto_de_conhecimento_nome='Figuras geométricas planas: reconhecimento do formato das faces de figuras geométricas espaciais.')
objeto_de_conhecimento_11.save();
objeto_de_conhecimento_12 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 4,ano= 1,objeto_de_conhecimento_nome='Medidas de comprimento, massa e capacidade: comparações e unidades de medida não convencionais.')
objeto_de_conhecimento_12.save();
objeto_de_conhecimento_13 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 4,ano= 1,objeto_de_conhecimento_nome='Medidas de tempo: unidades de medida de tempo, suas relações e o uso do calendário.')
objeto_de_conhecimento_13.save();
objeto_de_conhecimento_14 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 4,ano= 1,objeto_de_conhecimento_nome='Sistema monetário brasileiro: reconhecimento de cédulas e moedas.')
objeto_de_conhecimento_14.save();
objeto_de_conhecimento_15 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 5,ano= 1,objeto_de_conhecimento_nome='Noção de acaso.')
objeto_de_conhecimento_15.save();
objeto_de_conhecimento_16 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 5,ano= 1,objeto_de_conhecimento_nome='Leitura de tabelas e de gráficos de colunas simples.')
objeto_de_conhecimento_16.save();
objeto_de_conhecimento_17 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 5,ano= 1,objeto_de_conhecimento_nome='Coleta e organização de informações; Registros pessoais para comunicação de informações coletadas.')
objeto_de_conhecimento_17.save();
objeto_de_conhecimento_18 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 6,ano= 2,objeto_de_conhecimento_nome='Leitura, escrita, comparação e ordenação de números de até três ordens pela compreensão de características do sistema de numeração decimal valor posicional e papel do zero).')
objeto_de_conhecimento_18.save();
objeto_de_conhecimento_19 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 6,ano= 2,objeto_de_conhecimento_nome='Composição e decomposição de números naturais até 1000).')
objeto_de_conhecimento_19.save();
objeto_de_conhecimento_20 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 6,ano= 2,objeto_de_conhecimento_nome='Construção de fatos fundamentais da adição e da subtração.')
objeto_de_conhecimento_20.save();
objeto_de_conhecimento_21 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 6,ano= 2,objeto_de_conhecimento_nome='Problemas envolvendo diferentes significados da adição e da subtração juntar, acrescentar, separar, retirar).')
objeto_de_conhecimento_21.save();
objeto_de_conhecimento_22 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 6,ano= 2,objeto_de_conhecimento_nome='Problemas envolvendo adição de parcelas iguais multiplicação).')
objeto_de_conhecimento_22.save();
objeto_de_conhecimento_23 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 6,ano= 2,objeto_de_conhecimento_nome='Problemas envolvendo significados de dobro, metade, triplo e terça parte.')
objeto_de_conhecimento_23.save();
objeto_de_conhecimento_24 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 7,ano= 2,objeto_de_conhecimento_nome='Construção de sequências repetitivas e de sequências recursivas.')
objeto_de_conhecimento_24.save();
objeto_de_conhecimento_25 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 7,ano= 2,objeto_de_conhecimento_nome='Identificação de regularidade de sequências e determinação de elementos ausentes na sequência.')
objeto_de_conhecimento_25.save();
objeto_de_conhecimento_26 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 8,ano= 2,objeto_de_conhecimento_nome='Localização e movimentação de pessoas e objetos no espaço, segundo pontos de referência, e indicação de mudanças de direção e sentido.')
objeto_de_conhecimento_26.save();
objeto_de_conhecimento_27 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 8,ano= 2,objeto_de_conhecimento_nome='Esboço de roteiros e de plantas simples.')
objeto_de_conhecimento_27.save();
objeto_de_conhecimento_28 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 8,ano= 2,objeto_de_conhecimento_nome='Figuras geométricas espaciais cubo, bloco retangular, pirâmide, cone, cilindro e esfera): reconhecimento e características.')
objeto_de_conhecimento_28.save();
objeto_de_conhecimento_29 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 8,ano= 2,objeto_de_conhecimento_nome='Figuras geométricas planas círculo, quadrado, retângulo e triângulo): reconhecimento e características.')
objeto_de_conhecimento_29.save();
objeto_de_conhecimento_30 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 9,ano= 2,objeto_de_conhecimento_nome='Medida de comprimento: unidades não padronizadas e padronizadas metro, centímetro e milímetro).')
objeto_de_conhecimento_30.save();
objeto_de_conhecimento_31 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 9,ano= 2,objeto_de_conhecimento_nome='Medida de capacidade e de massa: unidades de medida não convencionais e convencionais litro, mililitro, cm3, grama e quilograma).')
objeto_de_conhecimento_31.save();
objeto_de_conhecimento_32 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 9,ano= 2,objeto_de_conhecimento_nome='Medidas de tempo: intervalo de tempo, uso do calendário, leitura de horas em relógios digitais e ordenação de datas.')
objeto_de_conhecimento_32.save();
objeto_de_conhecimento_33 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 9,ano= 2,objeto_de_conhecimento_nome='Sistema monetário brasileiro: reconhecimento de cédulas e moedas e equivalência de valores.')
objeto_de_conhecimento_33.save();
objeto_de_conhecimento_34 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 10,ano= 2,objeto_de_conhecimento_nome='Análise da ideia de aleatório em situações do cotidiano.')
objeto_de_conhecimento_34.save();
objeto_de_conhecimento_35 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 10,ano= 2,objeto_de_conhecimento_nome='Coleta, classificação e representação de dados em tabelas simples e de dupla entrada e em gráficos de colunas.')
objeto_de_conhecimento_35.save();
objeto_de_conhecimento_36 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Leitura, escrita, comparação e ordenação de números naturais de quatro ordens.')
objeto_de_conhecimento_36.save();
objeto_de_conhecimento_37 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Composição e decomposição de números naturais.')
objeto_de_conhecimento_37.save();
objeto_de_conhecimento_38 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Construção de fatos fundamentais da adição, subtração e multiplicação; Reta numérica.')
objeto_de_conhecimento_38.save();
objeto_de_conhecimento_39 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Procedimentos de cálculo mental e escrito) com números naturais: adição e subtração.')
objeto_de_conhecimento_39.save();
objeto_de_conhecimento_40 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Problemas envolvendo significados da adição e da subtração: juntar, acrescentar, separar, retirar, comparar e completar quantidades.')
objeto_de_conhecimento_40.save();
objeto_de_conhecimento_41 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Problemas envolvendo diferentes significados da multiplicação e da divisão: adição de parcelas iguais, configuração retangular, repartição em partes iguais e medida.')
objeto_de_conhecimento_41.save();
objeto_de_conhecimento_42 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 11,ano= 3,objeto_de_conhecimento_nome='Significados de metade, terça parte, quarta parte, quinta parte e décima parte.')
objeto_de_conhecimento_42.save();
objeto_de_conhecimento_43 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 12,ano= 3,objeto_de_conhecimento_nome='Identificação e descrição de regularidades em sequências numéricas recursivas.')
objeto_de_conhecimento_43.save();
objeto_de_conhecimento_44 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 12,ano= 3,objeto_de_conhecimento_nome='Relação de igualdade')
objeto_de_conhecimento_44.save();
objeto_de_conhecimento_45 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 13,ano= 3,objeto_de_conhecimento_nome='Localização e movimentação: representação de objetos e pontos de referência.')
objeto_de_conhecimento_45.save();
objeto_de_conhecimento_46 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 13,ano= 3,objeto_de_conhecimento_nome='Figuras geométricas espaciais cubo, bloco retangular, pirâmide, cone, cilindro e esfera): reconhecimento, análise de características e planificações.')
objeto_de_conhecimento_46.save();
objeto_de_conhecimento_47 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 13,ano= 3,objeto_de_conhecimento_nome='Figuras geométricas planas triângulo, quadrado, retângulo, trapézio e paralelogramo): reconhecimento e análise de características.')
objeto_de_conhecimento_47.save();
objeto_de_conhecimento_48 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 13,ano= 3,objeto_de_conhecimento_nome='Congruência de figuras geométricas planas.')
objeto_de_conhecimento_48.save();
objeto_de_conhecimento_49 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 14,ano= 3,objeto_de_conhecimento_nome='Significado de medida e de unidade de medida.')
objeto_de_conhecimento_49.save();
objeto_de_conhecimento_50 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 14,ano= 3,objeto_de_conhecimento_nome='Medidas de comprimento unidades não convencionais e convencionais): registro, instrumentos de medida, estimativas e comparações.')
objeto_de_conhecimento_50.save();
objeto_de_conhecimento_51 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 14,ano= 3,objeto_de_conhecimento_nome='Medidas de capacidade e de massa unidades não convencionais e convencionais): registro, estimativas e comparações.')
objeto_de_conhecimento_51.save();
objeto_de_conhecimento_52 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 14,ano= 3,objeto_de_conhecimento_nome='Comparação de áreas por superposição.')
objeto_de_conhecimento_52.save();
objeto_de_conhecimento_53 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 14,ano= 3,objeto_de_conhecimento_nome='Medidas de tempo: leitura de horas em relógios digitais e analógicos, duração de eventos e reconhecimento de relações entre unidades de medida de tempo.')
objeto_de_conhecimento_53.save();
objeto_de_conhecimento_54 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 14,ano= 3,objeto_de_conhecimento_nome='Sistema monetário brasileiro: estabelecimento de equivalências de um mesmo valor na utilização de diferentes cédulas e moedas.')
objeto_de_conhecimento_54.save();
objeto_de_conhecimento_55 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 15,ano= 3,objeto_de_conhecimento_nome='Análise da ideia de acaso em situações do cotidiano: espaço amostral.')
objeto_de_conhecimento_55.save();
objeto_de_conhecimento_56 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 15,ano= 3,objeto_de_conhecimento_nome='Leitura, interpretação e representação de dados em tabelas de dupla entrada e gráficos de barras.')
objeto_de_conhecimento_56.save();
objeto_de_conhecimento_57 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 15,ano= 3,objeto_de_conhecimento_nome='Coleta, classificação e representação de dados referentes a variáveis categóricas, por meio de tabelas e gráficos.')
objeto_de_conhecimento_57.save();
objeto_de_conhecimento_58 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Sistema de numeração decimal: leitura, escrita, comparação e ordenação de números naturais de até cinco ordens.')
objeto_de_conhecimento_58.save();
objeto_de_conhecimento_59 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Composição e decomposição de um número natural de até cinco ordens, por meio de adições e multiplicações por potências de 10.')
objeto_de_conhecimento_59.save();
objeto_de_conhecimento_60 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Propriedades das operações para o desenvolvimento de diferentes estratégias de cálculo com números naturais.')
objeto_de_conhecimento_60.save();
objeto_de_conhecimento_61 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Problemas envolvendo diferentes significados da multiplicação e da divisão: adição de parcelas iguais, configuração retangular, proporcionalidade, repartição equitativa e medida.')
objeto_de_conhecimento_61.save();
objeto_de_conhecimento_62 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Problemas de contagem.')
objeto_de_conhecimento_62.save();
objeto_de_conhecimento_63 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Números racionais: frações unitárias mais usuais 1/2, 1/3, 1/4, 1/5, 1/10 e 1/100).')
objeto_de_conhecimento_63.save();
objeto_de_conhecimento_64 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 16,ano= 4,objeto_de_conhecimento_nome='Números racionais: representação decimal para escrever valores do sistema monetário brasileiro.')
objeto_de_conhecimento_64.save();
objeto_de_conhecimento_65 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 17,ano= 4,objeto_de_conhecimento_nome='Sequência numérica recursiva formada por múltiplos de um número natural.')
objeto_de_conhecimento_65.save();
objeto_de_conhecimento_66 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 17,ano= 4,objeto_de_conhecimento_nome='Sequência numérica recursiva formada por números que deixam o mesmo resto ao ser divididos por um mesmo número natural diferente de zero.')
objeto_de_conhecimento_66.save();
objeto_de_conhecimento_67 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 17,ano= 4,objeto_de_conhecimento_nome='Relações entre adição e subtração e entre multiplicação e divisão.')
objeto_de_conhecimento_67.save();
objeto_de_conhecimento_68 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 17,ano= 4,objeto_de_conhecimento_nome='Propriedades da igualdade.')
objeto_de_conhecimento_68.save();
objeto_de_conhecimento_69 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 18,ano= 4,objeto_de_conhecimento_nome='Localização e movimentação: pontos de referência, direção e sentid;  Paralelismo e perpendicularismo.')
objeto_de_conhecimento_69.save();
objeto_de_conhecimento_70 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 18,ano= 4,objeto_de_conhecimento_nome='Figuras geométricas espaciais prismas e pirâmides): reconhecimento, representações, planificações e características.')
objeto_de_conhecimento_70.save();
objeto_de_conhecimento_71 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 18,ano= 4,objeto_de_conhecimento_nome='Ângulos retos e não retos: uso de dobraduras, esquadros e softwares.')
objeto_de_conhecimento_71.save();
objeto_de_conhecimento_72 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 18,ano= 4,objeto_de_conhecimento_nome='Simetria de reflexão.')
objeto_de_conhecimento_72.save();
objeto_de_conhecimento_73 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 19,ano= 4,objeto_de_conhecimento_nome='Medidas de comprimento, massa e capacidade: estimativas, utilização de instrumentos de medida e de unidades de medida convencionais mais usuais.')
objeto_de_conhecimento_73.save();
objeto_de_conhecimento_74 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 19,ano= 4,objeto_de_conhecimento_nome='Áreas de figuras construídas em malhas quadriculadas.')
objeto_de_conhecimento_74.save();
objeto_de_conhecimento_75 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 19,ano= 4,objeto_de_conhecimento_nome='Medidas de tempo: leitura de horas em relógios digitais e analógicos, duração de eventos e relações entre unidades de medida de tempo.')
objeto_de_conhecimento_75.save();
objeto_de_conhecimento_76 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 19,ano= 4,objeto_de_conhecimento_nome='Medidas de temperatura em grau Celsius: construção de gráficos para indicar a variação da temperatura mínima e máxima) medida em um dado dia ou em uma semana.')
objeto_de_conhecimento_76.save();
objeto_de_conhecimento_77 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 19,ano= 4,objeto_de_conhecimento_nome='Problemas utilizando o sistema monetário brasileiro.')
objeto_de_conhecimento_77.save();
objeto_de_conhecimento_78 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 20,ano= 4,objeto_de_conhecimento_nome='Análise de chances de eventos aleatórios.')
objeto_de_conhecimento_78.save();
objeto_de_conhecimento_79 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 20,ano= 4,objeto_de_conhecimento_nome='Leitura, interpretação e representação de dados em tabelas de dupla entrada, gráficos de colunas simples e agrupadas, gráficos de barras e colunas e gráficos pictóricos.')
objeto_de_conhecimento_79.save();
objeto_de_conhecimento_80 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 20,ano= 4,objeto_de_conhecimento_nome='Diferenciação entre variáveis categóricas e variáveis numéricas; Coleta, classificação e representação de dados de pesquisa realizada.')
objeto_de_conhecimento_80.save();
objeto_de_conhecimento_81 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Sistema de numeração decimal: leitura, escrita e ordenação de números naturais de até seis ordens).')
objeto_de_conhecimento_81.save();
objeto_de_conhecimento_82 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Números racionais expressos na forma decimal e sua representação na reta numérica.')
objeto_de_conhecimento_82.save();
objeto_de_conhecimento_83 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Representação fracionária dos números racionais: reconhecimento, significados, leitura e representação na reta numérica.')
objeto_de_conhecimento_83.save();
objeto_de_conhecimento_84 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Comparação e ordenação de números racionais na representação decimal e na fracionária utilizando a noção de equivalência.')
objeto_de_conhecimento_84.save();
objeto_de_conhecimento_85 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Cálculo de porcentagens e representação fracionária.')
objeto_de_conhecimento_85.save();
objeto_de_conhecimento_86 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Problemas: adição e subtração de números naturais e números racionais cuja representação decimal é finita.')
objeto_de_conhecimento_86.save();
objeto_de_conhecimento_87 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Problemas: multiplicação e divisão de números racionais cuja representação decimal é finita por números naturais.')
objeto_de_conhecimento_87.save();
objeto_de_conhecimento_88 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 21,ano= 5,objeto_de_conhecimento_nome='Problemas de contagem do tipo: “Se cada objeto de uma coleção A for combinado com todos os elementos de uma coleção B, quantos agrupamentos desse tipo podem ser formados?”')
objeto_de_conhecimento_88.save();
objeto_de_conhecimento_89 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 22,ano= 5,objeto_de_conhecimento_nome='Propriedades da igualdade e noção de equivalência.')
objeto_de_conhecimento_89.save();
objeto_de_conhecimento_90 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 22,ano= 5,objeto_de_conhecimento_nome='Grandezas diretamente proporcionais; Problemas envolvendo a partição de um todo em duas partes proporcionais.')
objeto_de_conhecimento_90.save();
objeto_de_conhecimento_91 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 23,ano= 5,objeto_de_conhecimento_nome='Plano cartesiano: coordenadas cartesianas 1º quadrante) e representação de deslocamentos no plano cartesiano.')
objeto_de_conhecimento_91.save();
objeto_de_conhecimento_92 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 23,ano= 5,objeto_de_conhecimento_nome='Figuras geométricas espaciais: reconhecimento, representações, planificações e características.')
objeto_de_conhecimento_92.save();
objeto_de_conhecimento_93 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 23,ano= 5,objeto_de_conhecimento_nome='Figuras geométricas planas: características, representações e ângulos.')
objeto_de_conhecimento_93.save();
objeto_de_conhecimento_94 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 23,ano= 5,objeto_de_conhecimento_nome='Ampliação e redução de figuras poligonais em malhas quadriculadas: reconhecimento da congruência dos ângulos e da proporcionalidade dos lados correspondentes.')
objeto_de_conhecimento_94.save();
objeto_de_conhecimento_95 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 24,ano= 5,objeto_de_conhecimento_nome='Medidas de comprimento, área, massa, tempo, temperatura e capacidade: utilização de unidades convencionais e relações entre as unidades de medida mais usuais.')
objeto_de_conhecimento_95.save();
objeto_de_conhecimento_96 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 24,ano= 5,objeto_de_conhecimento_nome='Áreas e perímetros de figuras poligonais: algumas relações.')
objeto_de_conhecimento_96.save();
objeto_de_conhecimento_97 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 24,ano= 5,objeto_de_conhecimento_nome='Noção de volume.')
objeto_de_conhecimento_97.save();
objeto_de_conhecimento_98 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 25,ano= 5,objeto_de_conhecimento_nome='Espaço amostral: análise de chances de eventos aleatórios.')
objeto_de_conhecimento_98.save();
objeto_de_conhecimento_99 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 25,ano= 5,objeto_de_conhecimento_nome='Cálculo de probabilidade de eventos equiprováveis.')
objeto_de_conhecimento_99.save();
objeto_de_conhecimento_100 = ObjetoDeConhecimento(etapa=4,unidade_tematica= 25,ano= 5,objeto_de_conhecimento_nome='Leitura, coleta, classificação interpretação e representação de dados em tabelas de dupla entrada, gráfico de colunas agrupadas, gráficos pictóricos e gráfico de linhas.')
objeto_de_conhecimento_100.save();
objeto_de_conhecimento_101 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Sistema de numeração decimal: características, leitura, escrita e comparação de números naturais e de números racionais representados na forma decimal.')
objeto_de_conhecimento_101.save();
objeto_de_conhecimento_102 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Operações adição, subtração, multiplicação, divisão e potenciação) com números naturais; Divisão euclidiana.')
objeto_de_conhecimento_102.save();
objeto_de_conhecimento_103 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Fluxograma para determinar a paridade de um número natural; Múltiplos e divisores de um número natural; Números primos e compostos.')
objeto_de_conhecimento_103.save();
objeto_de_conhecimento_104 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Frações: significados parte/todo, quociente equivalência, comparação, adição e subtração; cálculo da fração de um número natural; adição e subtração de frações.')
objeto_de_conhecimento_104.save();
objeto_de_conhecimento_105 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Operações adição, subtração, multiplicação, divisão e potenciação) com números racionais.')
objeto_de_conhecimento_105.save();
objeto_de_conhecimento_106 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Aproximação de números para múltiplos de potências de 10.')
objeto_de_conhecimento_106.save();
objeto_de_conhecimento_107 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 26,ano= 6,objeto_de_conhecimento_nome='Cálculo de porcentagens por meio de estratégias diversas, sem fazer uso da “regra de três”.')
objeto_de_conhecimento_107.save();
objeto_de_conhecimento_108 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 27,ano= 6,objeto_de_conhecimento_nome='Propriedades da igualdade.')
objeto_de_conhecimento_108.save();
objeto_de_conhecimento_109 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 27,ano= 6,objeto_de_conhecimento_nome='Problemas que tratam da partição de um todo em duas partes desiguais, envolvendo razões entre as partes e entre uma das partes e o todo.')
objeto_de_conhecimento_109.save();
objeto_de_conhecimento_110 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 28,ano= 6,objeto_de_conhecimento_nome='Plano cartesiano: associação dos vértices de um polígono a pares ordenados.')
objeto_de_conhecimento_110.save();
objeto_de_conhecimento_111 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 28,ano= 6,objeto_de_conhecimento_nome='Prismas e pirâmides: planificações e relações entre seus elementos vértices, faces e arestas).')
objeto_de_conhecimento_111.save();
objeto_de_conhecimento_112 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 28,ano= 6,objeto_de_conhecimento_nome='Polígonos: classificações quanto ao número de vértices, às medidas de lados e ângulos e ao paralelismo e perpendicularismo dos lados.')
objeto_de_conhecimento_112.save();
objeto_de_conhecimento_113 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 28,ano= 6,objeto_de_conhecimento_nome='Construção de figuras semelhantes: ampliação e redução de figuras planas em malhas quadriculadas.')
objeto_de_conhecimento_113.save();
objeto_de_conhecimento_114 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 28,ano= 6,objeto_de_conhecimento_nome='Construção de retas paralelas e perpendiculares, fazendo uso de réguas, esquadros e softwares.')
objeto_de_conhecimento_114.save();
objeto_de_conhecimento_115 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 29,ano= 6,objeto_de_conhecimento_nome='Problemas sobre medidas envolvendo grandezas como comprimento, massa, tempo, temperatura, área, capacidade e volume.')
objeto_de_conhecimento_115.save();
objeto_de_conhecimento_116 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 29,ano= 6,objeto_de_conhecimento_nome='Ângulos: noção, usos e medida.')
objeto_de_conhecimento_116.save();
objeto_de_conhecimento_117 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 29,ano= 6,objeto_de_conhecimento_nome='Plantas baixas e vistas aéreas.')
objeto_de_conhecimento_117.save();
objeto_de_conhecimento_118 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 29,ano= 6,objeto_de_conhecimento_nome='Perímetro de um quadrado como grandeza proporcional à medida do lado.')
objeto_de_conhecimento_118.save();
objeto_de_conhecimento_119 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 30,ano= 6,objeto_de_conhecimento_nome='Cálculo de probabilidade como a razão entre o número de resultados favoráveis e o total de resultados possíveis em um espaço amostral equiprovável; Cálculo de probabilidade por meio de muitas repetições de um experimento frequências de ocorrências e probabilidade frequentista).')
objeto_de_conhecimento_119.save();
objeto_de_conhecimento_120 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 30,ano= 6,objeto_de_conhecimento_nome='Leitura e interpretação de tabelas e gráficos de colunas ou barras simples ou múltiplas) referentes a variáveis categóricas e variáveis numéricas.')
objeto_de_conhecimento_120.save();
objeto_de_conhecimento_121 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 30,ano= 6,objeto_de_conhecimento_nome='Coleta de dados, organização e registro; Construção de diferentes tipos de gráficos para representá-los e interpretação das informações.')
objeto_de_conhecimento_121.save();
objeto_de_conhecimento_122 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 30,ano= 6,objeto_de_conhecimento_nome='Diferentes tipos de representação de informações: gráficos e fluxogramas.')
objeto_de_conhecimento_122.save();
objeto_de_conhecimento_123 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 31,ano= 7,objeto_de_conhecimento_nome='Múltiplos e divisores de um número natural.')
objeto_de_conhecimento_123.save();
objeto_de_conhecimento_124 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 31,ano= 7,objeto_de_conhecimento_nome='Cálculo de porcentagens e de acréscimos e decréscimos simples.')
objeto_de_conhecimento_124.save();
objeto_de_conhecimento_125 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 31,ano= 7,objeto_de_conhecimento_nome='Números inteiros: usos, história, ordenação, associação com pontos da reta numérica e operações.')
objeto_de_conhecimento_125.save();
objeto_de_conhecimento_126 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 31,ano= 7,objeto_de_conhecimento_nome='Fração e seus significados: como parte de inteiros, resultado da divisão, razão e operador.')
objeto_de_conhecimento_126.save();
objeto_de_conhecimento_127 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 31,ano= 7,objeto_de_conhecimento_nome='Números racionais na representação fracionária e na decimal: usos, ordenação e associação com pontos da reta numérica e operações.')
objeto_de_conhecimento_127.save();
objeto_de_conhecimento_128 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 32,ano= 7,objeto_de_conhecimento_nome='Linguagem algébrica: variável e incógnita.')
objeto_de_conhecimento_128.save();
objeto_de_conhecimento_129 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 32,ano= 7,objeto_de_conhecimento_nome='Equivalência de expressões algébricas: identificação da regularidade de uma sequência numérica.')
objeto_de_conhecimento_129.save();
objeto_de_conhecimento_130 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 32,ano= 7,objeto_de_conhecimento_nome='Problemas envolvendo grandezas diretamente proporcionais e grandezas inversamente proporcionais.')
objeto_de_conhecimento_130.save();
objeto_de_conhecimento_131 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 32,ano= 7,objeto_de_conhecimento_nome='Equações polinomiais do 1º grau.')
objeto_de_conhecimento_131.save();
objeto_de_conhecimento_132 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 33,ano= 7,objeto_de_conhecimento_nome='Transformações geométricas de polígonos no plano cartesiano: multiplicação das coordenadas por um número inteiro e obtenção de simétricos em relação aos eixos e à origem.')
objeto_de_conhecimento_132.save();
objeto_de_conhecimento_133 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 33,ano= 7,objeto_de_conhecimento_nome='Simetrias de translação, rotação e reflexão.')
objeto_de_conhecimento_133.save();
objeto_de_conhecimento_134 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 33,ano= 7,objeto_de_conhecimento_nome='A circunferência como lugar geométrico.')
objeto_de_conhecimento_134.save();
objeto_de_conhecimento_135 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 33,ano= 7,objeto_de_conhecimento_nome='Relações entre os ângulos formados por retas paralelas intersectadas por uma transversal.')
objeto_de_conhecimento_135.save();
objeto_de_conhecimento_136 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 33,ano= 7,objeto_de_conhecimento_nome='Triângulos: construção, condição de existência e soma das medidas dos ângulos internos.')
objeto_de_conhecimento_136.save();
objeto_de_conhecimento_137 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 33,ano= 7,objeto_de_conhecimento_nome='Polígonos regulares: quadrado e triângulo equilátero.')
objeto_de_conhecimento_137.save();
objeto_de_conhecimento_138 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 34,ano= 7,objeto_de_conhecimento_nome='Problemas envolvendo medições.')
objeto_de_conhecimento_138.save();
objeto_de_conhecimento_139 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 34,ano= 7,objeto_de_conhecimento_nome='Cálculo de volume de blocos retangulares, utilizando unidades de medida convencionais mais usuais.')
objeto_de_conhecimento_139.save();
objeto_de_conhecimento_140 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 34,ano= 7,objeto_de_conhecimento_nome='Equivalência de área de figuras planas: cálculo de áreas de figuras que podem ser decompostas por outras, cujas áreas podem ser facilmente determinadas como triângulos e quadriláteros.')
objeto_de_conhecimento_140.save();
objeto_de_conhecimento_141 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 34,ano= 7,objeto_de_conhecimento_nome='Medida do comprimento da circunferência.')
objeto_de_conhecimento_141.save();
objeto_de_conhecimento_142 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 35,ano= 7,objeto_de_conhecimento_nome='Experimentos aleatórios: espaço amostral e estimativa de probabilidade por meio de frequência de ocorrências.')
objeto_de_conhecimento_142.save();
objeto_de_conhecimento_143 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 35,ano= 7,objeto_de_conhecimento_nome='Estatística: média e amplitude de um conjunto de dados.')
objeto_de_conhecimento_143.save();
objeto_de_conhecimento_144 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 35,ano= 7,objeto_de_conhecimento_nome='Pesquisa amostral e pesquisa censitária; Planejamento de pesquisa, coleta e organização dos dados, construção de tabelas e gráficos e interpretação das informações.')
objeto_de_conhecimento_144.save();
objeto_de_conhecimento_145 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 35,ano= 7,objeto_de_conhecimento_nome='Gráficos de setores: interpretação, pertinência e construção para representar conjunto de dados.')
objeto_de_conhecimento_145.save();
objeto_de_conhecimento_146 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 36,ano= 8,objeto_de_conhecimento_nome='Notação científica.')
objeto_de_conhecimento_146.save();
objeto_de_conhecimento_147 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 36,ano= 8,objeto_de_conhecimento_nome='Potenciação e radiciação.')
objeto_de_conhecimento_147.save();
objeto_de_conhecimento_148 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 36,ano= 8,objeto_de_conhecimento_nome='O princípio multiplicativo da contagem.')
objeto_de_conhecimento_148.save();
objeto_de_conhecimento_149 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 36,ano= 8,objeto_de_conhecimento_nome='Porcentagens.')
objeto_de_conhecimento_149.save();
objeto_de_conhecimento_150 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 36,ano= 8,objeto_de_conhecimento_nome='Dízimas periódicas: fração geratriz.')
objeto_de_conhecimento_150.save();
objeto_de_conhecimento_151 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 37,ano= 8,objeto_de_conhecimento_nome='Valor numérico de expressões algébricas.')
objeto_de_conhecimento_151.save();
objeto_de_conhecimento_152 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 37,ano= 8,objeto_de_conhecimento_nome='Associação de uma equação linear de 1º grau a uma reta no plano cartesiano.')
objeto_de_conhecimento_152.save();
objeto_de_conhecimento_153 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 37,ano= 8,objeto_de_conhecimento_nome='Sistema de equações polinomiais de 1º grau: resolução algébrica e representação no plano cartesiano.')
objeto_de_conhecimento_153.save();
objeto_de_conhecimento_154 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 37,ano= 8,objeto_de_conhecimento_nome='Equação polinomial de 2º grau do tipo ax² = b.')
objeto_de_conhecimento_154.save();
objeto_de_conhecimento_155 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 37,ano= 8,objeto_de_conhecimento_nome='Sequências recursivas e não recursivas.')
objeto_de_conhecimento_155.save();
objeto_de_conhecimento_156 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 37,ano= 8,objeto_de_conhecimento_nome='Variação de grandezas: diretamente proporcionais, inversamente proporcionais ou não proporcionais.')
objeto_de_conhecimento_156.save();
objeto_de_conhecimento_157 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 38,ano= 8,objeto_de_conhecimento_nome='Congruência de triângulos e demonstrações de propriedades de quadriláteros.')
objeto_de_conhecimento_157.save();
objeto_de_conhecimento_158 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 38,ano= 8,objeto_de_conhecimento_nome='Construções geométricas: ângulos de 90°, 60°, 45° e 30° e polígonos regulares.')
objeto_de_conhecimento_158.save();
objeto_de_conhecimento_159 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 38,ano= 8,objeto_de_conhecimento_nome='Mediatriz e bissetriz como lugares geométricos: construção e problemas.')
objeto_de_conhecimento_159.save();
objeto_de_conhecimento_160 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 38,ano= 8,objeto_de_conhecimento_nome='Transformações geométricas: simetrias de translação, reflexão e rotação.')
objeto_de_conhecimento_160.save();
objeto_de_conhecimento_161 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 39,ano= 8,objeto_de_conhecimento_nome='Área de figuras planas; Área do círculo e comprimento de sua circunferência.')
objeto_de_conhecimento_161.save();
objeto_de_conhecimento_162 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 39,ano= 8,objeto_de_conhecimento_nome='Volume de bloco retangular; Medidas de capacidade.')
objeto_de_conhecimento_162.save();
objeto_de_conhecimento_163 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 40,ano= 8,objeto_de_conhecimento_nome='Princípio multiplicativo da contagem; Soma das probabilidades de todos os elementos de um espaço amostral')
objeto_de_conhecimento_163.save();
objeto_de_conhecimento_164 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 40,ano= 8,objeto_de_conhecimento_nome='Gráficos de barras, colunas, linhas ou setores e seus elementos constitutivos e adequação para determinado conjunto de dados.')
objeto_de_conhecimento_164.save();
objeto_de_conhecimento_165 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 40,ano= 8,objeto_de_conhecimento_nome='Organização dos dados de uma variável contínua em classes.')
objeto_de_conhecimento_165.save();
objeto_de_conhecimento_166 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 40,ano= 8,objeto_de_conhecimento_nome='Medidas de tendência central e de dispersão.')
objeto_de_conhecimento_166.save();
objeto_de_conhecimento_167 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 40,ano= 8,objeto_de_conhecimento_nome='Pesquisas censitária ou amostral; Planejamento e execução de pesquisa amostral')
objeto_de_conhecimento_167.save();
objeto_de_conhecimento_168 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 41,ano= 9,objeto_de_conhecimento_nome='Necessidade dos números reais para medir qualquer segmento de reta; Números irracionais: reconhecimento e localização de alguns na reta numérica.')
objeto_de_conhecimento_168.save();
objeto_de_conhecimento_169 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 41,ano= 9,objeto_de_conhecimento_nome='Potências com expoentes negativos e fracionários.')
objeto_de_conhecimento_169.save();
objeto_de_conhecimento_170 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 41,ano= 9,objeto_de_conhecimento_nome='Números reais: notação científica e problemas.')
objeto_de_conhecimento_170.save();
objeto_de_conhecimento_171 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 41,ano= 9,objeto_de_conhecimento_nome='Porcentagens: problemas que envolvem cálculo de percentuais sucessivos.')
objeto_de_conhecimento_171.save();
objeto_de_conhecimento_172 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 42,ano= 9,objeto_de_conhecimento_nome='Funções: representações numérica, algébrica e gráfica.')
objeto_de_conhecimento_172.save();
objeto_de_conhecimento_173 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 42,ano= 9,objeto_de_conhecimento_nome='Razão entre grandezas de espécies diferentes.')
objeto_de_conhecimento_173.save();
objeto_de_conhecimento_174 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 42,ano= 9,objeto_de_conhecimento_nome='Grandezas diretamente proporcionais e grandezas inversamente proporcionais.')
objeto_de_conhecimento_174.save();
objeto_de_conhecimento_175 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 42,ano= 9,objeto_de_conhecimento_nome='Expressões algébricas: fatoração e produtos notáveis; Resolução de equações polinomiais do 2º grau por meio de fatorações.')
objeto_de_conhecimento_175.save();
objeto_de_conhecimento_176 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Demonstrações de relações entre os ângulos formados por retas paralelas intersectadas por uma transversal.')
objeto_de_conhecimento_176.save();
objeto_de_conhecimento_177 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Relações entre arcos e ângulos na circunferência de um círculo.')
objeto_de_conhecimento_177.save();
objeto_de_conhecimento_178 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Semelhança de triângulos.')
objeto_de_conhecimento_178.save();
objeto_de_conhecimento_179 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Relações métricas no triângulo retângulo; Teorema de Pitágoras: verificações experimentais e demonstração Retas paralelas cortadas por transversais: teoremas de proporcionalidade e verificações experimentais.')
objeto_de_conhecimento_179.save();
objeto_de_conhecimento_180 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Polígonos regulares.')
objeto_de_conhecimento_180.save();
objeto_de_conhecimento_181 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Distância entre pontos no plano cartesiano.')
objeto_de_conhecimento_181.save();
objeto_de_conhecimento_182 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 43,ano= 9,objeto_de_conhecimento_nome='Vistas ortogonais de figuras espaciais.')
objeto_de_conhecimento_182.save();
objeto_de_conhecimento_183 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 44,ano= 9,objeto_de_conhecimento_nome='Unidades de medida para medir distâncias muito grandes e muito pequenas; Unidades de medida utilizadas na informática.')
objeto_de_conhecimento_183.save();
objeto_de_conhecimento_184 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 44,ano= 9,objeto_de_conhecimento_nome='Volume de prismas e cilindros.')
objeto_de_conhecimento_184.save();
objeto_de_conhecimento_185 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 45,ano= 9,objeto_de_conhecimento_nome='Análise de probabilidade de eventos aleatórios: eventos dependentes e independentes.')
objeto_de_conhecimento_185.save();
objeto_de_conhecimento_186 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 45,ano= 9,objeto_de_conhecimento_nome='Análise de gráficos divulgados pela mídia: elementos que podem induzir a erros de leitura ou de interpretação.')
objeto_de_conhecimento_186.save();
objeto_de_conhecimento_187 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 45,ano= 9,objeto_de_conhecimento_nome='Leitura, interpretação e representação de dados de pesquisa expressos em tabelas de dupla entrada, gráficos de colunas simples e agrupadas, gráficos de barras e de setores e gráficos pictóricos.')
objeto_de_conhecimento_187.save();
objeto_de_conhecimento_188 = ObjetoDeConhecimento(etapa=5,unidade_tematica= 45,ano= 9,objeto_de_conhecimento_nome='Planejamento e execução de pesquisa amostral e apresentação de relatório.')
objeto_de_conhecimento_188.save();

from questao.models import UnidadeTematica
unidade_tematica_1 = UnidadeTematica(etapa=4,ano= 1,unidade_tematica_nome= 'Números')
unidade_tematica_1.save();
unidade_tematica_2 = UnidadeTematica(etapa=4,ano= 1,unidade_tematica_nome= 'Álgebra')
unidade_tematica_2.save();
unidade_tematica_3 = UnidadeTematica(etapa=4,ano= 1,unidade_tematica_nome= 'Geometria')
unidade_tematica_3.save();
unidade_tematica_4 = UnidadeTematica(etapa=4,ano= 1,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_4.save();
unidade_tematica_5 = UnidadeTematica(etapa=4,ano= 1,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_5.save();
unidade_tematica_6 = UnidadeTematica(etapa=4,ano= 2,unidade_tematica_nome= 'Números')
unidade_tematica_6.save();
unidade_tematica_7 = UnidadeTematica(etapa=4,ano= 2,unidade_tematica_nome= 'Álgebra')
unidade_tematica_7.save();
unidade_tematica_8 = UnidadeTematica(etapa=4,ano= 2,unidade_tematica_nome= 'Geometria')
unidade_tematica_8.save();
unidade_tematica_9 = UnidadeTematica(etapa=4,ano= 2,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_9.save();
unidade_tematica_10 = UnidadeTematica(etapa=4,ano= 2,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_10.save();
unidade_tematica_11 = UnidadeTematica(etapa=4,ano= 3,unidade_tematica_nome= 'Números')
unidade_tematica_11.save();
unidade_tematica_12 = UnidadeTematica(etapa=4,ano= 3,unidade_tematica_nome= 'Álgebra')
unidade_tematica_12.save();
unidade_tematica_13 = UnidadeTematica(etapa=4,ano= 3,unidade_tematica_nome= 'Geometria')
unidade_tematica_13.save();
unidade_tematica_14 = UnidadeTematica(etapa=4,ano= 3,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_14.save();
unidade_tematica_15 = UnidadeTematica(etapa=4,ano= 3,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_15.save();
unidade_tematica_16 = UnidadeTematica(etapa=4,ano= 4,unidade_tematica_nome= 'Números')
unidade_tematica_16.save();
unidade_tematica_17 = UnidadeTematica(etapa=4,ano= 4,unidade_tematica_nome= 'Álgebra')
unidade_tematica_17.save();
unidade_tematica_18 = UnidadeTematica(etapa=4,ano= 4,unidade_tematica_nome= 'Geometria')
unidade_tematica_18.save();
unidade_tematica_19 = UnidadeTematica(etapa=4,ano= 4,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_19.save();
unidade_tematica_20 = UnidadeTematica(etapa=4,ano= 4,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_20.save();
unidade_tematica_21 = UnidadeTematica(etapa=4,ano= 5,unidade_tematica_nome= 'Números')
unidade_tematica_21.save();
unidade_tematica_22 = UnidadeTematica(etapa=4,ano= 5,unidade_tematica_nome= 'Álgebra')
unidade_tematica_22.save();
unidade_tematica_23 = UnidadeTematica(etapa=4,ano= 5,unidade_tematica_nome= 'Geometria')
unidade_tematica_23.save();
unidade_tematica_24 = UnidadeTematica(etapa=4,ano= 5,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_24.save();
unidade_tematica_25 = UnidadeTematica(etapa=4,ano= 5,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_25.save();
unidade_tematica_26 = UnidadeTematica(etapa=5,ano= 6,unidade_tematica_nome= 'Números')
unidade_tematica_26.save();
unidade_tematica_27 = UnidadeTematica(etapa=5,ano= 6,unidade_tematica_nome= 'Álgebra')
unidade_tematica_27.save();
unidade_tematica_28 = UnidadeTematica(etapa=5,ano= 6,unidade_tematica_nome= 'Geometria')
unidade_tematica_28.save();
unidade_tematica_29 = UnidadeTematica(etapa=5,ano= 6,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_29.save();
unidade_tematica_30 = UnidadeTematica(etapa=5,ano= 6,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_30.save();
unidade_tematica_31 = UnidadeTematica(etapa=5,ano= 7,unidade_tematica_nome= 'Números')
unidade_tematica_31.save();
unidade_tematica_32 = UnidadeTematica(etapa=5,ano= 7,unidade_tematica_nome= 'Álgebra')
unidade_tematica_32.save();
unidade_tematica_33 = UnidadeTematica(etapa=5,ano= 7,unidade_tematica_nome= 'Geometria')
unidade_tematica_33.save();
unidade_tematica_34 = UnidadeTematica(etapa=5,ano= 7,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_34.save();
unidade_tematica_35 = UnidadeTematica(etapa=5,ano= 7,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_35.save();
unidade_tematica_36 = UnidadeTematica(etapa=5,ano= 8,unidade_tematica_nome= 'Números')
unidade_tematica_36.save();
unidade_tematica_37 = UnidadeTematica(etapa=5,ano= 8,unidade_tematica_nome= 'Álgebra')
unidade_tematica_37.save();
unidade_tematica_38 = UnidadeTematica(etapa=5,ano= 8,unidade_tematica_nome= 'Geometria')
unidade_tematica_38.save();
unidade_tematica_39 = UnidadeTematica(etapa=5,ano= 8,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_39.save();
unidade_tematica_40 = UnidadeTematica(etapa=5,ano= 8,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_40.save();
unidade_tematica_41 = UnidadeTematica(etapa=5,ano= 9,unidade_tematica_nome= 'Números')
unidade_tematica_41.save();
unidade_tematica_42 = UnidadeTematica(etapa=5,ano= 9,unidade_tematica_nome= 'Álgebra')
unidade_tematica_42.save();
unidade_tematica_43 = UnidadeTematica(etapa=5,ano= 9,unidade_tematica_nome= 'Geometria')
unidade_tematica_43.save();
unidade_tematica_44 = UnidadeTematica(etapa=5,ano= 9,unidade_tematica_nome= 'Grandezas e medidas')
unidade_tematica_44.save()
unidade_tematica_45 = UnidadeTematica(etapa=5,ano= 9,unidade_tematica_nome= 'Probabilidade e estatística')
unidade_tematica_45.save()

from usuario.models import Usuario
from rest_framework.authtoken.models import Token
# super administrador - Cadastra os betas
usuario_1 = Usuario(nome='Alfa', sobrenome='01', email='alfa@bq.mat.br',  escolaridade='-----', nivel_de_acesso='alfa')
usuario_1.set_password('23571113')
usuario_1.save()
Token.objects.create(user=usuario_1)
# administrador nivel 1 - Administrador do IFNMG - Cordena um deupo de diretores
usuario_2 = Usuario(nome='Beta', sobrenome='01', email='beta@bq.mat.br',  escolaridade='-----', nivel_de_acesso='beta')
usuario_2.set_password('23571113')
usuario_2.save()
Token.objects.create(user=usuario_2)
# administrador nivel 2 - Diretores de escola - Cordenam um grupo de pibidianos
usuario_3 = Usuario(nome='Gama', sobrenome='01', email='gama@bq.mat.br',  escolaridade='-----', nivel_de_acesso='gama')
usuario_3.set_password('23571113')
usuario_3.save()
Token.objects.create(user=usuario_3)
# administrador nivel 3 - Pibidianos - Inserem as questoes
usuario_4 = Usuario(nome='Delta', sobrenome='01', email='delta@bq.mat.br',  escolaridade='-----', nivel_de_acesso='delta')
usuario_4.set_password('23571113')
usuario_4.save()
Token.objects.create(user=usuario_4)
# usuario final
usuario_5 = Usuario(nome='Epsilon', sobrenome='01', email='epsilon@bq.mat.br',  escolaridade='-----', nivel_de_acesso='epsilon')
usuario_5.set_password('23571113')
usuario_5.save()
Token.objects.create(user=usuario_5)

from usuario.models import Filiacao
filiacao_1 = Filiacao(superior='1', inferior='2')
filiacao_1.save()
filiacao_2 = Filiacao(superior='2', inferior='3')
filiacao_2.save()
filiacao_3 = Filiacao(superior='3', inferior='4')
filiacao_3.save()