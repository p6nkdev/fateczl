.data
msgNum: .asciiz "Digite um numero inteiro: "
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

    andi $t1, $t0, 1
    beq $t1, $zero, ehPar

    addi $t2, $t0, 8
    j mostrar

ehPar:
    addi $t2, $t0, 5

mostrar:
    li $v0, 4
    la $a0, msgRes
    syscall

    li $v0, 1
    add $a0, $t2, $zero
    syscall

    li $v0, 10
    syscall
