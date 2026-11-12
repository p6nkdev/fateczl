.data
msgNum1: .asciiz "Digite o primeiro numero: "
msgNum2: .asciiz "Digite o segundo numero (nao pode ser zero): "
msgErro: .asciiz "Valor invalido. Digite novamente.\n"
msgQuociente: .asciiz "Divisao inteira = "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgNum1
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

lerSegundo:
    li $v0, 4
    la $a0, msgNum2
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    bne $t1, $zero, dividir

    li $v0, 4
    la $a0, msgErro
    syscall
    j lerSegundo

dividir:
    div $t0, $t1
    mflo $t2

    li $v0, 4
    la $a0, msgQuociente
    syscall

    li $v0, 1
    add $a0, $t2, $zero
    syscall

    li $v0, 10
    syscall
