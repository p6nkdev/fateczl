.data
msgNum: .asciiz "Digite um numero: "
msgRes: .asciiz "Resultado = "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgNum
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    bltz $t0, negativo

    add $t1, $t0, $t0
    j mostrar

negativo:
    add $t1, $t0, $t0
    add $t1, $t1, $t0

mostrar:
    li $v0, 4
    la $a0, msgRes
    syscall

    li $v0, 1
    add $a0, $t1, $zero
    syscall

    li $v0, 10
    syscall
