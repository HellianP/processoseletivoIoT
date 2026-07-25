from machine import Pin, ADC
import time

print("Contador de Producao Inicializado")

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

LIMIAR_ENTRADA = 2000
LIMIAR_SAIDA = 1200

contador = 0
peca_passando = False

tempo_inicio = 0
micro_parada = False

botao = Pin(4, Pin.IN, Pin.PULL_UP)

ultimo_estado_botao = botao.value()
tempo_pressionado = None

while True:
    valor = ldr.read()
    estado_botao = botao.value()
    agora = time.ticks_ms()

    # Botão pressionado
    if ultimo_estado_botao == 1 and estado_botao == 0:
        tempo_pressionado = agora

    # Botão solto
    elif ultimo_estado_botao == 0 and estado_botao == 1:
        if tempo_pressionado is not None:
            if time.ticks_diff(agora, tempo_pressionado) >= 50:
                contador = 0
                peca_passando = False
                micro_parada = False
                tempo_inicio = 0
                print("Turno resetado com sucesso. Contadores zerados.")
            tempo_pressionado = None

    ultimo_estado_botao = estado_botao

    # Peça entrou
    if not peca_passando and valor >= LIMIAR_ENTRADA:
        peca_passando = True
        tempo_inicio = time.ticks_ms()
        micro_parada = False

    # Peça está passando: verificar micro-parada e saída
    if peca_passando:
        # verificar micro-parada
        if not micro_parada:
            if time.ticks_diff(time.ticks_ms(), tempo_inicio) >= 5000:
                print("Alerta: Micro-parada detectada!")
                micro_parada = True

        # verificar se a peça saiu
        if valor <= LIMIAR_SAIDA:
            contador += 1
            print(f"Peca detectada! Total: {contador}")
            peca_passando = False

    time.sleep_ms(20)