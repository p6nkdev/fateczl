.data
msgAltura: .asciiz "Digite a altura em cm da pessoa: "
msgMenor: .asciiz "Menor altura = "
msgMaior: .asciiz "\nMaior altura = "

.text
.globl main
main:
    li $t0, 0

lerPrimeira:
    li $v0, 4
    la $a0, msgAltura
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero
    add $t2, $t1, $zero
    add $t3, $t1, $zero
    addi $t0, $t0, 1

loop:
    beq $t0, 15, mostrar

    li $v0, 4
    la $a0, msgAltura
    syscall

    li $v0, 5
    syscall
    add $t1, $v0, $zero

    blt $t1, $t2, novoMenor
verificaMaior:
    bgt $t1, $t3, novoMaior
continua:
    addi $t0, $t0, 1
    j loop

novoMenor:
    add $t2, $t1, $zero
    j verificaMaior

novoMaior:
    add $t3, $t1, $zero
    j continua

mostrar:
    li $v0, 4
    la $a0, msgMenor
    syscall

    li $v0, 1
    add $a0, $t2, $zero
    syscall

    li $v0, 4
    la $a0, msgMaior
    syscall

    li $v0, 1
    add $a0, $t3, $zero
    syscall

    li $v0, 10
    syscall
