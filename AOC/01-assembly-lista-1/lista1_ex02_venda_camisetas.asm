.data
msgP: .asciiz "Quantidade de camisetas pequenas: "
msgM: .asciiz "Quantidade de camisetas medias: "
msgG: .asciiz "Quantidade de camisetas grandes: "
msgTotal: .asciiz "Valor arrecadado = R$ "

.text
.globl main
main:
    li $v0, 4
    la $a0, msgP
    syscall

    li $v0, 5
    syscall
    add $t0, $v0, $zero

    li $v0, 4
    la $a0, msgM
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    li $v0, 4
    la $a0, msgG
    syscall

    li $v0, 5
    syscall
    add $t2, $v0, $zero

    li $t3, 10
    li $t4, 12
    li $t5, 15

    mul $t6, $t0, $t3
    mul $t7, $t1, $t4
    mul $t8, $t2, $t5
    add $t9, $t6, $t7
    add $t9, $t9, $t8

    li $v0, 4
    la $a0, msgTotal
    syscall

    li $v0, 1
    add $a0, $t9, $zero
    syscall

    li $v0, 10
    syscall
