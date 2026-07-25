## Relatório do Candidato

### Identificação do Candidato

- **Nome completo:Hellian Sampaio Silva Peixinho **
- **GitHub:https://github.com/HellianP**

---

## Visão Geral da Solução

O projeto consiste em um contador de produção não intrusivo utilizando um ESP32 simulado no Wokwi. O sistema monitora a passagem de peças por meio de um sensor LDR, contabilizando cada objeto detectado, identificando situações de micro-parada na linha de produção e permitindo o reset dos contadores através de um botão físico.

A interação do usuário ocorre pela alteração da luminosidade incidente no sensor LDR e também pelo acionamento do botão de reset, enquanto as informações de status e alarmes são disponibilizadas pelo monitor serial.

---

## Arquitetura do Sistema Embarcado

O firmware foi desenvolvido em MicroPython utilizando um laço principal (while True) responsável por executar continuamente as leituras do sensor e do botão.

A lógica implementada é baseada em estados:

Inicialização do sistema com configuração do sensor LDR e botão.
Monitoramento contínuo da leitura analógica do LDR.
Detecção da entrada de uma peça quando o valor do sensor ultrapassa o limiar de entrada.
Contagem da peça quando a luminosidade retorna ao estado normal.
Monitoramento do tempo de permanência da peça para identificação de micro-paradas.
Tratamento do botão utilizando debounce para reinicialização dos contadores.

A lógica foi implementada utilizando uma máquina de estados simples e priorizando legibilidade, assim como baixo acoplamento e facilidade de manutenção.

---

## Componentes Utilizados na Simulação

Componentes utilizados:

ESP32 DevKit C V4: Microcontrolador central responsável pelo processamento lógico do firmware.

Sensor Fotoresistor (LDR) conectado ao ADC (GPIO 34): Responsável pela detecção da passagem das peças através da variação analógica de luminosidade.

Botão (Push Button) conectado ao GPIO 4: Utilizado para a reinicialização manual dos contadores do turno.

Monitor Serial (UART): Interface de comunicação utilizada para exibir mensagens de inicialização, contagem de peças, alertas de micro-parada e confirmação de reset.
---

## Decisões Técnicas Relevantes

Durante o desenvolvimento foram adotadas as seguintes decisões:

Separação das variáveis de controle em estados simples (peca_passando, micro_parada e contador).
Utilização de limiares de entrada e saída diferentes para evitar múltiplas contagens durante pequenas oscilações do sensor.
Utilização de time.ticks_ms() para medição de tempo sem bloqueios longos na execução do firmware.
Implementação de debounce para o botão de reset utilizando comparação de tempo, evitando múltiplos acionamentos durante um único pressionamento.
Mensagens seriais implementada conforme especificado no enunciado para garantir compatibilidade com os testes automatizados do Wokwi CI.

---

## Resultados Obtidos

O sistema desenvolvido atende aos requisitos propostos:

Inicialização correta do firmware.
Contagem de peças através da leitura do sensor LDR.
Detecção de micro-paradas após permanência prolongada da peça sobre o sensor.
Reset correto dos contadores por meio do botão físico.
Compatibilidade com os cenários de validação automatizados do Wokwi CI.
---

## Comentários Adicionais (Opcional)

Durante o desenvolvimento foi necessário ajustar os limiares de leitura do sensor LDR de acordo com os valores fornecidos pelo simulador do Wokwi, bem como revisar o tratamento de debounce do botão para garantir apenas um reset por acionamento.

A principal aprendizagem obtida foi a importância da implementação de máquinas de estado simples e do uso de lógica não bloqueante em sistemas embarcados, especialmente quando integrados a testes automatizados.
---
