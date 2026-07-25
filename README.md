# Relatório do Candidato

## Identificação do Candidato

- **Nome completo:** Hellian Sampaio Silva Peixinho
- **GitHub:** https://github.com/HellianP

---

# Visão Geral da Solução

O projeto consiste em um contador de produção não intrusivo utilizando um ESP32 simulado no Wokwi. O sistema monitora a passagem de peças por meio de um sensor LDR, contabilizando automaticamente cada objeto detectado, identificando situações de micro-parada na linha de produção e permitindo o reset manual dos contadores por meio de um botão.

A interação do usuário ocorre pela alteração da luminosidade incidente no sensor LDR e pelo acionamento do botão de reset. As informações de funcionamento, contagem e alertas são exibidas através do monitor serial (UART).

---

# Arquitetura do Sistema Embarcado

O firmware foi desenvolvido em MicroPython utilizando um laço principal (`while True`), responsável pela leitura contínua do sensor LDR e do botão de reset.

A lógica do sistema é composta pelas seguintes etapas:

- Inicialização do sistema e configuração dos periféricos.
- Leitura contínua do sensor LDR.
- Detecção da entrada de uma peça quando o valor do sensor ultrapassa o limiar de entrada.
- Contagem da peça quando a luminosidade retorna ao estado normal.
- Monitoramento do tempo de bloqueio do sensor para identificação de micro-paradas.
- Leitura do botão com tratamento de debounce para reinicialização dos contadores.

A solução foi implementada utilizando estados simples, priorizando organização, legibilidade e facilidade de manutenção.

---

# Componentes Utilizados na Simulação

- **ESP32 DevKit C V4:** microcontrolador responsável pela execução do firmware.
- **Sensor Fotoresistor (LDR):** conectado ao ADC (GPIO 34), utilizado para detectar a passagem das peças através da variação da luminosidade.
- **Botão (Push Button):** conectado ao GPIO 4, utilizado para realizar o reset manual do turno.
- **Monitor Serial (UART):** utilizado para exibir mensagens de inicialização, contagem de peças, alertas de micro-parada e confirmação do reset.

---

# Decisões Técnicas Relevantes

Durante o desenvolvimento foram adotadas as seguintes decisões:

- Utilização de variáveis de estado (`peca_passando`, `micro_parada` e `contador`) para simplificar a lógica do sistema.
- Definição de limiares distintos de entrada e saída do sensor, reduzindo múltiplas contagens causadas por oscilações na leitura.
- Utilização de `time.ticks_ms()` para controle de tempo e detecção de micro-paradas sem bloqueios prolongados.
- Implementação de debounce por software para o botão de reset, evitando múltiplos acionamentos durante um único pressionamento.
- Implementação das mensagens seriais exatamente conforme especificado no enunciado, garantindo compatibilidade com os testes automatizados do Wokwi CI.

---

# Resultados Obtidos

O sistema desenvolvido atende aos requisitos propostos no desafio:

- Inicialização correta do firmware.
- Contagem automática de peças utilizando o sensor LDR.
- Detecção de micro-paradas após permanência prolongada da peça sobre o sensor.
- Reset correto dos contadores por meio do botão físico.
- Comunicação serial conforme especificado.
- Compatibilidade com os cenários de validação automatizados do Wokwi CI.

---

# Comentários Adicionais

Durante o desenvolvimento foi necessário ajustar os limiares de leitura do sensor LDR para os valores retornados pelo simulador Wokwi e implementar um tratamento adequado de debounce no botão de reset para evitar múltiplos acionamentos.

O projeto permitiu reforçar conceitos importantes de sistemas embarcados, como leitura de sensores analógicos, utilização de máquinas de estado simples, programação não bloqueante e integração com pipelines de testes automatizados utilizando GitHub Actions e Wokwi CI.