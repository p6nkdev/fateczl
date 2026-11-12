.data
msgEntrada: .asciiz "Digite um numero de 0 a 100 (negativo encerra): "
msgInvalido: .asciiz "Valor invalido. Digite um numero entre 0 e 100.\n"
msgA: .asciiz "Intervalo [0-25]: "
msgB: .asciiz "\nIntervalo [26-50]: "
msgC: .asciiz "\nIntervalo [51-75]: "
msgD: .asciiz "\nIntervalo [76-100]: "

.text
.globl main
main:
    li $t0, 0
    li $t1, 0
    li $t2, 0
    li $t3, 0

lerNumero:
    li $v0, 4
    la $a0, msgEntrada
    syscall

    li $v0, 5
    syscall
    add $t4, $v0, $zero

    bltz $t4, mostrar
    bgt $t4, 100, invalido
    ble $t4, 25, faixaA
    ble $t4, 50, faixaB
    ble $t4, 75, faixaC
    addi $t3, $t3, 1
    j lerNumero

invalido:
    li $v0, 4
    la $a0, msgInvalido
    syscall
    j lerNumero

faixaA:
    addi $t0, $t0, 1
    j lerNumero

faixaB:
    addi $t1, $t1, 1
    j lerNumero

faixaC:
    addi $t2, $t2, 1
    j lerNumero

mostrar:
    li $v0, 4
    la $a0, msgA
    syscall

    li $v0, 1
    add $a0, $t0, $zero
    syscall

    li $v0, 4
    la $a0, msgB
    syscall

    li $v0, 1
    add $a0, $t1, $zero
    syscall

    li $v0, 4
    la $a0, msgC
    syscall

    li $v0, 1
    add $a0, $t2, $zero
    syscall

    li $v0, 4
    la $a0, msgD
    syscall

    li $v0, 1
    add $a0, $t3, $zero
    syscall

    li $v0, 10
    syscall
